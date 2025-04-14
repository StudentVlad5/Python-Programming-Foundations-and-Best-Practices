from main_project.modules.Common_m.field import Field
from datetime import datetime
import re

class Birthday(Field):
    """
    A class representing a birthday, inheriting from the Field class.

    This class validates the given date to ensure it follows the format 
    DD.MM.YYYY. If the provided value is None or does not match this 
    format, a ValueError will be raised.

    Attributes:
        value: The valid birthday value contained in the field, represented 
               as a datetime object.

    Methods:
        __init__(value): Initializes a new instance of the Birthday class 
                         with the given date value. Raises ValueError if the 
                         value is None or does not match the required format.
        validate_birthday(value): Static method that checks if the given 
                                  date string is in the correct format 
                                  (DD.MM.YYYY) using a regular expression.
    """
    def __init__(self, value):
        if value is None or not self.validate_birthday(value):
            raise ValueError(
                "[red]Invalid date format. Use DD.MM.YYYY. You provided:[/red]", f"[red]{value}[/red]"
            )
        self.value = datetime.strptime(value, "%d.%m.%Y")

    @staticmethod
    def validate_birthday(value):
        return bool(re.match(r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$", value))
