"""
    Book
"""

from LibraryItem import LibraryItem



class Book (LibraryItem):
    
    def __init__ (self, title, author, status = "available"):
        super().__init__(title, "Book", status)
        self.author = author


    def display_info (self):
        return f"{super().display_info()}, Author: {self.author}"