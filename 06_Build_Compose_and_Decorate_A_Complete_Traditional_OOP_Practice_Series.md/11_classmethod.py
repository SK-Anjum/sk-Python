#Class Methods
#Assignment:11
#Create a class Book with a class variable total_books.
# Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"Total books: {cls.total_books}")

    # Constructor to initialize book title and author and increment the book count

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()


# Example usage
book1 = Book("To Kill a Mockingbird", "Harper Lee")



   