from rich.console import Console
from rich.table import Table

def help():
    """
    Displays a table of available commands for the Address Book and Notes applications.

    The table categorizes commands by functionality, providing a brief description of each command's 
    purpose within the applications. The commands include options for managing contacts in an 
    Address Book and interacting with notes.

    It uses the `rich` library to create a formatted table that is displayed in the console.

    The commands include:
    - Address Book commands for viewing, adding, editing, and deleting contacts
    - Notes commands for managing notes and their associated tags
    - Logs and system commands for viewing logs and handling application control

    Example Usage:
        >>> help()  # Calls the help function to display available commands
    """
    console = Console()

    table = Table(title="📚 Available Commands", show_lines=True)

    table.add_column("Category", style="cyan", no_wrap=True)
    table.add_column("Command", style="magenta", no_wrap=False)
    table.add_column("Description", style="green")

    # Address Book Commands
    table.add_row("Address Book", "all-contacts", "Show all contacts")
    table.add_row("Address Book", "all-birthdays", "Show all birthdays")
    table.add_row("Address Book", "add", "Add full contact: name phone birthday email address")
    table.add_row("Address Book", "add-name", "Add a contact name")
    table.add_row("Address Book", "add-phone", "Add phone to contact: name phone")
    table.add_row("Address Book", "add-email", "Add email to contact: name email")
    table.add_row("Address Book", "add-birthday", "Add birthday: name dd.mm.yyyy")
    table.add_row("Address Book", "add-address", "Add address to contact: name address")
    table.add_row("Address Book", "contact", "Show full contact details: name")
    table.add_row("Address Book", "phone", "Show contact's phone")
    table.add_row("Address Book", "email", "Show contact's email")
    table.add_row("Address Book", "address", "Show contact's address")
    table.add_row("Address Book", "birthday", "Show contact's birthday")
    table.add_row("Address Book", "birthdays", "Upcoming birthdays in X days: number_of_days")
    table.add_row("Address Book", "search-contact", "Search for a contact by name")
    table.add_row("Address Book", "edit-phone", "Edit phone: name old_phone new_phone")
    table.add_row("Address Book", "edit-email", "Edit email: name old_email new_email")
    table.add_row("Address Book", "edit-birthday", "Edit birthday: name new_birthday")
    table.add_row("Address Book", "edit-address", "Edit address: name new_address")
    table.add_row("Address Book", "delete", "Delete a contact: name")
    table.add_row("Address Book", "delete-phone", "Remove phone: name phone")
    table.add_row("Address Book", "delete-email", "Remove email: name email")
    table.add_row("Address Book", "delete-birthday", "Remove birthday: name")
    table.add_row("Address Book", "delete-address", "Remove address: name")

    # Notes Commands
    table.add_row("Notes", "all-notes", "Show all notes")
    table.add_row("Notes", "add-note", "Add a note: title tags")
    table.add_row("Notes", "add-tag", "Add a tag to a note: title tag")
    table.add_row("Notes", "show-note", "Show a note by title")
    table.add_row("Notes", "edit-title", "Edit a note's title: title new_title")
    table.add_row("Notes", "search-tag", "Search notes by tag: tag")
    table.add_row("Notes", "search-message", "Search notes by message content: text")
    table.add_row("Notes", "delete-note", "Delete a note: title")
    table.add_row("Notes", "delete-tag", "Delete a tag from a note: title tag")

    # Logs & System Commands
    table.add_row("Logs", "all-logs", "Show all command logs")
    table.add_row("Logs", "logs-by-date", "Show logs by date: YYYY-MM-DD")
    table.add_row("System", "hello", "Greet the user")
    table.add_row("System", "exit", "Exit the application")
    table.add_row("System", "close", "Exit the application (alternative)")

    console.print(table)