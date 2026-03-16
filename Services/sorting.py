from abc import ABC , abstractmethod

class sortingStrategy(ABC):
    @abstractmethod
    def sort(self ,contact):
        pass


class sortbyName(sortingStrategy):
        
        def sort(self , contacts):
            contacts.sort(
            key=lambda contact: (
                contact.firstname.casefold(),
                contact.lastname.casefold(),
            )
        )
            
class sortbycity(sortingStrategy):
     def sort(self , contact): contact.sort(key = lambda contact: contact.city.casefold())

class sortbystate(sortingStrategy):
     def sort(self, contact):
          contact.sort(key = lambda contact: contact.state.casefold())

class sortbyzip(sortingStrategy):
     def sort(self , contact):
          contact.sort(key = lambda contact: contact.zip_code.casefold())
