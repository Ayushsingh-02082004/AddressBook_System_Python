from models.contact import contact
from models.addressbook import AddressBook
from utilities.ui import main_menue, welcome_screen
from utilities.helper import get_input
from utilities.contactoperations import edit_contact

#initialize the addressbook
address_book = AddressBook()

def add_contact_flow():
    fields = ["First Name" , "Last Name" , "Phone Number" , "Email" , 
              "Address" , "City" , "State" , "Zip Code"]
    #Collect all the data using the helper 
    values = [get_input(field) for field in fields]
    #Create contact object and add it to the book
    # The *values unpacs the list into the 8 arguments the class needs
    new_contact = contact(*values)
    address_book.add_contact(new_contact)


def main():
    while True:
        welcome_screen()
        main_menue()
        choice = input("\nSelect an option: ")

        if choice == "1":
            add_contact_flow()
            input("\nPress Enter to return to menu..")
        elif choice == "2":
            address_book.display_contacts()
            input("\nPress Enter to return to menu..")
        elif choice == "3":
            edit_contact(address_book)
            input("\nPress Enter to return to menu..")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice , try again.")
            input("\n Press Enter to continue...")





if __name__=="__main__":
    main()