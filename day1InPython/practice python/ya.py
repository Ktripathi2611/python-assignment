books = []

def create_book(title, author, genre):
    return {"title": title, "author": author, "genre": genre}

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")

    # Check for duplicate entries before adding
    if any(book["title"] == title for book in books):
        print(f"Book with title '{title}' already exists. Skipping...")
        return

    books.append(create_book(title, author, genre))
    print("Book added successfully!")

def remove_book():
    title = input("Enter book title to remove: ")
    for i, book in enumerate(books):
        if book["title"] == title:
            books.pop(i)
            print("Book removed (if present)!")
            return  # Exit after successful removal

def search_books(search_term, field="all"):
    search_term = search_term.lower()
    return [book for book in books if search_term in get_searchable_field(book, field)]

def get_searchable_field(book, field):
    if field == "all":
        return (book["title"].lower(), book["author"].lower(), book["genre"].lower())
    else:
        return book[field].lower()

def show_books():
    if not books:
        print("No books found in the library.")
        return
    print("\nHere are all the books:")
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")

def categorize_books():
    genres = {}
    for book in books:
        genre = book["genre"]
        genres.setdefault(genre, []).append(book)
    return genres

def display_categories():
    categorized_books = categorize_books()
    if not categorized_books:
        print("No books found in the library.")
        return
    print("\nBooks categorized by genres:")
    for genre, books in categorized_books.items():
        print(f"\nGenre: {genre}")
        for book in books:
            print(f"- {book['title']} by {book['author']}")

# User Interaction
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Books")
    print("4. Show All Books")
    print("5. Categorize Books")  # New option
    print("6. Check for Duplicate Entries")  # New option
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_term = input("Enter search term: ")
        field = input("Search in (title/author/genre/all) [all]: ") or "all"
        results = search_books(search_term, field)
        if results:
            print("\nSearch results:")
            for book in results:
                print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
        else:
            print("No matching books found.")
    elif choice == "4":
        show_books()
    elif choice == "5":
        display_categories()
    elif choice == "6":
        # Check for duplicate titles
        duplicates = [book["title"] for book in books if books.count(book) > 1]
        if duplicates:
            print("\nDuplicate books found:")
            for title in duplicates:
                print(f"- {title}")
        else:
            print("No duplicate entries found.")
    elif choice == "7":
        print("Exiting Library Management System...")
        break
    else:
        print("Invalid choice. Please try again.")
