class AdressBookManager:

    def __init__(self):
        #Dictionary to store
        self.__address_books = {}

    def add_addressbook(self , name , book_object):
        if name in self.__address_books:
            raise ValueError(f"Address Book {name} already exists.")
        self.__address_books[name] = book_object

    
    def get_addressbook(self , name):
        if name not in self.__address_books:
            raise KeyError(f"Adress Book '{name}' not found.")
        return self.__address_books[name]
    
    def list_allbooks(self):
        return list(self.__address_books.keys())