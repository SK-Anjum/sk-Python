import os
import json

# File name for saving the book collection
DATA_FILE = "library.txt"

# Load existing library from file, or return an empty list if file doesn't exist
def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save current library to file
def save_books(library):
    with open(DATA_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Show the main menu
def show_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Prompt user and add a new book to the library
def add_new_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("Invalid year. Book not added.")
        return
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("✅ Book added successfully!")

# Remove a book by title
def delete_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("🗑️ Book removed successfully!")
            return
    print("❌ Book not found in your library.")

# Search books by title or author
def search_books(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the keyword: ").strip().lower()
    results = []

    for book in library:
        if (choice == "1" and keyword in book["title"].lower()) or \
           (choice == "2" and keyword in book["author"].lower()):
            results.append(book)

    if results:
        print("📖 Matching Books:")
        for i, book in enumerate(results, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("🔍 No books matched your search.")

# Display all books in the library
def list_books(library):
    if not library:
        print("📂 Your library is currently empty.")
        return
    print("📚 Your Library:")
    for idx, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Show stats: total books and read percentage
def show_statistics(library):
    total = len(library)
    if total == 0:
        print("📊 No books to analyze.")
        return
    read_books = sum(1 for book in library if book["read"])
    percent_read = (read_books / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percent_read:.1f}%")

# Main control loop
def run_manager():
    library = load_books()

    # Add sample books only if this is the first run
    if not library:
        library = [
            {
                "title": "Python Crash Course",
                "author": "Eric Matthes",
                "year": 2015,
                "genre": "Programming",
                "read": True
            },
            {
                "title": "Fluent Python",
                "author": "Luciano Ramalho",
                "year": 2015,
                "genre": "Programming",
                "read": False
            }
        ]
        print("📘 Sample Python books have been added to your library.")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_book(library)
        elif choice == "2":
            delete_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            list_books(library)
        elif choice == "5":
            show_statistics(library)
        elif choice == "6":
            save_books(library)
            print("💾 Library saved to file. Goodbye!")
            break
        else:
            print("❗ Invalid input. Please choose a number from 1 to 6.")

# Run the program
if __name__ == "__main__":
    run_manager()
