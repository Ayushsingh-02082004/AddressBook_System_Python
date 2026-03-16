class AdressBookManager:

    def __init__(self):
        #Dictionary to store
        self.__address_books = {}

        #UC9: New dictionaries for grouping by location
        self.__city_topersons = {}
        self.__state_topersons = {}

    def update_location_maps(self):
        """Rebuilds the city and state dictonaries from all address books"""

        self.__city_topersons.clear()
        self.__state_topersons.clear()

        for book in self.__address_books.values():
            for contact in book.get_all_contacts():

                # Group by city

                city = contact.city.casefold()
                if city not in self.__city_topersons:
                    self.__city_topersons[city] = []
                self.__city_topersons[city].append(contact)

                # Group by State
                state = contact.state.casefold()
                if state not in self.__state_topersons:
                    self.__state_topersons[state] = []
                self.__state_topersons[state].append(contact)

    def get_persons_by_city(self):
        return self.__city_topersons
    
    def get_persons_by_state(self):
        return self.__state_topersons

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
    
    def search_across_allbooks(self , location , searchtype):
        result = []
        #loop through addressbook object in dictionary 
        for book_name , book_object in self.__address_books.items():  #book object is the addressbook object and items gives data in key
            matches = book_object.get_contact_byLocation(location , searchtype)
            result.extend(matches)  #add the found matches in the master list
        return result
    

    def get_count_bylocation(self):
        """"Returns a summary of counts for all cities and states"""

        # Ensure maps are fresh
        self.update_location_maps()

        city_counts = {city: len(people) for city , people in self.__city_topersons.items()}
        state_counts = {state: len(people) for state , people in self.__state_topersons.items()}

        return city_counts , state_counts
    
    def perform_file_io(self , strategy , filename , mode):
        """mode : 'save' or 'load' """

        if mode == "save" : 
            # pass our dictionary of books to the strategy 
            strategy.save_data(filename , self.__address_books)
        elif mode == "load":
            # We pass 'self' (the manager) so the strategy can add books/contacts
            strategy.load_data(filename, self)
    

    def clear_all_data(self):
        self.__address_books.clear()
        # Also clear your location maps if you use UC9
        self.__city_topersons.clear()
        self.__city_topersons.clear()
        print("Memory cleared for fresh load.")
