from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from modules.Common_m.dictionary import command_list, command_d_keys
from termcolor import colored

command_completer = WordCompleter(command_list, ignore_case=True)

def handle_user_input():
    # Введення з автозаповненням команд
    user_input = prompt("Enter a command: ", completer=command_completer)
    command_keys = command_d_keys()
    if user_input.split()[0] in command_keys:
        print(colored(f"Implementation: {user_input}", 'cyan'))
        return user_input
    else:
        print(colored("Unknown command. Try again.", 'red'))
        return None  
