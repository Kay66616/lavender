books = []

while True:
    print("\nWelcome to the Book Title Library!")
    print("Choose an option:")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. View All Books")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        title = input("Enter the book title: ")
        if title in books:
            print(title, "is already in the library.")
        else:
            books.append(title)
            print(title, "has been added to the library.")
    
    elif choice == '2':
        title = input("Enter the book title to remove: ")
        if title in books:
            books.remove(title)
            print(title, "has been removed from the library.")
        else:
            print("Book not found.")
    
    elif choice == '3':
        if not books:
            print("No books in the library.")
        else:
            print("Books in the Library:")
            for title in books:
                print("-", title)
    
    elif choice == '4':
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Try again.")
