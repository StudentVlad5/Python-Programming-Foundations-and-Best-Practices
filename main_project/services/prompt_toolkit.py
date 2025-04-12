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
