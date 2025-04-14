from main_project.modules.Common_m.field import Field


class Address(Field):
    """
    A class representing an address, inheriting from the Field class.

    This class ensures that the address value is not None. If an attempt is 
    made to initialize an Address with a None value, a ValueError will be raised.

    Attributes:
        value: The valid address value contained in the field.

    Methods:
        __init__(value): Initializes a new instance of the Address class with 
                         the given address value. Raises ValueError if the 
                         value is None.
    """
    def __init__(self, value):
        if value is None:
            raise ValueError("[red]Invalid address format:[/red]", f"[red]{value}[/red]")
        super().__init__(value)
        
