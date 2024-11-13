"""
    Homework 5 (Laboratory 6)
    Task 6
    Application Starter
"""

from Book import Book
from DVD import DVD
from Magazine import Magazine



# Create Examples

book = Book("The Great Gatsby", "F. Scott Fitzgerald")
dvd = DVD("Inception", "Christopher Nolan")
magazine = Magazine("National Geographic", 2024)



# Display Information Example

print(book.display_info())
print(dvd.display_info())
print(magazine.display_info())
print()



# Check Out Example

book.check_out()
dvd.check_out()
dvd.check_out()
print()



# Return Items Example

book.return_item()
dvd.return_item()
print()



# Display the Updated Information

print(book.display_info())
print(dvd.display_info())
print(magazine.display_info())