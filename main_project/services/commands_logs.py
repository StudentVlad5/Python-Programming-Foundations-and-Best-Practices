"""
This module provides functionality for logging function calls and managing log entries
in a simple command-line application. It includes a decorator for logging requests, 
functions to display logs, and a way to analyze logs by date.

Logging Decorator:
    log_request(func): A decorator that logs the timestamp, command name, and arguments
                       of a function call to a specified log file.

Log Management Functions:
    parse_logs(log_filename): A generator that reads log entries from the specified file,
                              yielding tuples of (timestamp, function name, arguments).
    all_logs(): Displays all logged entries in a formatted table in the console.
    logs_by_date(args): Displays logs for a specified date, formatting the output in a table.
    stats_by_date(args): Displays the count of commands executed on a specified date.

Constants:
    log_filename (str): The file path where logs are stored, imported from the application's 
                        CONSTANT module.

Example Usage:
    @log_request
    def sample_function(arg1, arg2):
        # function implementation
"""
from functools import wraps
from datetime import datetime
from rich.console import Console
from rich.table import Table
from main_project.modules.Common_m.CONSTANT import log_filename

console = Console()

#log decorator
def log_request(func):
    """
    A decorator to log function calls with their arguments and timestamps.

    This decorator wraps a function and writes a log entry each time the function is called. 
    It logs the timestamp, the function name, and the arguments provided to the function. 
    The logs are written to the specified log file.

    Parameters:
        func (function): The function to be wrapped and logged.

    Returns:
        function: The wrapped function, with logging functionality added.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_msg = ""
        if args:
            if func.__name__ == "handle_user_input" and args:
                if args[0]:
                    command_str = args[0].split()[0]
                    log_msg = f"{timestamp} | Command: {command_str} | Args: {args} \n"
                else:
                    command_str = "handle_user_input"
                    log_msg = f"{timestamp} | Command: {command_str} | Args: {args} \n"
            else:
                command_str = func.__name__
                log_msg = f"{timestamp} | Command: {command_str} | Args: {args} \n"
        else:
            command_str = func.__name__
            log_msg = f"{timestamp} | Command: {command_str} | Args: {args} \n"
    
        with open(log_filename, "a", encoding="utf-8") as log_file:
            log_file.write(log_msg)
        
        return func(*args, **kwargs)
    
    return wrapper

# generator for logs
def parse_logs(log_filename):
    """
    Reads and parses log entries from the specified log file.

    This function yields tuples containing timestamp, function name, and arguments
    for each log entry in the file. If the file is not found, it yields None.

    Parameters:
        log_filename (str): The path to the log file to read.

    Yields:
        tuple: A tuple of (timestamp, function name, arguments) for each log entry.
               If the log format is incorrect, empty strings are returned.
               Yields None if the log file is not found.
    """
    try:
        with open(log_filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                parts = line.split(" | ")
                if len(parts) >= 3:
                    timestamp = parts[0]
                    func_name = parts[1].replace("Function: ", "")
                    args_part = parts[2].replace("Args: ", "")
                    yield (timestamp, func_name, args_part)
                else:
                    yield (line, "", "")
    except FileNotFoundError:
        yield None  

#see all logs
def all_logs():
    """
    Displays all logs in a formatted table in the console.

    This function retrieves all log entries using `parse_logs` and presents them 
    in a readable format, using a rich table for better visualization. If the log 
    file is not found or is empty, appropriate messages are printed.

    Returns:
        None
    """
    log_rows = parse_logs(log_filename)

    console = Console()
    table = Table(title="All Logs", header_style="bold green")
    table.add_column("Timestamp", style="blue", justify="left")
    table.add_column("Function", style="cyan", justify="left")
    table.add_column("Arguments", style="yellow", justify="left")

    found_logs = False
    for row in log_rows:
        if row is None:
            console.print("[red]Log file not found.[/red]")
            return
        table.add_row(*row)
        found_logs = True

    if not found_logs:
        console.print("[red]No logs available.[/red]")
        return

    console.print(table)

#see logs by date
def logs_by_date(args):
    """
    Displays logs that match a specified date.

    This function takes a date argument in the format YYYY-MM-DD, reads the log file, 
    and presents entries that correspond to that date in a formatted table. 
    If the date argument is missing or invalid, an error message is displayed.

    Parameters:
        args (list): A list containing the date as the first element.

    Returns:
        None
    """
    if not args:
        console.print("[red]Missing date argument.[/red]")
        return

    date_str = args[0] 
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        console.print("[red]Invalid date format. Use YYYY-MM-DD.[/red]")
        return

    try:
        with open(log_filename, "r", encoding="utf-8") as file:
            matched_lines = [line.strip() for line in file if line.startswith(date_str)]
    except FileNotFoundError:
        console.print("[red]Log file not found.[/red]")
        return

    if not matched_lines:
        console.print(f"[yellow]No logs found for date: {date_str}[/yellow]")
        return

    table = Table(title=f"Logs for {date_str}", header_style="bold green")
    table.add_column("Timestamp", style="blue", justify="left")
    table.add_column("Function", style="cyan", justify="left")
    table.add_column("Arguments", style="yellow", justify="left")

    for line in matched_lines:
        parts = line.split(" | ")
        if len(parts) >= 3:
            timestamp = parts[0]
            func_name = parts[1].replace("Function: ", "")
            args_part = parts[2].replace("Args: ", "")
            table.add_row(timestamp, func_name, args_part)
        else:
            table.add_row(line, "", "")

    console.print(table)

def stats_by_date(args):
    """
    Displays command execution statistics for a specified date.

    This function takes a date argument in the format YYYY-MM-DD, 
    reads the log file, and counts how many times each command was executed on that date.
    The results are displayed in a formatted table. If the date argument is missing or 
    invalid, or if no logs are found for that date, appropriate messages are displayed.

    Parameters:
        args (list): A list containing the date as the first element.

    Returns:
        None
    """
    if not args:
        console.print("[red]Missing date argument.[/red]")
        return

    date_str = args[0]
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        console.print("[red]Invalid date format. Use YYYY-MM-DD.[/red]")
        return

    stats = {}
    found = False
    try:
        with open(log_filename, "r", encoding="utf-8") as file:
            matched_lines = (line.strip() for line in file if line.startswith(date_str))
            for line in matched_lines:
                found = True
                parts = line.split(" | ")
                if len(parts) >= 2:
                    command_logged = parts[1].strip()
                    if command_logged.startswith("Command: "):
                        command_logged = command_logged.replace("Command: ", "").strip()
                    elif command_logged.startswith("Function: "):
                        command_logged = command_logged.replace("Function: ", "").strip()
                    command_name = command_logged.split()[0]
                    stats[command_name] = stats.get(command_name, 0) + 1
    except FileNotFoundError:
        console.print("[red]Log file not found.[/red]")
        return

    if not found:
        console.print(f"[yellow]No logs found for date: {date_str}[/yellow]")
        return

    table = Table(title=f"Statistics for {date_str}", header_style="bold green")
    table.add_column("Command", justify="left", style="cyan", no_wrap=True)
    table.add_column("Count", justify="right", style="magenta")
    for command, count in stats.items():
        table.add_row(command, str(count))

    console.print(table)