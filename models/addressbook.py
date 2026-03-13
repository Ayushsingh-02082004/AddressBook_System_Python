class AddressBook:
    def __init__(self):

        #Encapsulation: private list to store contacts
        self.__contacts = []

    def add_contact(self , contact):
        self.__contacts.append(contact)
        print("\nContact added successfully!")

    def display_contacts(self):
        if not self.__contacts:
            print("\nAddress book is empty.")
            return
        
        print("\n------All Contacts--------------")
        for contact in self.__contacts:
            print(contact)
            print("-" * 30)