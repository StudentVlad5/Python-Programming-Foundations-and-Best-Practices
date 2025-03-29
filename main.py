from termcolor import colored
from services.file_manager import load_data, save_data
from services.data_parse_input import parse_input
from modules.AddressBook_m.addressbook_m import AddressBook
from modules.AddressBook_m.record_m import Record
from modules.AddressBook_m.phone_m import Phone
from modules.AddressBook_m.birthday_m import Birthday

filename = "addressbook.pkl"
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
