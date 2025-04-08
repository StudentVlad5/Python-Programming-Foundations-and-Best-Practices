from ..Common_m.field import Field
import re
from rich.text import Text

class Email(Field):
    def __init__(self, value):
        if value is None or not self.validate_email(value):
            raise ValueError(
                Text("Invalid email format: ", style="yellow") + Text(value, style="red"))
        super().__init__(value)
        
    @staticmethod
    def validate_email(value):
        # Regular expression for a basic email validation
        email_regex = r"(^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)"
        return bool(isinstance(value, str) and re.match(email_regex, value))
