from collections import UserDict
from rich.console import Console
from rich.text import Text

console=Console()
class Note(UserDict):
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

