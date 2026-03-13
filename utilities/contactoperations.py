
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