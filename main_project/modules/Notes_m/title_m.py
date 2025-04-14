from main_project.modules.Common_m.field import Field
from rich.text import Text

class Title(Field):
    """
    A class representing a title, inheriting from the Field class.

    This class validates the provided title to ensure it is a non-empty string. 
    If the supplied value is None or not a string, a ValueError will be raised.

    Attributes:
        value: The valid title contained in the field, represented as a string.

    Methods:
        __init__(value): Initializes a new instance of the Title class with the given title. Raises ValueError if the value is None or not a string.
        
        validate_message(value): Static method that checks if the provided value is a valid title, specifically checking that it is of type string.
    """
    def __init__(self, value):
        if value is None or not self.validate_message(value):
             raise ValueError(Text(f"Invalid title format: {value}", style='red'))
        super().__init__(value)
        

    @staticmethod
    def validate_message(value):
        return bool(isinstance(value, str))