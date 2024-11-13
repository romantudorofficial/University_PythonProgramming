"""
    DVD
"""

from LibraryItem import LibraryItem



class DVD (LibraryItem):
    
    def __init__ (self, title, director, status = "available"):
        super().__init__(title, "DVD", status)
        self.director = director


    def display_info (self):
        return f"{super().display_info()}, Director: {self.director}"