from ..Common_m.field import Field
from termcolor import colored

class Tag(Field):
    def __init__(self, value):
        if value is None or not self.validate_message(value):
            raise ValueError(f"{colored("Invalid tag format: ", 'yellow')}{colored(value, 'red')}")
        super().__init__(value)
        

    @staticmethod
    def validate_message(value):
        return bool(isinstance(value, str))
