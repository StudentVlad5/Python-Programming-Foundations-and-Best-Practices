def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return None, []

    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args
