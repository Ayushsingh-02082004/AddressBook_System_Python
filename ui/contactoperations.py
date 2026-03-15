from ui.helper import get_input
from models.contact import contact
from Services.addressbook import AddressBook



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