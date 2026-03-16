from ui.helper import get_input
from models.contact import contact
from Services.addressbook import AddressBook
from Services.sorting import sortbyName, sortbycity, sortbystate, sortbyzip


def create_addressbook_flow(manager):
    name = input("Enter a unique name for the new Addressbook : ")
    try:
        #create a new instance of AddressBook for this name
        manager.add_addressbook(name , AddressBook())
        print(f"Adress Book '{name} created successfully!")
    except ValueError as e:
        print(e)


def open_addressbook_flow(manager):
    name = input("Enter the name of the Address Book to open: ")
    try:
        # Get the specfic book from the dictionary
        current_book = manager.get_addressbook(name)
        print(f"----Currently in : {name} ---")
        return current_book
    except KeyError as e:
        print(e)
        return None


def deletecontact_flow(addressbook):
    try:
        firstname = input("Enter first name :")
        lastname = input("Enter last name : ")

        #call the delete methord from addressbook
        contact_deleted  = addressbook.delete_contact(firstname , lastname)

        if contact_deleted : 
            print(f"Contact {firstname} {lastname} deleted successfully")
        else :
            print("Contact not found .")

    except Exception as e : 
        print(f"An error occured during deletion {e}")


def add_contact_flow(address_book):
    fields = ["First Name" , "Last Name" , "Phone Number" , "Email" , 
              "Address" , "City" , "State" , "Zip Code"]
    #Collect all the data using the helper 
    values = [get_input(field) for field in fields]
    #Create contact object and add it to the book
    # The *values unpacs the list into the 8 arguments the class needs
    new_contact = contact(*values)
    address_book.add_contact(new_contact)


def edit_contact(addressbook):
    try:
        fullname = input("Enter the full name of the contact to edit: ")
        #split "john Doe" into ["john" , "Doe"]
        parts = fullname.split()
        if len(parts) < 2:
            print("Error: Please enter both First and Last Name")
            return
        
        firstname , lastname = parts[0] , parts[1]
        contact = addressbook.get_contact(firstname , lastname)

        if not contact:
            print("Contact not found!")
            return 
    
        print("\n. Phone | 2. Email | 3. Address | 4. City | 5. State | 6.Zip")
        choice = input("Which field do you want to edit ?")

        match choice:
            case "1":
                contact.phonenumber = input("Enter new phone number : ")
            case "2":
                contact.email = input("Enter new email : ")
            case "3":
                contact.address  = input("Enter new Address : ")
            case "4":
                contact.city = input("Enter New City: ")
            case "5":
                contact.state = input("Enter new State : ")
            case "6":
                contact.zip_code = input("Enter New Zip Code : ")
            case _:
                print("Invalid choice.")
        
        print("Contact updated Successfully!")
        
    except Exception as e:
        print(f"An error Occured: {e}")



def search_by_location_flow(manager):
    print(" 1.Search by city | 2. search by state")
    choice = input("Choose search options : ")

    searchtype = "city" if choice == "1" else "state"
    location = input(f"Enter the {searchtype} name ")

    result = manager.search_across_allbooks(location , searchtype)

    if not result:
        print(f"No contacts found in {location}")
    else:
        print(f"Found {len(result)} contact in {location}")
        for person in result:
            print(person)


def view_by_location_flow(manager):
    #Update the maps first to ensure we have latest data uc9

    manager.update_location_maps()

    print("\n 1. View by City | 2. View by State")
    choice = input("Select view type: ")

    if choice == "1":
        data = manager.get_persons_by_city()
        label = "city"
    else:
        data = manager.get_persons_by_state()
        label = "state"

    if not data:
        print("No data available.")

    for location , people in data.items():
        print(f"\n--- {label}: {location.upper()} ({len(people)} persons)---")
        for p in people:
            print(f"- {p.firstname} {p.lastname} ({p.phonenumber})")


def view_location_counts_flow(manager):
    city_counts, state_counts = manager.get_count_bylocation()

    print("\n---- CONTACT COUNT BY CITY ---")
    if not city_counts:
        print("No data available.")
    for city , count in city_counts.items():
        print(f"{city.capitalize()}:{count}")  

    print("\n --- CONTACT COUNT BY STATE---")
    if not state_counts:
        print("No data available.")

    for state , count in state_counts.items():
        print(f"{state.upper()}:{count}")



def sort_contacts_flow(address_book):
    print("\n Sort by : 1.Name | 2. City | 3.State | 4.Zip")

    choice = input("Select sorting preference: ")

    strategies = {
        "1": sortbyName(),
        "2": sortbycity(),
        "3": sortbystate(),
        "4": sortbyzip()
    }

    strategy = strategies.get(choice)

    if strategy : 
        address_book.perform_sort(strategy)
        address_book.display_contacts()
    else:
        print("Invalid choice. Returning to menu.")