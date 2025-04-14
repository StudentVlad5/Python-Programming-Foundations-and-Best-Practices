from main_project.services.errors_wrap import input_error
from collections import UserDict
from datetime import datetime, timedelta
from rich.text import Text
from rich.console import Console

console = Console()

class AddressBook(UserDict):
    """
    A class representing an address book, inheriting from UserDict.

    The AddressBook class manages a collection of contact records, allowing
    for adding, finding, deleting, and retrieving upcoming birthdays of contacts.

    Attributes:
        data (dict): A dictionary that stores records, where the key is the contact's name and the value is the corresponding Record object.

    Methods:
        add_record(record): Adds a new record to the address book. If the record has an invalid name (None), a message is printed to the console.

        find(name): Searches for a contact record by name. Returns the corresponding Record object if found, otherwise returns None.

        delete(name): Deletes the contact record identified by the given name. Returns 1 on successful deletion, or 0 if the record does not exist.
        
        birthdays(search_period=7): Retrieves a list of upcoming birthdays within the specified search period (in days). Returns a sorted 
         list of birthday reminders containing the name and congratulation date.
        __str__(): Returns a string representation of all records in the address book.

    Usage:
        address_book = AddressBook()
        address_book.add_record(record)
        contact = address_book.find("John Doe")
        address_book.delete("Jane Smith")
        upcoming_birthdays = address_book.birthdays(30)
        print(address_book)
    """
    def add_record(self, record):
        if record.name is None:
            console.print(Text("Cannot add a record with an invalid name.", style="red"))
            return
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        return None
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return 1
        else:
            console.print(Text("Error: Record for ", style="yellow") + Text(name, style="red") + Text(" not found.", style="yellow"))
            return 0

    @input_error
    def birthdays(self, search_period=7):
        today = datetime.today().date()
        upcoming_birthdays = []

        for user in self.data.values():
            if user.birthday is None:
                continue 

            birthday = user.birthday.value
            birthday_date = birthday.date()


            for delta in range(int(search_period) + 1):
                check_date = today + timedelta(days=delta)

                if birthday_date.month == check_date.month and birthday_date.day == check_date.day:
                    upcoming_birthdays.append({
                        "name": user.name.value,
                        "congratulation_date": birthday_date.strftime("%d.%m.%Y")
                    })
                    break  

        sorted_upcoming_birthdays = sorted(upcoming_birthdays, key=lambda x: datetime.strptime(x["congratulation_date"], "%d.%m.%Y"))
        
        return sorted_upcoming_birthdays
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
