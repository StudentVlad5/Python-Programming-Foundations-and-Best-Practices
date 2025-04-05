from termcolor import colored
from services.file_manager import load_data, save_data
from services.data_parse_input import parse_input
from services.prompt_toolkit import handle_user_input
from modules.AddressBook_m.addressbook_m import AddressBook
from modules.Notes_m.note_m import Note
from modules.Common_m.CONSTANT import filename, filenameNotes
from modules.Common_m.dictionary import command_d
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from modules.Common_m.dictionary import command_list

command_completer = WordCompleter(command_list, ignore_case=True)
def main():
    book = AddressBook()
    notes = Note()
    command_dict = command_d(book, notes)

    loaded_contacts = load_data(book, filename)
    book.data.update(loaded_contacts)
    loaded_notes = load_data(notes, filenameNotes)
    notes.data.update(loaded_notes)

    print(colored("Welcome to the assistant bot!", 'cyan'))

    while True:
        user_input = prompt("Enter a command: ", completer=command_completer)
        handle_user_input(user_input)
        if user_input is None:
            continue
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
