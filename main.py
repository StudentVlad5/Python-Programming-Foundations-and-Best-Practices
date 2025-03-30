from termcolor import colored
from services.file_manager import load_data, save_data
from services.data_parse_input import parse_input
from modules.AddressBook_m.addressbook_m import AddressBook
from modules.Notes_m.note_m import Note
from services.address_book_manager import hello, add_contact, add_phone, add_birthday, show_all_contacts, show_phone, show_birthday, delete_contact
from services.note_manager import add_note, show_all_notes, add_tag, delete_tag, show_message, edit_message, delete_note, search_tag, search_message
from modules.Common_m.CONSTANT import filename, filenameNotes


def main():
    book = AddressBook()
    notes = Note()

    loaded_contacts = load_data(book, filename)
    book.data.update(loaded_contacts)
    loaded_notes = load_data(notes, filenameNotes)
    notes.data.update(loaded_notes)

    print(colored("Welcome to the assistant bot!", 'cyan'))

    command_dict = {
        "hello": hello,
    #  addressBook commands
        "add": lambda args: add_contact(book, args),
        "add-phone": lambda args: add_phone(book, args),
        "add-birthday": lambda args: add_birthday(book, args),
        "all": lambda _: show_all_contacts(book),
        "phone": lambda args: show_phone(book, args),
        "birthday": lambda args: show_birthday(book, args),
        "delete": lambda args: delete_contact(book, args),
    #  notes commands
        "add-note": lambda args: add_note(notes, args),
        "all-note": lambda _: show_all_notes(notes),
        "add-tag": lambda args: add_tag(notes, args),
        "delete-tag": lambda args: delete_tag(notes, args),
        "show-message": lambda args: show_message(notes, args),
        "edit-message": lambda args: edit_message(notes, args),
        "delete-note": lambda args: delete_note(notes, args),
        "search-tag": lambda args: search_tag(notes, args),
        "search-message": lambda args: search_message(notes, args)
    }

    while True:
        user_input = input(colored("Enter a command: ", 'cyan'))
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book.data, filename)
            save_data(notes.data, filenameNotes)
            print(colored("Good bye!", 'blue'))
            break
        elif command in command_dict:
            command_dict[command](args)
        else:
            print(colored("Invalid command.", 'red'))

if __name__ == "__main__":
    main()
