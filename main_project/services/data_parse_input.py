def parse_input(user_input):
    """
    Parses a user input string into a command and its arguments.

    This function takes a user's input as a string, trims any leading or trailing whitespace, 
    and splits the input into components. The first part is treated as the command, and the 
    remaining parts are treated as its arguments.

    Parameters:
        user_input (str): The raw input string entered by the user.

    Returns:
        tuple: A tuple containing:
            - cmd (str): The command part of the input, converted to lowercase. 
                         Returns None if the input is empty or contains only whitespace.
            - args (list): A list of arguments following the command. It is an empty list 
                           if no arguments are provided.

    Example Usage:
        >>> command, arguments = parse_input("add-note My first note")
        >>> print(command)  # Output: "add-note"
        >>> print(arguments)  # Output: ["My", "first", "note"]
    """
    parts = user_input.strip().split()
    if not parts:
        return None, []

    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args
