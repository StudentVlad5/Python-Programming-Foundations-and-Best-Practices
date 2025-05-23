"""
This module provides functionalities for managing notes in a command-line interface 
using the `rich` library for formatted output.

It allows users to add, edit, delete, and search notes and their associated tags. 
Notes are represented as `Record` objects, which encapsulate a title, tags, and a message. 
Data persistence is managed through file-saving operations.

Dependencies:
- Record from main_project.modules.Notes_m.record_m
- save_data from main_project.services.file_manager
- filenameNotes from main_project.modules.Common_m.CONSTANT
- rich console components for enhanced display

Functions:
    add_note(notes, args): Adds a new note with the given title and optional tags.
                           Prompts the user to input a message for the note.
    add_tag(notes, args): Adds tags to an existing note identified by the title.
    delete_tag(notes, args): Deletes a specified tag from an existing note.
    show_all_notes(notes): Displays all existing notes, or a message if none are available.
    show_note(notes, args): Displays the content of a specific note identified by the title.
    edit_title(notes, args): Edits the title of an existing note.
    delete_note(notes, args): Deletes a note based on the title provided.
    search_tag(notes, args): Searches for notes containing a specified tag.
    search_message(notes, args): Searches for notes containing a specified message input.
    notes_print_helper(arr): A helper function to print a formatted table of notes and their details.

Example Usage:
    notes = Note()
    add_note(notes, ["My First Note", "important", "urgent"])
    show_all_notes(notes)
    search_tag(notes, ["urgent"])
"""
from main_project.modules.Notes_m.record_m import Record
from main_project.services.file_manager import save_data
from main_project.modules.Common_m.CONSTANT import filenameNotes
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich import box
import sys

console=Console()
# Function to handle command "add"
def add_note(notes, args):
    if not args or len(args) < 1:
        console.print(Text(f"Missing title", style='red'))
    else:
        try:
            title = args[0]
            tags = args[1:] if len(args) > 1 else None

        except Exception as e:
            console.print(Text(f"Error: {e}", style='red'))
            return

        record = notes.find(title)
        if record:
            console.print(Text(f"You already have title {title} in your notes", style='red'))
        else:
            record = Record(title)
            try:
                if tags:
                    for tag in tags:
                        record.add_tag(tag)
            except ValueError as e:
                console.print(Text(f"Error: {e}", style='red'))

            print("Please enter the message for this note. To finish editing:")
            print("Linux/macOS: Press Ctrl + D (hold down the Ctrl key and press the D key)")
            print("Windows: Press Ctrl + Z, then press Enter.")
            #message = input("Please enter the message for this note: ")
            note_lines = sys.stdin.readlines()
            message = "".join(note_lines)
            record.message = message

            notes.add_record(record)
            save_data(notes.data, filenameNotes)
            show_note(notes, [title])
            console.print(Text(f"Added '{title}' with message {message}.", style='green'))

# Function to handle command "add-tag"
def add_tag(notes, args):
    if len(args) < 2:
        console.print(Text(f"Missing title or tag", style='red'))
    else:
        try:
            title = args[0]
            tags = args[1:] if len(args) > 1 else None

        except Exception as e:
            console.print(Text(f"Error: {e}", style='red'))
            return

        record = notes.find(title)
        if record:
            try:
                if tags:
                    for tag in tags:
                        if record.add_tag(tag):
                           record.add_tag(tag)
                           save_data(notes.data, filenameNotes)
                           console.print(Text(f"Added tags: '{', '.join(tags)}' to title '{title}'.", style='green'))
                        else:
                            console.print(Text(f"Tag '{tag}' already exists under the title '{title}'.", style='red'))
                        show_note(notes, [title])
            except ValueError as e:
                console.print(Text(f"Error: {e}", 'red'))
        else:
            console.print(Text(f"Note with title '{title}' not found.", style='red'))

