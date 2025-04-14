from main_project.modules.Common_m.field import Field
from rich.text import Text

class Name(Field):
    """
    A class representing a name, inheriting from the Field class.

    This class ensures that the provided name is not empty. If an attempt
    is made to initialize a Name object with an empty value, a ValueError 
    will be raised.

    Attributes:
        value: The valid name contained in the field, which must be a 
               non-empty string.

    Methods:
        __init__(value): Initializes a new instance of the Name class with 
                         the given name. Raises ValueError if the value is 
                         empty.
    """
    def __init__(self, value):
        if not value:
            raise ValueError(Text("Name cannot be empty.", style='red'))
        super().__init__(value)
