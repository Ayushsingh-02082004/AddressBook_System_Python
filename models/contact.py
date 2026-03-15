class contact:
    def __init__(self , firstname , lastname , phonenumber , email , address , city , state , zip_code ):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __eq__(self, other):

        #is instance checks the other here is of the samy object type as contact 
        if not isinstance(other , contact):
            return False
        #Duplicate check is done on Person Name
        return (self.firstname.casefold() == other.firstname.casefold() and 
                self.lastname.casefold() == other.lastname.casefold())

    def __str__(self):
        #this function returns the formatted string to the caller like print function 
        return (
            f"contact details:\n"
            f"Name: {self.firstname} {self.lastname} \n"
            f"PhoneNumber : {self.phonenumber}\n"
            f"Email: {self.email}\n"
            f"Address: {self.address} , {self.city} , {self.state}-{self.zip_code}\n"
            f"-----------------------------------------------------"
        )
