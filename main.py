from Services.addressbook import AddressBook
from Services.addressbookmanager import AdressBookManager # Import your manager
from ui.menus import main_menue, welcome_screen, address_book_menu # Import both menus
from ui.contactoperations import (
    edit_contact, deletecontact_flow, add_contact_flow, view_by_location_flow,
    create_addressbook_flow, open_addressbook_flow , search_by_location_flow , view_location_counts_flow
)
#initialize the addressbook
manager = AdressBookManager()

def manage_contacts(selected_book):
    """Sub-loop for operations inside  a specfic book"""

    while True:
        address_book_menu()
        choice = input("\nSelect an option: ")

        if choice == "1":
            add_contact_flow(selected_book)
        elif choice == "2":
            selected_book.display_contacts()
            input("\nPress Enter....")
        elif choice == "3":
            edit_contact(selected_book)
        elif choice == "4":
            deletecontact_flow(selected_book)
        elif choice == "5":
            print("GoodBye!")
            break #go back to main menu


def main():
    while True:
        welcome_screen()
        main_menue()
        choice = input("\nSelect an option: ")

        if choice == "1":
            create_addressbook_flow(manager)
            input("\nPress Enter to return to menu..")
        elif choice == "2":
            selected_book = open_addressbook_flow(manager)
            if selected_book :
                manage_contacts(selected_book)
            input("\nPress Enter to return to menu..")
        elif choice == "3":
            print("\Availabe Address Books: ")
            books = manager.list_allbooks()
            for b in books:
                print(f"- {b}")
            input("\nPress Enter to return to menu..")
        elif choice == "4":
            search_by_location_flow(manager)
            input("Press Enter to return")
        elif choice == "5": # <--- Add this case for UC9
            view_by_location_flow(manager)
            input("\nPress Enter to return to menu..")
        elif choice == "6":
            view_location_counts_flow(manager)
            input("\n Press Enter to return...")
        elif choice == "7":
            print("GoodBye!")
            break





if __name__=="__main__":
    main()