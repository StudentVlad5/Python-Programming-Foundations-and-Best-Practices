from main_project.modules.Common_m.field import Field
import re

class Phone(Field):
    """
    A class representing a phone number, inheriting from the Field class.

    This class validates the provided phone number to ensure it is in the 
    correct format. The expected format is a string containing exactly 
    10 digits. If the supplied value is None or does not match this 
    format, a ValueError will be raised.

    Attributes:
        value: The valid phone number contained in the field, represented 
               as a string of digits.

    Methods:
        __init__(value): Initializes a new instance of the Phone class with 
                         the given phone number. Raises ValueError if the 
                         value is None or does not match the required format.
        validate_phone(value): Static method that checks if the provided 
                               value is a valid phone number (10 digits) 
                               using a regular expression.
    """
    def __init__(self, value):
        if value is None or not self.validate_phone(value):
            raise ValueError("[red]Invalid phone number format:[/red]", f"[red]{value}[/red]")
        super().__init__(value)
        

    @staticmethod
    def validate_phone(value):
         return bool(isinstance(value, str) and re.match(r"^\d{10}$", value))
