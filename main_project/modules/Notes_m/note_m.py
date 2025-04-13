from collections import UserDict
from rich.console import Console
from rich.text import Text

console=Console()
class Note(UserDict):
    """
    A class representing a collection of notes, inheriting from UserDict.

    This class manages a dictionary of note records, providing functionality to add,
    find, and delete notes based on their titles.

    Attributes:
        data (dict): A dictionary storing note records, where the key is the title 
                     of the note and the value is the corresponding Record object.

    Methods:
        add_record(record): Adds a new note record to the collection. If the record 
                            does not have a title, an error message is printed to 
                            the console and the record is not added.
        find(title): Searches for a note record by its title. Returns the corresponding 
                     Record object if found, otherwise returns None.
        delete(title): Deletes the note record identified by the given title. Returns 
                       1 on successful deletion, or 0 if the record does not exist, 
                       with an error message printed to the console.
        __str__(): Returns a string representation of all note records in the collection.

    Usage:
        notes = Note()
        notes.add_record(record)
        found_note = notes.find("Note Title")
        notes.delete("Note Title")
        print(notes)
    """
    def add_record(self, record):
        if record.title is None:
            console.print(Text(f"Cannot add a record with no title.", style='red'))
            return
        self.data[record.title.value] = record

    def find(self, title):
        if title in self.data:
            return self.data[title]
        return None

    def delete(self, title):
        if title in self.data:
            del self.data[title]
            return 1
        else:
            console.print(Text(f"Error: Record for {title} not found.", style='red'))
            return 0
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