# Function to handle command "delete-tag"
def delete_tag(notes, args):
    if len(args) < 2:
        console.print(Text(f"Missing note title or tag", style='red'))
    else:
        try:
            title = args[0]
            tag = args[1]
        except Exception as e:
            console.print(Text(f"Error: {e}", style='red'))
            return

        record = notes.find(title)
        if record:
            if record.delete_tag(tag):
                save_data(notes.data, filenameNotes)
                show_note(notes, [title])
                console.print(Text(f"Deleted tag '{tag}' from title '{title}'.", style='green'))
            else:
                console.print(Text(f"Tag '{tag}' not found under the title '{title}'.", style='red'))
        else:
            console.print(Text(f"Title '{title}' not found.", style='red'))

# Function to handle command "all"
def show_all_notes(notes):
    if not notes.data:
        console.print(Text("No notes available.", style='red'))
    else:
        notes_print_helper(notes.data.values())

# Function to handle command "show-note"
def show_note(notes, args):
    if len(args) < 1:
        console.print(Text(f"Missing message", style='red'))
    else:
        try:
            title = args[0]
        except Exception as e:
            console.print(Text(f"Error: {e}", style='red'))
            return

        record = notes.find(title)
        if record:
            notes_print_helper([record])
        else:
            console.print(Text(f"Title '{title}' not found.", style='red'))

# Function to handle command "edit-title"
def edit_title(notes, args):
    if len(args) < 2:
        console.print(Text(f"Missing title or new content", style='red'))
    else:
        try:
            title = args[0]
            new_title = args[1]
        except Exception as e:
            console.print(Text(f"Error: {e}", style='red'))
            return
        new_record = notes.find(new_title)
        if new_record:
            console.print(Text(f"New title already exsist.", style='red'))
            return
        record = notes.find(title)
        if record:
            new_note = Record(title=new_title, message=record.message, tags=[*record.tags])
            print(new_note)
            notes.add_record(new_note)
            notes.delete(title)
            save_data(notes.data, filenameNotes)
            show_note(notes,[new_title])
            console.print(Text(f"Note '{title}' updated to '{new_title}'.", style='green'))
        else:
            console.print(Text(f"Error: Note format is incorrect for '{title}'.", style='red'))
    
# Function to handle command "delete"
def delete_note(notes, args):
    if len(args) == 1:
        title = args[0]
        if notes.delete(title):
            console.print(f"[green]Deleted note {title}.[/green]")
            save_data(notes.data, filenameNotes)
        else:
            console.print(f"[red]Error: {title} not found.[/red]")
    else:
        console.print("[red]Error: Please provide a valid title.[/red]")
  
# Function to handle command "search-tag"
def search_tag(notes, args):
    search_input = args[0].lower()
    results = []
    for record in notes.data.values(): 
        for tag in record.tags:
            if search_input in tag.value.lower(): 
                results.append(record)

    if results:
        notes_print_helper(results)
    else:
        console.print(Text(f"No tags found matching '{search_input}'.", style='red'))

# Function to handle command "search-message"
def search_message(notes, args):
    print('search')
    if not args:
        console.print(Text("Please provide a search input.", style='red'))
        return
    search_input = args[0].lower() 
    results = []
    for record in notes.data.values():  
        if record.message and search_input in record.message.lower(): 
            results.append(record)

    if results:
        notes_print_helper(results)
    else:
        console.print(Text(f"No messages matching '{search_input}' found.", style='red'))

# Function-helper for printing notes
def notes_print_helper(arr):
    console.print(Text("Search Results:", style='green'))
    table = Table(
    title="📝 [bold cyan]Notes",
    title_style="bold white on blue",
    box=box.ROUNDED,
    border_style="bright_magenta",
    show_lines=True,
    padding=(0, 1)
)

    table.add_column("📂 Title", style="bold green", no_wrap=True)
    table.add_column("🔗 Tags", style="white")
    table.add_column("💡 Message", style="white")

    for item in arr:
        title = f"[bold]{item.title}[/bold]" if item.title else "[dim]—[/dim]"
        tags = ", ".join([p.value for p in item.tags]) if item.tags else "[dim]—[/dim]"
        message = f"[bold]{item.message}[/bold]" if item.message else "[dim]—[/dim]"

        table.add_row(title, tags, message)
    console.print(table)