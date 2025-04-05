from modules.Common_m.dictionary import command_d_keys
from services.commands_logs import log_request
from termcolor import colored

@log_request
def handle_user_input(user_input):
    command_keys = command_d_keys()
    if user_input.split()[0] in command_keys:
        print(colored(f"Implementation: {user_input}", 'cyan'))
        return user_input
    else:
        print(colored("Unknown command. Try again.", 'red'))
        return None  
