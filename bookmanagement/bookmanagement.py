import json
import os

# File to store book data
BOOK_FILE = 'books.json'

def load_books():
    """Load books from the JSON file."""
    if os.path.exists(BOOK_FILE):
        with open(BOOK_FILE, 'r') as file:
            return json.load(file)
    return []

def save_books(books):
    """Save books to the JSON file."""
    with open(BOOK_FILE, 'w') as file:
        json.dump(books, file, indent=4)

def display_books(books):
    """Display all books."""
    if not books:
        print("No books in the library.")
        return
    print("\nLibrary Books:")
    for idx, book in enumerate(books, start=1):
        print(f"{idx}. {book['title']} by {book['author']} (Published: {book['published_year']})")

def search_book(books):
    """Search for a book by title."""
    title = input("Enter the title of the book to search: ").strip().lower()
    found_books = [book for book in books if title in book['title'].lower()]
    if not found_books:
        print(f"No books found with title containing '{title}'.")
    else:
        print("\nSearch Results:")
        for book in found_books:
            print(f"{book['title']} by {book['author']} (Published: {book['published_year']})")

def add_book(books):
    """Add a new book to the library."""
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author of the book: ").strip()
    published_year = input("Enter the published year of the book: ").strip()
    
    books.append({"title": title, "author": author, "published_year": published_year})
    print(f"Book '{title}' added successfully!")
    save_books(books)

def delete_book(books):
    """Delete a book by title."""
    title = input("Enter the title of the book to delete: ").strip().lower()
    for book in books:
        if book['title'].lower() == title:
            books.remove(book)
            print(f"Book '{book['title']}' deleted successfully!")
            save_books(books)
            return
    print(f"No book found with title '{title}'.")

def main():
    """Main program loop."""
    books = load_books()
    while True:
        print("\nLibrary Menu:")
        print("1. Display all books")
        print("2. Search for a book")
        print("3. Add a new book")
        print("4. Delete a book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            display_books(books)
        elif choice == '2':
            search_book(books)
        elif choice == '3':
            add_book(books)
        elif choice == '4':
            delete_book(books)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
