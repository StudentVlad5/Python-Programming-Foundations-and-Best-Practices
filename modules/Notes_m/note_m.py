from collections import UserDict
from termcolor import colored

class Note(UserDict):
    def add_record(self, record):
        if record.message is None:
            print(colored(f"Cannot add a record with an invalid message.", 'red'))
            return
        self.data[record.message.value] = record

    def find(self, message):
        if message in self.data:
            return self.data[message]
        return None

    def delete(self, message):
        if message in self.data:
            del self.data[message]
            return 1
        else:
            print(f"{colored('Error: Record for', 'yellow')} {colored(message, 'red')} {colored('not found.', 'yellow')}")
            return 0
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

