from functools import wraps
from rich.text import Text
from rich.console import Console

# wrap of errors
console=Console()

def input_error(func):
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

