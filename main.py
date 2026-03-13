from models.addressbook import AddressBook
from utilities.ui import main_menue, welcome_screen
from utilities.contactoperations import edit_contact , deletecontact_flow , add_contact_flow

#initialize the addressbook
address_book = AddressBook()


def main():
    while True:
        welcome_screen()
        main_menue()
        choice = input("\nSelect an option: ")

        if choice == "1":
            add_contact_flow(address_book)
            input("\nPress Enter to return to menu..")
        elif choice == "2":
            address_book.display_contacts()
            input("\nPress Enter to return to menu..")
        elif choice == "3":
            edit_contact(address_book)
            input("\nPress Enter to return to menu..")
        elif choice == "4":
            deletecontact_flow(address_book)
        elif choice == "5":
            print("GoodBye!")
            break
        else:
            print("Invalid choice , try again.")
            input("\n Press Enter to continue...")





if __name__=="__main__":
    main()