#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"
    
    @property
    def size(self):
        return self._size
    

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            return
        self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"  # Set condition to "New"

    def __str__(self):
        return f"{self.brand} Shoe, Size: {self.size} Condition: {self.condition}"
        