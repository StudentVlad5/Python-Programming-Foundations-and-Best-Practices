"""
Handles user input by parsing commands and logging the request for further processing.

This function takes user input as a string, splits it into tokens, and checks if the first token 
corresponds to a known command. If the command is recognized, it logs the input and returns it 
for further processing. If the command is unknown, it notifies the user.

Parameters:
    user_input (str): The raw user input string containing the command and any optional arguments.

Returns:
    str: The original user input if the command is recognized; otherwise, returns None.

Example Usage:
    >>> handle_user_input("add John Doe 123-456-7890")
    Implementation: add John Doe 123-456-7890
    'add John Doe 123-456-7890'
    
    >>> handle_user_input("unknown command")
    Unknown command. Try again.
    None

Additional Notes:
    - The function uses a decorator `@log_request` to log the incoming user requests.
    - The command keys are retrieved from an imported function `command_d_keys` which should 
      return a list of valid command strings.
"""
from main_project.modules.Common_m.dictionary import command_d_keys
from main_project.services.commands_logs import log_request
from rich.console import Console
from rich.text import Text

console=Console()

@log_request
def handle_user_input(user_input):
    command_keys = command_d_keys()  
    user_input_split = user_input.split()

    if user_input_split:
        command = user_input_split[0]  
        if command in command_keys:
            console.print(Text(f"Implementation: {user_input}", style='cyan'))
            return user_input
    else:
        console.print(Text("Unknown command. Try again.", style='red'))
        return None
