from abc import ABC , abstractmethod

class sortingStragegy(ABC):
    @abstractmethod
    def sort(self ,contact):
        pass


class sortbyName(sortingStragegy):
        
        def sort(self , contacts):
            contacts.sort(
            key=lambda contact: (
                contact.firstname.casefold(),
                contact.lastname.casefold(),
            )
        )
