from functools import wraps
from datetime import datetime
from rich.console import Console
from rich.table import Table
from main_project.modules.Common_m.CONSTANT import log_filename

console = Console()

#log decorator
def log_request(func):
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