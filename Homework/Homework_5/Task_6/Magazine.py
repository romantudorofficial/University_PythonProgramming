"""
    Magazine
"""

from LibraryItem import LibraryItem



class Magazine (LibraryItem):
    
    def __init__ (self, title, issue_number, status = "available"):
        super().__init__(title, "Magazine", status)
        self.issue_number = issue_number


    def display_info (self):
        return f"{super().display_info()}, Issue Number: {self.issue_number}"