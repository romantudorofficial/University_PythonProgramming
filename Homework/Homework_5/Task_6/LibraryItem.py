"""
    Library Item
"""

class LibraryItem:
    
    def __init__ (self, title, item_type, status = "available"):
        self.title = title
        self.item_type = item_type
        self.status = status


    def check_out (self):
        if self.status == "available":
            self.status = "checked out"
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")


    def return_item (self):
        if self.status == "checked out":
            self.status = "available"
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not checked out.")


    def display_info (self):
        return f"Title: {self.title}, Type: {self.item_type}, Status: {self.status}"