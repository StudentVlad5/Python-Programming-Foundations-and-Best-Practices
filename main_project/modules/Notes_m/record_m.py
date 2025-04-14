from main_project.modules.Notes_m.title_m import Title
from main_project.modules.Notes_m.tag_m import Tag
from rich.console import Console
from rich.text import Text

console=Console()

class Record:
    """
    A class representing a note record with a title, tags, and a message.

    This class manages a note's title, tags, and message, providing functionality
    to add, delete, and edit tags associated with the note. It validates the title 
    and manages lists of tags, ensuring that tags are unique (case-insensitive).

    Attributes:
        title (Title): The title of the note, represented by a Title object.
        tags (list): A list of Tag objects associated with the note.
        message (str): The message content of the note.

    Methods:
        __init__(title, tags=None, message=None): Initializes a new instance of the 
                                                  Record class with the given title, 
                                                  optional tags, and optional message.
                                                  Raises ValueError if the title is invalid.
        add_tag(tag): Adds a new tag to the note. Returns 1 on success, 0 if the
                      tag already exists or if there is a ValueError.
        delete_tag(tag): Deletes the specified tag from the note. Returns 1 on 
                         success or 0 if no matching tag is found.
        edit_tag(old_tag, new_tag): Edits an existing tag by replacing it with a new tag.
                                     Returns 1 on success, or raises a ValueError if 
                                     the old tag is not found.
        __str__(): Returns a string representation of the note including the title,
                   tags, and message in a formatted manner.

    Usage:
        record = Record("My First Note", ["personal", "important"], "This is the content.")
        record.add_tag("urgent")
        record.edit_tag("important", "high priority")
        print(record)
    """
    def __init__(self, title, tags=None, message=None):
        try:
            self.title = Title(title)
        except ValueError as e:
            console.print(Text(f"Error: {e}", style='red'))
            self.title = None
            
        self.tags = tags if tags is not None else [] 
        self.message = message

    def add_tag(self, tag):
        try:
            tag_obj = Tag(tag)
            new_tag_value = tag_obj.value.lower()

            if any(t.value.lower() == new_tag_value for t in self.tags):
                return 0
            else:
                self.tags.append(tag_obj)
                return 1
        except ValueError as e:
            console.print(Text(f"Error: {e}", style='red'))
            return 0

    def delete_tag(self, tag):
        try: 
            self.tags = [t for t in self.tags if t.value != tag]
            return 1
        except ValueError as e:
            console.print(Text(f"Error: {e}", style='red'))
            return 0

    def edit_tag(self, old_tag, new_tag):
        try:
            for t in self.tags:
                if t.value == old_tag:
                    self.add_tag(new_tag)
                    self.delete_tag(old_tag)
                    return 1
            raise ValueError(Text(f"Tag {old_tag} not found.", style='red'))
        except ValueError as e:
            console.print(Text(f"Error: {e}", style='red'))
            return 0
        
    def __str__(self):
        title_str = self.title.value if self.title else "No title"
        tags_str = ", ".join([tag.value for tag in self.tags]) if self.tags else "No tags"
        message_str = self.message if self.message else "No message"
            
        return f"{Text(f'Title: {title_str}; Tags: {tags_str}; Message: {message_str}', style='cyan')}"
