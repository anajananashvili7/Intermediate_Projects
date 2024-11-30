import json
import os


class BookManager:
    def __init__(self, json_file="books.json"):
        self.json_file = json_file
        self.books = self.load_books()

    def load_books(self):
        """Load books from the JSON file."""
        if os.path.exists(self.json_file):
            with open(self.json_file, "r") as file:
                return json.load(file)
        return []

    def save_books(self):
        """Save books to the JSON file."""
        with open(self.json_file, "w") as file:
            json.dump(self.books, file, indent=4)

    def display_books(self):
        """Display all books."""
        if not self.books:
            print("No books available.")
        else:
            print("\nList of Books:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book['title']} by {book['author']} ({book['published_year']})")

    def add_book(self, title, author, published_year):
        """Add a new book."""
        new_book = {"title": title, "author": author, "published_year": published_year}
        self.books.append(new_book)
        self.save_books()
        print(f"Book added: {title} by {author} ({published_year})")

    def delete_book(self, title):
        """Delete a book by title."""
        for book in self.books:
            if book['title'].lower() == title.lower():
                self.books.remove(book)
                self.save_books()
                print(f"Book deleted: {book['title']}")
                return
        print(f"No book found with title '{title}'.")

    def search_books(self, query):
        """Search books by title or author."""
        results = [book for book in self.books if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
        if results:
            print("\nSearch Results:")
            for idx, book in enumerate(results, start=1):
                print(f"{idx}. {book['title']} by {book['author']} ({book['published_year']})")
        else:
            print(f"No books found matching '{query}'.")


def main():
    manager = BookManager()

    while True:
        print("\n--- Book Management Menu ---")
        print("1. Display All Books")
        print("2. Add a Book")
        print("3. Delete a Book")
        print("4. Search Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manager.display_books()
        elif choice == '2':
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            published_year = input("Enter the published year: ")
            manager.add_book(title, author, published_year)
        elif choice == '3':
            title = input("Enter the title of the book to delete: ")
            manager.delete_book(title)
        elif choice == '4':
            query = input("Enter a title or author to search: ")
            manager.search_books(query)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
