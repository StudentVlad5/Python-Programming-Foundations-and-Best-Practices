"""
This module provides functionality for loading and saving data to and from files 
using Python's built-in `pickle` module, along with rich text output for console 
messages.

The module utilizes the `os` library to manage file paths and directory structures, 
ensuring that data operations occur in the correct project directory.

Functions:
    load_data(book, filename): Loads data from a specified file into the provided 
                               'book' object. If the file does not exist or an error 
                               occurs during loading, it prints an error message to 
                               the console and returns the original 'book' object.
    save_data(book, filename): Saves the provided 'book' object to a specified 
                               file. If an error occurs during saving, an error 
                               message is printed to the console, and the user is 
                               informed of potential causes.

Constants:
    console (Console): An instance of the Console class from the `rich` library,
                       used for formatting and printing messages to the terminal.

Usage Example:
    book_data = {}
    book_data = load_data(book_data, 'data.pkl')
    save_data(book_data, 'data.pkl')
"""
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
