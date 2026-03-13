class AddressBook:
    def __init__(self):

        #Encapsulation: private list to store contacts
        self.__contacts = []

    def add_contact(self , contact):
        self.__contacts.append(contact)
        print("\nContact added successfully!")

    def get_contact(self , firstname , lastname):
        for contact in self.__contacts:
            #  .casefold () makes teh search case-insensitive(ayush==Ayush)
            if(contact.firstname.casefold() == firstname.casefold() and contact.lastname.casefold() == lastname.casefold()):
                return contact
        return None
    
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