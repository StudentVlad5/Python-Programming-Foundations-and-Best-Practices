from ..Common_m.field import Field
from rich.text import Text

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError(Text("Name cannot be empty.", style='red'))
        super().__init__(value)
