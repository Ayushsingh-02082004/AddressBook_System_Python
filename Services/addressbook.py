class AddressBook:
    def __init__(self):

        #Encapsulation: private list to store contacts
        self.__contacts = list()

    def add_contact(self , contact):

        #uc7 python is equivalent of java sterem it checks that if any contact matches new contact
        #this uses the __eq__ method we just wrote above
        if any(existingcontact == contact for existingcontact in self.__contacts):
            print(f"Error: contact {contact.firstname } {contact.lastname} already exists.")
            return False
        self.__contacts.append(contact)
        print("\nContact added successfully!")
        return True

    def get_contact(self , firstname , lastname):
        for contact in self.__contacts:
            #  .casefold () makes teh search case-insensitive(ayush==Ayush)
            if(contact.firstname.casefold() == firstname.casefold() and contact.lastname.casefold() == lastname.casefold()):
                return contact
        return None
    
    def get_all_contacts(self):
        return self.__contacts
    
    def delete_contact(self , firstname  , lastname ):
        contact_toDelete = self.get_contact(firstname , lastname)

        if contact_toDelete :
            self.__contacts.remove(contact_toDelete)
            return True
        return False

    def display_contacts(self):
        if not self.__contacts:
            print("\nAddress book is empty.")
            return
        
        print("\n------All Contacts--------------")
        for contact in self.__contacts:
            print(contact)
            print("-" * 30)

    def get_contact_byLocation(self , location , search_type):
        #serchtype is city or state
        #location is the name of the city or state 
        if search_type == "city":
            return [c for c in self.__contacts if c.city.casefold() == location.casefold()]
        elif search_type == "state":
            return [c for c in self.__contacts if c.state.casefold() == location.casefold()]
        return []