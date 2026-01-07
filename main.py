from library.library import Library
from library.physical_book import PhysicalBook
from library.ebook import EBook
from library.member import Member

library = Library()

while True:
    print("\n--- Smart Library Menu ---")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Save Library")
    print("6. Load Library")
    print("7. Exit")

    choice = input("Choose an option: ")

    try:
        if choice == "1":
            book_type = input("Book type (physical/ebook): ").strip().lower()
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")

            if book_type == "physical":
                copies = int(input("Number of copies: "))
                library.add_book(PhysicalBook(book_id, title, author, copies))
            elif book_type == "ebook":
                size_mb = float(input("File size (MB): "))
                library.add_book(EBook(book_id, title, author, size_mb))
            else:
                print("Invalid book type!")

        elif choice == "2":
            member_id = input("Member ID: ")
            name = input("Member name: ")
            library.add_member(Member(member_id, name))

        elif choice == "3":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)
            print("Book borrowed successfully!")

        elif choice == "4":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)
            print("Book returned successfully!")

        elif choice == "5":
            library.save_to_file("data.json")
            print("Library saved!")

        elif choice == "6":
            library.load_from_file("data.json")
            print("Library loaded!")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")

    except Exception as e:
        print("Error:", e)
