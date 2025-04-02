# Python-Programming-Foundations-and-Best-Practices

AddressBook and Notes CLI System
This Python-based command-line application provides functionalities to manage contacts in an AddressBook and manage notes. It offers a set of commands to add, view, edit, and delete contact details and notes.

Features
AddressBook Features:
Add a Contact: Add a contact with details like name, phone number, email, birthday, and address.

Show Contacts: Display all contacts and search for contact details like phone, email, address, and birthday.

Edit Contact Details: Edit a contact's phone number, email, address, or birthday.

Delete Contact: Delete a contact from the AddressBook.

Show Birthdays: View all birthdays or search for birthdays on a specific date.

Notes Features:
Add a Note: Add notes with optional tags.

View Notes: Display all notes or search for notes based on tags or text content.

Edit Note: Edit the message of a note.

Delete Note: Delete a note.

Add/Remove Tags: Add or remove tags for notes.

Installation
Clone the repository:

bash
Копіювати
git clone <repository_url>
Install the required dependencies using pip:

bash
Копіювати
pip install -r requirements.txt
Ensure that you have Python 3.x installed. You can verify the installation by running:

bash
Копіювати
python --version
Usage
Commands
The following commands are available in the AddressBook and Notes CLI system:

AddressBook Commands
hello – Greets the user.

all-contacts – Displays all contacts in the address book.

all-birthdays – Displays all birthdays in the address book.

add – Add a new contact with full details (name, phone, birthday, email, address).

add-phone – Add a phone number to a contact.

add-email – Add an email to a contact.

add-birthday – Add a birthday to a contact.

add-address – Add an address to a contact.

phone – View a contact's phone number.

email – View a contact's email address.

address – View a contact's address.

birthday – View a contact's birthday.

birthdays – Show contacts with a specific birthday (in dd.mm.yyyy format).

edit-address – Edit a contact's address.

edit-birthday – Edit a contact's birthday.

edit-email – Edit a contact's email address.

edit-phone – Edit a contact's phone number.

delete – Delete a contact.

delete-address – Delete a contact's address.

delete-birthday – Delete a contact's birthday.

delete-email – Delete a contact's email.

delete-phone – Delete a contact's phone number.

Notes Commands
all-note – Show all notes.

add-note – Add a new note with message and optional tags.

add-tag – Add a tag to a note.

show-message – Show a note based on its message content.

edit-message – Edit the message of a note.

search-tag – Search notes by tags.

search-message – Search notes by message content.

delete-note – Delete a note.

delete-tag – Remove a tag from a note.

Other Commands
exit – Exit the application.

close – Close the application (same as exit).

Example Usage
bash
Копіювати
# Run the program
$ python main.py

Enter a command: add John 1234567890 john@example.com 01.01.1990 123 Street
Implementation: Add contact

Enter a command: all-contacts
Implementation: Show all contacts
Autocompletion
The program supports autocompletion of commands. As you start typing a command, the available options will be shown.

Saving Data
The data for both the AddressBook and Notes are saved to files:

addressbook.pkl – AddressBook data (contacts).

notes.pkl – Notes data.

You can load and save these files using the commands provided, and the system will handle serialization and deserialization automatically.

File Structure
The project has the following structure:

sql
Копіювати
/your_project_folder
|-- main.py                  # Main program file
|-- services/                # Folder containing service logic for address book and notes
|   |-- address_book_manager.py
|   |-- note_manager.py
|-- modules/                 # Contains the AddressBook and Notes classes
|   |-- AddressBook_m/
|   |-- Notes_m/
|   |-- Common_m/
|-- requirements.txt         # List of dependencies
|-- .gitignore               # Git ignore file
|-- README.md                # Project documentation
Development
If you'd like to contribute to the project, feel free to fork the repository and submit a pull request. Before making changes, make sure to run the tests (if any) and ensure that the code works as expected.

Additional Notes:
The command_d function maps commands to their corresponding action in the AddressBook and Notes system. The function command_d_keys returns a list of available commands that the user can execute.

The command_list defines a comprehensive list of commands with syntax explanations to help users understand the required input.

License
This project is licensed under the MIT License - see the LICENSE file for details.