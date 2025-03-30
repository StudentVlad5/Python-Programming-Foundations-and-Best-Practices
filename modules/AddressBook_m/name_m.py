from ..Common_m.field import Field
from termcolor import colored

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError(colored("Name cannot be empty.", 'red'))
        super().__init__(value)
