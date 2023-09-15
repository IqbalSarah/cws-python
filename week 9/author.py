class Author:
    def __init__(self) -> None:
        self.name: str = input("Enter name = ")
        self.age: int = int(input("Enter age = "))
        self.books: list = []

    def displayInfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def displayBooks(self):
        if not self.books:  # Checking if the list is empty
            print("The author hasn't written any books yet.")
            return
        print(f"Books by {self.name}: ")
        for book in self.books:
            print(book)

    def addBook(self):
        book_name = input("Enter the name of the book: ")
        self.books.insert(0, book_name)
        print(f"'{book_name}' has been added to the list of books.")


author = Author()
author.addBook()
author.displayInfo()
author.displayBooks()
