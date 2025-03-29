from collections import UserDict
import re
from datetime import datetime, timedelta
from termcolor import colored
from services.file_manager import load_data, save_data
from services.data_parse_input import parse_input
from services.errors_wrap import input_error

filename = "addressbook.pkl"

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError(f"{colored("Invalid phone number format: ", 'yellow')}{colored(value, 'red')}")
        super().__init__(value)

    @staticmethod
    def validate_phone(value):
        return bool(re.match(r"^\d{10}$", value))

class Birthday(Field):
    def __init__(self, value):
        if not self.validate_birthday(value):
            raise ValueError(
                f"{colored('Invalid date format. Use DD.MM.YYYY. You provided:', 'yellow')} {colored(value, 'red')}"
            )
        self.value = datetime.strptime(value, "%d.%m.%Y")

    @staticmethod
    def validate_birthday(value):
        return bool(re.match(r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$", value))

class Record:
    def __init__(self, name):
        try:
            self.name = Name(name)
        except ValueError as e:
            print(f"Error: {e}")
            self.name = None
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        try:
            valid_phone = Phone(phone) 
            self.phones.append(valid_phone)
            return 1
        except ValueError as e:
            print(f"Error: {e}")
            return 0

    def delete_phone(self, phone):
        try: 
            self.phones = [p for p in self.phones if p.value != phone]
            return 1
        except ValueError as e:
            print(f"Error: {e}")
            return 0

    def edit_phone(self, old_phone, new_phone):
        try:
            for p in self.phones:
                if p.value == old_phone:
                    self.add_phone(new_phone)
                    self.delete_phone(old_phone)
                    return 1
            raise ValueError(f"Phone number {old_phone} not found.")
        except ValueError as e:
            print(f"Error: {e}")
            return 0
    @input_error
    def add_birthday(self, birthday):
        if self.birthday is not None:
            print(f"Birthday for {self.name.value} already exists.")
            return 0
        try:
            self.birthday = Birthday(birthday)
            return 1
        except ValueError as e:
            print(f"Error: {e}")
            return 0
    
    def delete_birthday(self):
        self.birthday = None
    
    def edit_birthday(self, new_birthday):
        try:
            self.birthday = Birthday(new_birthday)
            return 1
        except ValueError as e:
            print(f"Error: {e}")
            return 0
    @input_error
    def show_birthday(self):
        if self.birthday is None:
            return f"{colored("Birthday for",'yellow')} {colored(self.name.value, 'red')}{colored(" is not set.", 'yellow')}"
        return self.birthday.value.strftime("%d.%m.%Y")

    def __str__(self):
        birthday_str = self.birthday.value.date().strftime("%d.%m.%Y") if self.birthday else "unknown date"
        phones_str = "; ".join([str(p.value) for p in self.phones]) if self.phones else "no phones"
        return f"{colored("Contact name: ",'light_cyan')} {colored(self.name.value.ljust(10), 'green')}{colored("birthday: ", 'light_cyan')}  {colored(birthday_str.ljust(15), 'green')}{colored(" phones: ",'light_cyan')} {colored(phones_str, 'green')}"

class AddressBook(UserDict):
    def add_record(self, record):
        if record.name is None:
            print(colored(f"Cannot add a record with an invalid name.", 'red'))
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
            print(f"{colored("Error: Record for",'yellow')} {colored(name, 'red')} {colored("not found.", 'yellow')}")
            return 0
    @input_error
    def birthdays(self, check_day=None):
        try: 
            check_date = datetime.strptime(check_day, "%d.%m.%Y")
        except ValueError:
            print(colored(f"The invalid data of the date {check_day}", 'red'))
            check_date = None
        today = check_date if check_date else datetime.today().date()

        search_period = 7
        upcoming_birthdays = []

        for user in self.data.values():
            if user.birthday is None:
                continue 

            birthday = user.birthday.value
            birthday_date = birthday.date()

            for delta in range(search_period + 1):
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

def main():

    book = AddressBook()
    loaded_contacts = load_data(book, filename)
    book.data.update(loaded_contacts)

    print(colored("Welcome to the assistant bot!", 'cyan'))
    while True:
        user_input = input(colored("Enter a command: ", 'cyan'))
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book.data)
            print(colored("Good bye!", 'blue'))
            break
        # just say hello
        elif command == "hello":
            print(colored("How can I help you?", 'blue'))
        # add new contact (name phone(10 numbers) birthday(dd.mm.yyyy))
        elif command == "add":
            if not args or len(args) < 1:
                print(colored(f"Miss name", 'red'))
            else:
                try:
                    name = args[0]
                    phone = args[1] if len(args) > 1 else None
                    birthday = args[2] if len(args) > 2 else None
                except  Exception as e:
                    print(colored(f"Error: {e}", 'red'))

                record = book.find(name)
                if record:
                    print(colored(f"You already have contact {name} in your book", 'red'))
                else:
                    record = Record(name)
                    try:
                        if Phone(phone):
                            record.add_phone(phone)
                    except ValueError  as e:
                        print(colored(f"Error: {e}", 'red'))
                    try:
                        if Birthday(birthday):
                            record.add_birthday(birthday)
                    except ValueError as e:
                         print(colored(f"Error: {e}", 'red'))

                    book.add_record(record)
                    save_data(book.data)
                    print(colored(f"Added {name} with phone {phone} and with birthday {birthday}.",'green'))
        # add phone to contact (name phone(10 numbers))
        elif command == "add-phone":
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
                                    save_data(book.data)
                                    print(colored(f"Added {name} with phone {phone}.", 'green'))
                            except Exception as e:
                                print(colored(f"Error: {e}", 'red'))
        # add birthday to contact (name birthday(dd.mm.yyyy))
        elif command == "add-birthday":
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
                                    save_data(book.data)
                                    print(colored(f"Added {name} with birthday {birthday}.", 'green'))
                            except Exception as e:
                                print(colored(f"Error: {e}", 'red'))
        # see all list of contacts
        elif command == "all":
            print(book)
        # see phone of contact (name)
        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                record = book.find(name)
                if record:
                    if len(record.phones) > 0:
                        print(colored(f"Phones for {name}: {', '.join(str(p.value) for p in record.phones)}", 'green'))
                    else: 
                        print(colored(f"Contact {name}:doesn't have phones",'red'))
                else:
                    print(colored(f"Error: {name} not found.", 'red'))
        # see birthday of contact (name)
        elif command == "birthday":
            if len(args) == 1:
                name = args[0]
                record = book.find(name)
                if record:
                    if record.birthday:
                        print(colored(f"Birthday for {name}: {record.show_birthday()}", 'green'))
                    else: 
                        print(colored(f"Contact {name}:doesn't have birthday date",'red'))
                else:
                    print(colored(f"Error: {name} not found.", 'red'))
        # delete contact (name)
        elif command == "delete":
            if len(args) == 1:
                name = args[0]
                if book.delete(name):
                    print(f"Deleted contact {name}.")
                    save_data(book.data)
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
        else:
            print(colored("Invalid command.", 'red'))
            
if __name__ == "__main__":
    main()
