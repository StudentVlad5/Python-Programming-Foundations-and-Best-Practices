def parse_input(user_input):
    if not user_input.strip():
        return "", [] 

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args
