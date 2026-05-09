"""
Design Library Book Class
Problem: Create a Book class for a library management system.

Requirements:

Fields: title, author, isbn, isAvailable
Constructor that initializes all fields (book starts as available)
borrowBook(): marks book as unavailable if currently available, returns success/failure
returnBook(): marks book as available
displayInfo(): prints book details including availability status
"""

class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.isAvailable = True
    
    def borrowBook(self) -> bool:
        if self.isAvailable:
            self.isAvailable = False
            return True
        else:
            return False
    
    def returnBook(self) -> bool:
        self.isAvailable = True
    
    def displayInfo(self):
        print(f"The title is: {self.title}")
        print(f"The author is: {self.author}")
        print(f"The isbn is: {self.isbn}") 
        print("Available") if self.isAvailable else print("Unavailable")


if __name__ == "__main__":
    book1 = Book("Book1", "author1", "123-456")
    book1.borrowBook()
    book1.displayInfo() # unavailable
    