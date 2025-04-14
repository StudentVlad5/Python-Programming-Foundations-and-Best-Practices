from functools import wraps
from rich.text import Text
from rich.console import Console

# wrap of errors
console=Console()

def input_error(func):
    """
    A decorator to handle errors in command functions.

    This decorator wraps a function to catch and handle specific exceptions that may
    occur during its execution. When an error is raised within the wrapped function, 
    it is caught and an appropriate error message is printed to the console using
    the `rich` library for enhanced formatting.

    Supported Exceptions:
        - ValueError: Caught when an invalid value is encountered, and an error message
          is printed indicating the specific error.
        - IndexError: Caught when not enough arguments are provided to the function,
          prompting the user with a specific error message.
        - General Exception: Catches any other unexpected errors and prints a message 
          with the error details.

    Parameters:
        func (function): The function to be wrapped by the decorator.

    Returns:
        function: The wrapped function, which now includes error handling.

    Example Usage:
        @input_error
        def add_contact(self, name, phone):
            # Function implementation
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs): 
        try:
            return func(self, *args, **kwargs)
        except ValueError as e:
            console.print(Text(f"Error: {e}", style='red'))
        except IndexError:
            console.print(Text("Error: Not enough arguments provided.",style='red'))
        except Exception as e:
            console.print(Text(f"Unexpected error: {e}",style='red'))
    return wrapper

