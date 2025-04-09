from .tag_m import Tag
from .message_m import Message
from termcolor import colored
from rich.console import Console
from rich.text import Text

console=Console()

class Record:
    def __init__(self, title):
        # try:
        #     self.message = Message(message)
        # except ValueError as e:
        #     print(f"Error: {e}")
        #     self.message = None
        # self.tags = []
        try:
            self.title = Message(title)
        except ValueError as e:
            print(f"Error: {e}")
            self.title = None
        self.tags = []

    def add_tag(self, tag):
        try:
            self.tags.append(Tag(tag))
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
            raise ValueError(colored(f"Tag {old_tag} not found.", 'red'))
        except ValueError as e:
            console.print(Text(f"Error: {e}", style='red'))
            return 0
        
    def __str__(self):
        title_str = self.title.value if self.message else "No title"

        if self.tags:
            tags_str = ", ".join([tag.value for tag in self.tags])
        else:
            tags_str = "No tags"
            
        return f"{colored("Title: ",'cyan')} {colored(title_str, 'green')} {colored("Tags: ", 'cyan')} {colored(tags_str, 'green')}"
    # def __str__(self):
    #     message_str = self.message.value if self.message else "No message"

    #     if self.tags:
    #         tags_str = ", ".join([tag.value for tag in self.tags])
    #     else:
    #         tags_str = "No tags"
            
    #     return f"{colored("Message: ",'cyan')} {colored(message_str, 'green')} {colored("Tags: ", 'cyan')} {colored(tags_str, 'green')}"

