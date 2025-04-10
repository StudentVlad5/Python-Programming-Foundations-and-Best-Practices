from main_project.services.file_manager import load_data, save_data
from main_project.services.data_parse_input import parse_input
from main_project.services.prompt_toolkit import handle_user_input
from main_project.modules.AddressBook_m.addressbook_m import AddressBook
from main_project.modules.Notes_m.note_m import Note
from main_project.modules.Common_m.dictionary import command_d
from main_project.modules.Common_m.CONSTANT import filename, filenameNotes
from main_project.modules.Common_m.dictionary import command_list
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from rich.text import Text
from rich.panel import Panel
from rich.console import Console

console = Console()
welcome_message = Text("[bold cyan]Welcome to the assistant bot![/bold cyan]")
goodbye_message = Text("[bold blue]Good bye![/bold blue]")
invalid_command_message = Text("[bold red]Invalid command.[/bold red]")

command_completer = WordCompleter(command_list, ignore_case=True)

def main():
    book = AddressBook()
    notes = Note()
    command_dict = command_d(book, notes)

    loaded_contacts = load_data(book, filename)
    sorted_loaded_contacts= sorted(loaded_contacts.items(), key=lambda x: x[0])
    book.data.update(sorted_loaded_contacts)
    loaded_notes = load_data(notes, filenameNotes)
    notes.data.update(loaded_notes)

    console.print(Panel(f"🤖 {welcome_message}", style="cyan", expand=True))

    while True:
        user_input = prompt("Enter a command: ", completer=command_completer)
        handle_user_input(user_input)
        if user_input is None:
            continue
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book.data, filename)
            save_data(notes.data, filenameNotes)
            console.print(Panel(f"👋 {goodbye_message}", style="blue", expand=True))
            break
        elif command in command_dict:
            command_dict[command](args)
        else:
            console.print(Panel(f"❌ {invalid_command_message}", style="red", expand=True))

if __name__ == "__main__":
    main()
