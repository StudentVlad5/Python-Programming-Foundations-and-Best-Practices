from termcolor import colored
from modules.AddressBook_m.record_m import Record
from modules.AddressBook_m.phone_m import Phone
from modules.AddressBook_m.birthday_m import Birthday
from modules.AddressBook_m.email_m import Email
from modules.AddressBook_m.address_m import Address
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
            email = args[3] if len(args) > 3 else None
            address = args[4] if len(args) > 4 else None
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
                if Email(email):
                    record.add_email(email)
            except ValueError as e:
                print(colored(f"Error: {e}", 'red'))
            try:
                if Birthday(birthday):
                    record.add_birthday(birthday)
            except ValueError as e:
                print(colored(f"Error: {e}", 'red'))
            try:
                if Address(address):
                    record.add_address(address)
            except ValueError as e:
                print(colored(f"Error: {e}", 'red'))

            book.add_record(record)
            save_data(book.data, filename)
            print(colored(f"Added {name} with phone {phone} with email {email} with address {address} and birthday {birthday}.", 'green'))

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

# Function to handle command "add-email"
def add_email(book, args):
    if not args or len(args) < 1:
        print(colored("Missing name", 'red'))
    else:
        try:
            name = args[0]
            email = args[1] if len(args) > 1 else None
        except Exception as e:
            print(colored(f"Error: {e}", 'red'))
            return 

        record = book.find(name)
        if record:
            if email:
                try:
                    if record.add_email(email):
                        book.add_record(record)
                        save_data(book.data, filename)
                        print(colored(f"Added {name} with email {email}.", 'green'))
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

# Function to handle command "add-address"
def add_address(book, args):
    if not args or len(args) < 1:
        print(colored("Missing name", 'red'))
    else:
        try:
            name = args[0]
            address = args[1] if len(args) > 1 else None
        except Exception as e:
            print(colored(f"Error: {e}", 'red'))
            return 

        record = book.find(name)
        if record:
            if address:
                try:
                    if record.add_address(address):
                        book.add_record(record)
                        save_data(book.data, filename)
                        print(colored(f"Added {name} with address {address}.", 'green'))
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

# Function to handle command "email"
def show_email(book, args):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)
        if record:
            if len(record.emails) > 0:
                print(colored(f"Emails for {name}: {', '.join(str(em.value) for em in record.emails)}", 'green'))
            else: 
                print(colored(f"Contact {name}: doesn't have email", 'red'))
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

# Function to handle command "address"
def show_address(book, args):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)
        if record:
            if record.address:
                print(colored(f"Address for {name}: {record.show_address()}", 'green'))
            else: 
                print(colored(f"Contact {name}: doesn't have address", 'red'))
        else:
            print(colored(f"Error: {name} not found.", 'red'))

# Function to handle command "delete"
def delete_contact(book, args):
    if len(args) == 1:
        name = args[0]
        if book.delete(name):
            print(f"Deleted contact {name}.")
            save_data(book.data,filename)

# delete phone (name)
        elif command == "delete-phone":
            if len(args) == 2:
                name, phone = args[0], args[1]
                record = book.find(name)
                if record:
                    if record.delete_phone(phone):
                        print(f"Deleted phone {phone} for {name}.")
                        save_data(book.data)  
                else:
                    print(f"Error: {name} not found.")
        # delete birthday (name)
        elif command == "delete-birthday":
            if len(args) == 1:
                name = args[0]
                record = book.find(name)
                if record:
                    record.delete_birthday()
                    print(f"Deleted birthday for {name}.")
                    save_data(book.data) 
                else:
                    print(f"Error: {name} not found.")
        # edit phone (name old-phone(10 numbers) new-phone(10 numbers))
        elif command == "edit-phone":
            if len(args) >= 3:
                name, old_phone, new_phone = args[0], args[1], args[2]
                record = book.find(name)
                if record:
                    record.edit_phone(old_phone, new_phone)
                    print(f"Changed phone for {name}.")
                    save_data(book.data)
                else:
                    print(colored(f"Error: {name} not found.", 'red)'))
            else:
                print(colored(f"Please add correct name and two phone numbers", 'red'))
        # edit birthday (name new-birthday(dd.mm.yyyy))
        elif command == "edit-birthday":
            if len(args) == 2:
                name, new_birthday = args[0], args[1]
                record = book.find(name)
                if record:
                    try: 
                        record.edit_birthday(new_birthday)
                        print(colored(f"Edited birthday for {name}.", 'green'))
                        save_data(book.data)
                    except Exception as e:
                         print(colored(f"Error: {e}", 'red'))
                else:
                    print(colored(f"Error: {name} not found.", 'red'))
        # see  birthdays [today + 7 days]
        # edit birthday (fix-date(dd.mm.yyyy)) [fix-date + 7 days]
        elif command == "birthdays":
            if args:
                upcoming = book.birthdays(args[0])
            else:
                upcoming = book.birthdays() 
            if upcoming:
                print(colored("Upcoming birthdays:", 'green'))
                for it in upcoming:
                    print(f"{colored(it['name'], 'magenta')} {colored("on", 'yellow')} {colored(it['congratulation_date'], 'magenta')}")
            else:
                print(colored(f"No upcoming birthdays in the next 7 days.", 'magenta'))
        # see all contact's birthdays 
        elif command == "birthdays-all":
            print(colored("All birthdays:", 'green'))
            for record in book.data.values():
                print(colored(f"{record.name.value}: {record.show_birthday()}", 'magenta'))
        # message about invalid command