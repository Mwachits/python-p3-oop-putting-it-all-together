#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  # Using a private variable for page count
        self.page_count = page_count  # Calls the setter

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __str__(self):
        return f"{self.title}, Pages: {self.page_count}"