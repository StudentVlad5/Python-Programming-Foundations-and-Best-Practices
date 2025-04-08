import os
import pickle
from rich.text import Text
from rich.console import Console
from rich.panel import Panel

console = Console()

# Upload contacts from a pickle file
def load_data(book, filename):
    if not os.path.exists(filename):
        console.print(Panel(Text("File not found",style='red')))
        return book

    try:
        with open(filename, "rb") as file:
            return pickle.load(file) 
    except Exception as e:
        console.print(Panel(Text("An error occurred while loading data:", style= 'yellow') + Text(e, style='red')))
        return book

# Save contacts to a pickle file
def save_data(book, filename):
    try:
        with open(filename, "wb") as file:
            pickle.dump(book, file)
        console.print(Panel(Text('Data saved successfully', style='green')))
    except Exception as e:
        console.print(Panel(Text('An error occurred while saving data:', style='yellow') + Text(str(e), style='red')))
        console.print(Panel(Text("Possible cause: Could be an issue with pickling non-serializable objects.", style='yellow')))
