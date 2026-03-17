from abc import ABC, abstractmethod
import csv
import os
from models.contact import contact

class FileIoStrategy(ABC):
    @abstractmethod
    def save_data(self, filename, address_books):
        pass

    @abstractmethod
    def load_data(self, filename, manager):
        pass

class TextFileIoStrategy(FileIoStrategy):
    def save_data(self, filename, address_books):
        """Converts AddressBook objects into a flat text file"""
        try:
            with open(filename, mode="w", encoding="utf-8") as file:
                # 1. Loop through the dictionary: ab_name is Key, address_book is Value
                for ab_name, address_book in address_books.items():
                    # FIX: Use 'address_book' (the instance), NOT 'address_books' (the dict)
                    for c in address_book.get_all_contacts():
                        # 2. Create a single line string separated by "|"
                        line = f"{ab_name}|{c.firstname}|{c.lastname}|{c.phonenumber}|{c.email}|{c.address}|{c.city}|{c.state}|{c.zip_code}\n"
                        file.write(line)
            print(f"Successfully saved all books to {filename}")
        except IOError as e:
            print(f"Error saving file: {e}")
    
    def load_data(self, filename, manager):
        manager.clear_all_data()
        
        """Read the text file and recreates the object in memory."""
        if not os.path.exists(filename):
            print("File not found.")
            return
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                for line in file:
                    # 1. Split the line back into individual pieces of data
                    parts = line.strip().split("|")
                    if len(parts) == 9:
                        ab_name, fn, ln, ph, em, ad, ct, st, zp = parts

                        # 2. Check if the Address Book exists in the manager
                        if ab_name not in manager.list_allbooks():
                            # Lazy import to avoid circular dependency
                            from Services.addressbook import AddressBook
                            manager.add_addressbook(ab_name, AddressBook())
                        
                        # 3. Create the contact object and add it to the correct book
                        new_contact = contact(fn, ln, ph, em, ad, ct, st, zp)
                        manager.get_addressbook(ab_name).add_contact(new_contact)
            print(f"Successfully loaded data from {filename}")
        except Exception as e:
            print(f"An error occurred while loading: {e}")


class CsvFileIoStrategy(FileIoStrategy):
    def __init__(self):
        # Define the headers (columns) for the CSV file
        self.headers = [
            "addressbook_name", "firstname", "lastname", 
            "phone", "email", "address", "city", "state", "zip"
        ]

    def save_data(self, filename, address_books):
        """Saves all address books into a single CSV file"""
        try:
            with open(filename, mode="w", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader() # Write the top row (headers)

                for ab_name, book in address_books.items():
                    for c in book.get_all_contacts():
                        writer.writerow({
                            "addressbook_name": ab_name,
                            "firstname": c.firstname,
                            "lastname": c.lastname,
                            "phone": c.phonenumber,
                            "email": c.email,
                            "address": c.address,
                            "city": c.city,
                            "state": c.state,
                            "zip": c.zip_code
                        })
            print(f"Successfully saved data to CSV: {filename}")
        except IOError as e:
            print(f"Error saving CSV: {e}")

    def load_data(self, filename, manager):
        """Reads CSV and rebuilds the objects in memory"""
        if not os.path.exists(filename):
            print("CSV file not found.")
            return

        manager.clear_all_data() # Ensure fresh start
        try:
            with open(filename, mode="r", encoding="utf-8", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    ab_name = row["addressbook_name"]

                    # Ensure the Address Book exists
                    if ab_name not in manager.list_allbooks():
                        from Services.addressbook import AddressBook
                        manager.add_addressbook(ab_name, AddressBook())

                    # Reconstruct the contact object
                    new_contact = contact(
                        row["firstname"], row["lastname"], row["phone"],
                        row["email"], row["address"], row["city"],
                        row["state"], row["zip"]
                    )
                    manager.get_addressbook(ab_name).add_contact(new_contact)
            print(f"Successfully loaded data from CSV: {filename}")
        except Exception as e:
            print(f"Error loading CSV: {e}")