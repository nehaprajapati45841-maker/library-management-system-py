# Library Management System

def add_book():
    book = input("Enter Book Name: ")

    with open("books.txt", "a") as file:
        file.write(book + "\n")

    print("Book Added Successfully!")


def view_books():
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

        if len(books) == 0:
            print("No Books Available")
        else:
            print("\nBooks in Library:")
            for book in books:
                print(book.strip())

    except FileNotFoundError:
        print("No Books Available")


def search_book():
    book_name = input("Enter Book Name to Search: ")

    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

        found = False

        for book in books:
            if book_name.lower() == book.strip().lower():
                found = True
                break

        if found:
            print("Book Found!")
        else:
            print("Book Not Found!")

    except FileNotFoundError:
        print("No Books Available")


def delete_book():
    book_name = input("Enter Book Name to Delete: ")

    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

        found = False

        with open("books.txt", "w") as file:
            for book in books:
                if book.strip().lower() != book_name.lower():
                    file.write(book)
                else:
                    found = True

        if found:
            print("Book Deleted Successfully!")
        else:
            print("Book Not Found!")

    except FileNotFoundError:
        print("No Books Available")


def issue_book():
    book_name = input("Enter Book Name to Issue: ")

    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

        found = False

        with open("books.txt", "w") as file:
            for book in books:
                if book.strip().lower() != book_name.lower():
                    file.write(book)
                else:
                    found = True

        if found:
            with open("issued_books.txt", "a") as file:
                file.write(book_name + "\n")

            print("Book Issued Successfully!")
        else:
            print("Book Not Found!")

    except FileNotFoundError:
        print("No Books Available")


def return_book():
    book_name = input("Enter Book Name to Return: ")

    try:
        with open("issued_books.txt", "r") as file:
            books = file.readlines()

        found = False

        with open("issued_books.txt", "w") as file:
            for book in books:
                if book.strip().lower() != book_name.lower():
                    file.write(book)
                else:
                    found = True

        if found:
            with open("books.txt", "a") as file:
                file.write(book_name + "\n")

            print("Book Returned Successfully!")
        else:
            print("Book Not Issued!")

    except FileNotFoundError:
        print("No Issued Books Found")


while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        delete_book()

    elif choice == "5":
        issue_book()

    elif choice == "6":
        return_book()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")