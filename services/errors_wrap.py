from functools import wraps
from termcolor import colored

# wrap of errors
def input_error(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs): 
        try:
            return func(self, *args, **kwargs)
        except ValueError as e:
            print(colored(f"Error: {e}", 'red'))
        except IndexError:
            print(colored("Error: Not enough arguments provided.",'red'))
        except Exception as e:
            print(colored(f"Unexpected error: {e}",'red'))
    return wrapper

