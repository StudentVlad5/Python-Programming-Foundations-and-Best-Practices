import os
import pickle
from rich.text import Text
from rich.console import Console
from rich.panel import Panel

console = Console()

# Переходимо в корінь проєкту з services
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

def load_data(book, filename):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        console.print(Panel(Text(f"File '{filename}' not found at {filepath}", style='red')))
        return book

    try:
        with open(filepath, "rb") as file:
            return pickle.load(file)
    except Exception as e:
        console.print(Panel(Text("An error occurred while loading data:", style='yellow') + Text(str(e), style='red')))
        return book

def save_data(book, filename):
    filepath = os.path.join(BASE_DIR, filename)
    try:
        with open(filepath, "wb") as file:
            pickle.dump(book, file)
        console.print(Panel(Text(f"Data saved successfully to {filepath}", style='green')))
    except Exception as e:
        console.print(Panel(Text('An error occurred while saving data:', style='yellow') + Text(str(e), style='red')))
        console.print(Panel(Text("Possible cause: Could be an issue with pickling non-serializable objects.", style='yellow')))
