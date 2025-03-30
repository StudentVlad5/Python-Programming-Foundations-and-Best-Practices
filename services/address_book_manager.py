from termcolor import colored
from modules.AddressBook_m.record_m import Record
from modules.AddressBook_m.phone_m import Phone
from modules.AddressBook_m.birthday_m import Birthday
from services.file_manager import save_data
from modules.Common_m.CONSTANT import filename

# Function to handle command "hello"
def hello():
    print(colored("How can I help you?", 'blue'))

# Function to handle command "add"
def add_contact(book, args):
    if not args or len(args) < 1:
        print(colored(f"Missing name", 'red'))
    else:
        try:
            name = args[0]
            phone = args[1] if len(args) > 1 else None
            birthday = args[2] if len(args) > 2 else None
        except Exception as e:
            print(colored(f"Error: {e}", 'red'))
            return

        record = book.find(name)
        if record:
            print(colored(f"You already have contact {name} in your book", 'red'))
        else:
            record = Record(name)
            try:
                if Phone(phone):
                    record.add_phone(phone)
            except ValueError as e:
                print(colored(f"Error: {e}", 'red'))
            try:
                if Birthday(birthday):
                    record.add_birthday(birthday)
            except ValueError as e:
                print(colored(f"Error: {e}", 'red'))

            book.add_record(record)
            save_data(book.data, filename)
            print(colored(f"Added {name} with phone {phone} and birthday {birthday}.", 'green'))

# Function to handle command "add-phone"
def add_phone(book, args):
    if not args or len(args) < 1:
        print(colored("Missing name", 'red'))
    else:
        try:
            name = args[0]
            phone = args[1] if len(args) > 1 else None
        except Exception as e:
            print(colored(f"Error: {e}", 'red'))
            return 

        record = book.find(name)
        if record:
            if phone:
                try:
                    if record.add_phone(phone):
                        book.add_record(record)
                        save_data(book.data, filename)
                        print(colored(f"Added {name} with phone {phone}.", 'green'))
                except Exception as e:
                    print(colored(f"Error: {e}", 'red'))

# Function to handle command "add-birthday"
def add_birthday(book, args):
    if not args or len(args) < 1:
        print(colored("Missing name", 'red'))
    else:
        try:
            name = args[0]
            birthday = args[1] if len(args) > 1 else None
        except Exception as e:
            print(colored(f"Error: {e}", 'red'))
            return 

        record = book.find(name)
        if record:
            if birthday:
                try:
                    if record.add_birthday(birthday):
                        book.add_record(record)
                        save_data(book.data, filename)
                        print(colored(f"Added {name} with birthday {birthday}.", 'green'))
                except Exception as e:
                    print(colored(f"Error: {e}", 'red'))

# Function to handle command "all"
def show_all_contacts(book):
    print(book)

# Function to handle command "phone"
def show_phone(book, args):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)
        if record:
            if len(record.phones) > 0:
                print(colored(f"Phones for {name}: {', '.join(str(p.value) for p in record.phones)}", 'green'))
            else: 
                print(colored(f"Contact {name}: doesn't have phones", 'red'))
        else:
            print(colored(f"Error: {name} not found.", 'red'))

# Function to handle command "birthday"
def show_birthday(book, args):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)
        if record:
            if record.birthday:
                print(colored(f"Birthday for {name}: {record.show_birthday()}", 'green'))
            else: 
                print(colored(f"Contact {name}: doesn't have birthday date", 'red'))
        else:
            print(colored(f"Error: {name} not found.", 'red'))

# Function to handle command "delete"
def delete_contact(book, args):
    if len(args) == 1:
        name = args[0]
        if book.delete(name):
            print(f"Deleted contact {name}.")
            save_data(book.data,filename)