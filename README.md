# Python-Programming-Foundations-and-Best-Practices
# AddressBook and Notes CLI System

This Python-based command-line application allows users to manage contacts in an sorted AddressBook and organize notes. You can add, view, edit, and delete contact details and notes using a variety of simple commands.
Akso implemented a decorator for logging user commands. 
---

## Features

### **AddressBook Features**

- **Add a Contact**: Add a new contact with details like name, phone number, email, birthday, and address.
- **Show Contacts**: View all contacts or search by phone, email, address, or birthday.
- **Edit Contact Details**: Modify a contact's phone number, email, address, or birthday.
- **Delete Contact**: Remove a contact from the AddressBook.
- **Show Birthdays**: View upcoming birthdays or search for birthdays on a specific date.

### **Notes Features**

- **Add a Note**: Write a new note with an optional set of tags.
- **View Notes**: View all notes or search for notes by tag or text content.
- **Edit Note**: Edit the content of an existing note.
- **Delete Note**: Delete a note from the system.
- **Add/Remove Tags**: Add or remove tags for organizing notes.

---

## Installation

1. **Clone the repository**:

    ```bash
    git clone <repository_url>
    ```

2. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Verify Python installation**:

    Ensure you have Python 3.x installed:

    ```bash
    python --version
    ```

---

## Usage

1. **Run the Program**:

    ```bash
    python main.py
    ```

2. **Available Commands**:

### AddressBook Commands

- `hello` – Greet the user.
- `all-contacts` – Display all contacts in the address book.
- `all-birthdays` – Display all birthdays in the address book.
- `add` – Add a new contact with full details (name, phone, email, birthday, address).
- `add-phone` – Add a phone number to an existing contact.
- `add-email` – Add an email to an existing contact.
- `add-birthday` – Add a birthday to a contact.
- `add-address` – Add an address to a contact.
- `phone` – View a contact's phone number.
- `email` – View a contact's email address.
- `address` – View a contact's address.
- `birthday` – View a contact's birthday.
- `birthdays` – Show contacts with a specific birthday (in `dd.mm.yyyy` format).
- `edit-*` – Edit specific contact details (address, birthday, email, phone).
- `delete` – Delete a contact.
- `delete-*` – Delete specific contact details (address, birthday, email, phone).

### Notes Commands

- `all-notes` – Show all notes.
- `add-note` – Add a new note with a message and optional tags.
- `add-tag` – Add a tag to a note.
- `show-note` – Display a note based on its message content.
- `edit-title` – Edit the title of a note.
- `search-tag` – Search notes by tags.
- `search-message` – Search notes by message content.
- `delete-note` – Delete a note.
- `delete-tag` – Remove a tag from a note.

### Other Commands

- `exit` or `close` – Close the application.

---

### Example Usage

```bash
# Run the program
$ python main.py

# Add a new contact
Enter a command: add John 1234567890 john@example.com 01.01.1990 123 Street

# Show all contacts
Enter a command: all-contacts

Autocompletion
The program supports autocompletion of commands. As you start typing a command, the available options will be shown.

Data Saving
The system automatically saves data for both the AddressBook and Notes in the following files:

addressbook.pkl – Contains AddressBook data (contacts).

notes.pkl – Contains Notes data.

log_file.txt – Contains commands log.

The system handles serialization and deserialization of this data automatically.

File Structure
your_project_folder/
│
├── main.py                  # Main program file
├── services/                # Contains service logic for AddressBook and Notes
│   ├── address_book_manager.py
│   ├── note_manager.py
│   ├── commands_logs.py
│   ├── data_parse_input.py
│   ├── errors_wrap.py
│   ├── file_manager.py
│   └── promt_toolkit.py
├── modules/                 # Contains the AddressBook and Notes classes
│   ├── AddressBook_m/
│   ├── Notes_m/
│   └── Common_m/
├── requirements.txt         # List of dependencies
├── .gitignore               # Git ignore file
├── log_file.txt             # Logs of user's commands
├── addressbook.pkl          # Data of address contacts
├── notes.pkl                # Data of notes
└── README.md                # Project documentation

Contributing
Feel free to fork the repository and submit a pull request. Before making changes, please:

Run any existing tests to ensure everything works as expected.

Write tests for any new features or fixes.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

