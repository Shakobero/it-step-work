class Book:
    def __init__(self, title, author, year, genre, country):
        # Initialize the Book object with provided attributes
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.country = country
 
class BookManager:
    def __init__(self):
        # Initialize the BookManager with an empty library
        self.library = []
 
    def add_book(self, title, author, year, genre, country):
        # Create a new Book instance and add it to the library
        new_book = Book(title, author, year, genre, country)
        self.library.append(new_book)
        print(f"Book '{title}' added in the library successfully.")
 
    def display_books(self):
        # Display all books in the library or a message if the library is empty
        if not self.library:
            print("No books available in the library.")
       
        else:
            print("\nBooks in Library:")
            # Enumerate through the library and print book details
            for i, book in enumerate(self.library, start=1):
                print(f"{i}. {book.title} by {book.author} ({book.year}) ({book.genre}) ({book.country})")
 
    def search_books(self, key):
        # Search for books with a matching title and display results
        if not self.library:
            print("No books available in the library.")
 
        else:
            results = [book for book in self.library if key.lower() in book.title.lower()]
           
            if results:
                print("\nSearch Results:")
                # Enumerate through the search results and print book details
                for i, book in enumerate(results, start=1):
                    print(f"{i}. {book.title} by {book.author} ({book.year}) ({book.genre}) ({book.country})")
           
            else:
                print("No matching books found in the library.")
 
def main():
    # Create a BookManager instance
    book_manager = BookManager()
 
    while True:
        print("\nUser Interface:")
        print("1. Add Book in the Library")
        print("2. Display All Books of the Library")
        print("3. Search Books by Title")
        print("4. Exit Library")
 
        # Get user input for the desired operation
        choice = input("Enter your choice (1-4): ")
 
        if choice == '1':
            # Add a new book to the library
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            while True:
                year = input("Enter year: ")
                try:
                    year = int(year)
                    break  # Exit the loop if the conversion is successful
                except ValueError:
                    print("Invalid input. Please enter an integer for the year.")
            genre = input("Enter the genre: ")
            country = input("Enter author's country: ")
            book_manager.add_book(title, author, year, genre, country)
       
        elif choice == '2':
            # Display all books in the library
            book_manager.display_books()
       
        elif choice == '3':
            # Search for books by title
            key = input("Enter the search title: ")
            book_manager.search_books(key)
       
        elif choice == '4':
            # Exit the library program
            print("Exiting Library. Goodbye!")
            break
       
        else:
            # Display an error message for an invalid choice
            print("Invalid choice. Please enter a number between 1 and 4.")
 
 
if __name__ == "__main__":
    # Run the main function when the script is executed
    main()