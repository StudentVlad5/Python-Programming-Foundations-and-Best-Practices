class Field:
    """
    A class representing a field that holds a single value.

    Attributes:
        value: The value contained in the field, which can be of any datatype.

    Methods:
        __init__(value): Initializes a new instance of the Field class with the given value.
        __str__(): Returns a string representation of the field's value.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)