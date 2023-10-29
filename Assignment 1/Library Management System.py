class Library: # Parent Class is Library

    def __init__(self, list_of_books): # Constructor of Library Class
        self.available_books = list_of_books


    def display_available_books(self): #--for displaying available books
        print("\nAvailable Books:")
        for book in self.available_books:
            print(book)


    def lend_book(self, requested_book): #--for lending the book
        if requested_book in self.available_books:
            self.available_books.remove(requested_book) #--remove the book from available books
            return True  
        else:
            return False  


    def add_book(self, new_book): #--for adding the book
        self.available_books.append(new_book) #--add the book to available books
        print(f"{new_book} has been added to the library.")


    def remove_book(self, book_to_remove): #--for removing the book
        if book_to_remove in self.available_books:
            self.available_books.remove(book_to_remove) #--remove the book from available books
            print(f"{book_to_remove} has been removed from the library.")
        else:
            print(f"{book_to_remove} is not in the library.")

class MemberLibrary(Library): # Child Class is MemberLibrary inherited from Library

    def __init__(self, list_of_books, checked_out_books=None): # Constructor of MemberLibrary Class
        super().__init__(list_of_books)
        if checked_out_books is None:
            self.checked_out_books = []
        else:
            self.checked_out_books = checked_out_books


    def view_checked_out_books(self): #--for viewing the checked out books  
        print("\nChecked-Out Books:")
        for book in self.checked_out_books:
            print(book)


    def lend_book(self, requested_book): #--for lending the book  
        if requested_book in self.available_books:
            success = super().lend_book(requested_book)
            if success:
                self.checked_out_books.append(requested_book)
                print("You have now borrowed the book.")
            else:
                print("Sorry, the book is not available in our list.")
        else:
            print("Sorry, the book is not available in our list.")


    def return_book(self, returned_book): #--for returning the book
        if returned_book in self.checked_out_books:
            self.checked_out_books.remove(returned_book)
            super().add_book(returned_book)
            print("You have returned the book. Thank you!")
        else:
            print("You didn't borrow this book from us.")



library = MemberLibrary(['Think and Grow Rich', 'Who Will Cry When You Die', 'For One More Day', 'The Alchemist', 'The Power of Habit', 'The Catcher in the Rye'])

while True:
    print("\nEnter 1 to display the available books.")
    print("Enter 2 to request for a book.")
    print("Enter 3 to return a book.")
    print("Enter 4 to view checked-out books.")
    print("Enter 5 to add a book to the library.")
    print("Enter 6 to remove a book from the library.")
    print("Enter 7 to exit.")
    user_choice = input("Enter your choice: ")

    if user_choice == '1': #--option for displaying available books
        library.display_available_books()
    elif user_choice == '2': #--option for requesting a book
        library.display_available_books()
        requested_book = input("Enter the name of the book you want to borrow: ")
        success = library.lend_book(requested_book)
        if success:
            print("You have now borrowed the book.")
        else:
            print("Sorry, the book is not available in our list.")
    elif user_choice == '3': #--option for returning a book
        returned_book = input("Enter the name of the book you want to return: ")
        library.return_book(returned_book)
    elif user_choice == '4': #--option for viewing checked out books
        library.view_checked_out_books()
    elif user_choice == '5': #--option for adding a book to the library
        new_book = input("Enter the name of the book to add to the library: ")
        library.add_book(new_book)
    elif user_choice == '6': #--option for removing a book from the library
        book_to_remove = input("Enter the name of the book to remove from the library: ")
        library.remove_book(book_to_remove)
    elif user_choice == '7': #--option for exiting the program
        quit()
    else:
        print("Invalid choice. Please enter a valid option.")
