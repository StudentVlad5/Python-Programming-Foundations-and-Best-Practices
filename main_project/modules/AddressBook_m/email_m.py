from main_project.modules.Common_m.field import Field
import re
from rich.text import Text

class Email(Field):
    """
    A class representing an email address, inheriting from the Field class.

    This class validates the provided email to ensure it follows a basic 
    email format. If the supplied value is None or does not match the 
    expected format, a ValueError will be raised.

    Attributes:
        value: The valid email address contained in the field.

    Methods:
        __init__(value): Initializes a new instance of the Email class with 
                         the given email address. Raises ValueError if the 
                         value is None or does not match the required email format.
        validate_email(value): Static method that checks if the provided 
                               value is a valid email address using a regular 
                               expression.
    """
    def __init__(self, value):
        if value is None or not self.validate_email(value):
            raise ValueError(
                "[red]Invalid email format:[/red]", f"[red]{value}[/red]")
        super().__init__(value)
        
    @staticmethod
    def validate_email(value):
        # Regular expression for a basic email validation
        email_regex = r"(^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)"
        return bool(isinstance(value, str) and re.match(email_regex, value))
