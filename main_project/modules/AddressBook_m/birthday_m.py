from main_project.modules.Common_m.field import Field
from datetime import datetime
import re
from rich.text import Text

class Birthday(Field):
    def __init__(self, value):
        if value is None or not self.validate_birthday(value):
            raise ValueError(
                f"{Text('Invalid date format. Use DD.MM.YYYY. You provided:', style='yellow')} + {Text(value, style='red')}"
            )
        self.value = datetime.strptime(value, "%d.%m.%Y")

    @staticmethod
    def validate_birthday(value):
        return bool(re.match(r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$", value))
