from main_project.modules.Common_m.field import Field
import re
from rich.text import Text

class Phone(Field):
    def __init__(self, value):
        if value is None or not self.validate_phone(value):
            raise ValueError("[red]Invalid phone number format:[/red]", f"[red]{value}[/red]")
        super().__init__(value)
        

    @staticmethod
    def validate_phone(value):
         return bool(isinstance(value, str) and re.match(r"^\d{10}$", value))
