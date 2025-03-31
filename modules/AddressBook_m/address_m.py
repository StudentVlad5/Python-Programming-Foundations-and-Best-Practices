from ..Common_m.field import Field
from termcolor import colored

class Address(Field):
    def __init__(self, value):
        if value is None:
            raise ValueError(f"{colored('Invalid address format: ', 'yellow')}{colored(value, 'red')}")
        super().__init__(value)
        
