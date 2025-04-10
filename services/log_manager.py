import csv
import datetime
from rich.console import Console
from rich.table import Table

LOG_FILE = "commands_log.csv"

def init_log_file():
    """
    Створює лог-файл з заголовками, якщо файл ще не існує.
    """
    try:
        # Режим "x" створює файл, якщо його ще немає.
        with open(LOG_FILE, "x", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["timestamp", "command", "parameters", "result"])
    except FileExistsError:
        pass

def log_command(command, parameters, result):
    """
    Логує виконання команди, додаючи запис у лог-файл.
    
    :param command: Назва команди, наприклад, "add"
    :param parameters: Параметри команди у вигляді рядка.
    :param result: Результат виконання команди (рядок, повідомлення).
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, command, parameters, result])

def get_logs_for_date(report_date):
    """
    Зчитує лог-файл і повертає список записів, де timestamp починається із звітної дати.
    
    :param report_date: Дата у форматі "YYYY-MM-DD"
    :return: Список записів-словників
    """
    logs = []
    with open(LOG_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Перевіряємо, чи починається поле timestamp з звітної дати
            if row["timestamp"].startswith(report_date):
                logs.append(row)
    return logs

def print_logs_for_date(report_date):
    """
    Виводить лог-за задану дату у зручному форматі в консоль.
    """
    console = Console()
    logs = get_logs_for_date(report_date)
    if not logs:
        console.print(f"[red]За дату {report_date} немає логів.[/red]")
        return
    console.print(f"[green]Логи за дату {report_date}:[/green]")
    for log in logs:
        # Формуємо рядок для кожного запису
        console.print(f"[blue]{log['timestamp']}[/blue] - [yellow]{log['command']}[/yellow]  {log['parameters']} -> {log['result']}")

def get_statistics_for_date(report_date):
    """
    Обчислює статистику команд за звітну дату – підраховує кількість виконань кожної команди.
    
    :param report_date: Дата у форматі "YYYY-MM-DD"
    :return: Словник типу {command: count}
    """
    logs = get_logs_for_date(report_date)
    stats = {}
    for log in logs:
        cmd = log["command"]
        stats[cmd] = stats.get(cmd, 0) + 1
    return stats

def print_statistics_for_date(report_date):
    """
    Виводить таблицю зі статистикою команд за задану дату за допомогою rich.Table.
    """
    stats = get_statistics_for_date(report_date)
    console = Console()
    if not stats:
        console.print(f"[red]За дату {report_date} немає статистичних даних.[/red]")
        return
    table = Table(title=f"Статистика команд за дату {report_date}")
    table.add_column("Команда", justify="left", style="cyan", no_wrap=True)
    table.add_column("Кількість", justify="right", style="magenta")
    for command, count in stats.items():
        table.add_row(command, str(count))
    console.print(table)

# --- Приклад використання:
if __name__ == "__main__":
    # Ініціалізуємо лог-файл (створюється, якщо ще не існує)
    init_log_file()

    # Приклад логування декількох команд
    log_command("add", "name=John, phone=1234567890", "Контакт додано")
    log_command("delete", "name=John", "Контакт видалено")
    log_command("add", "name=Jane, phone=0987654321", "Контакт додано")
    log_command("update", "name=Jane, email=jane@example.com", "Контакт оновлено")
    
    # Встановлюємо звітну дату (наприклад, сьогодні)
    report_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Виводимо логи за звітну дату
    print_logs_for_date(report_date)
    
    # Виводимо таблицю статистики команд за звітну дату
    print_statistics_for_date(report_date)
