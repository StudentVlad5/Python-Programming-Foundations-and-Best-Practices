from ..Common_m.field import Field
from rich.text import Text

class Title(Field):
    def __init__(self, value):
        if value is None or not self.validate_message(value):
             raise ValueError(Text(f"Invalid title format: {value}", style='red'))
        super().__init__(value)
        

    @staticmethod
    def validate_message(value):
        return bool(isinstance(value, str))