

def welcome_screen():

    banner = r"""
    /$$$$$$        /$$       /$$                                              /$$$$$$$                      /$$      
   /$$__  $$      | $$      | $$                                             | $$__  $$                    | $$      
  | $$  \ $$  /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$$      | $$  \ $$  /$$$$$$   /$$$$$$ | $$   /$$
  | $$$$$$$$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$_____//$$_____/      | $$$$$$$  /$$__  $$ /$$__  $$| $$  /$$/
  | $$__  $$| $$  | $$| $$  | $$| $$  \__/| $$$$$$$$|  $$$$$$|  $$$$$$       | $$__  $$| $$  \ $$| $$  \ $$| $$$$$$/ 
  | $$  | $$| $$  | $$| $$  | $$| $$      | $$_____/ \____  $$\____  $$      | $$  \ $$| $$  | $$| $$  | $$| $$_  $$ 
  | $$  | $$|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$$ /$$$$$$$//$$$$$$$/      | $$$$$$$/|  $$$$$$/|  $$$$$$/| $$ \  $$
  |__/  |__/ \_______/ \_______/|__/       \_______/|_______/|_______/       |_______/  \______/  \______/ |__/  \__/

                              ADDRESS BOOK
    """
    
    

    print(banner)
    print("Welcome to Your Adddress Book System")
    print("--------------------------------------")

# def main_menue():
#     print("\n1. Add contact")
#     print("2. Display contact")
#     print("3. Edit Contact")
#     print("4. Delete Contact")
#     print("5. Exit")

def main_menue():
    print("\n1.Add new Address Book")
    print("2. Open Existing Address Book")
    print("3. List All Address Books")
    print("4. Search by location in Address Book")
    print("5. View All by City/State")
    print("6. view count of person in city/state ")
    print("7. Exit")


def address_book_menu():
    """Level 2: Operations inside a SPECIFIC Address Book."""
    welcome_screen()
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Sort Contacts by Name")
    print("6. Go Back (Main Menu)")