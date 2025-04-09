from modules.Notes_m.record_m import Record
from services.file_manager import save_data
from modules.Common_m.CONSTANT import filenameNotes
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich import box

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

            notes.add_record(record)
            save_data(notes.data, filenameNotes)
            console.print(Text(f"Added '{title}'.", style='green'))

# Function to handle command "add-tag"
def add_tag(notes, args):
    if len(args) < 2:
        console.print(Text(f"Missing message or tag", style='red'))
    else:
        try:
            message = args[0]
            tag = args[1]
        except Exception as e:
            console.print(Text(f"Error: {e}", style='red'))
            return

        record = notes.find(message)
        if record:
            try:
                record.add_tag(tag)
                save_data(notes.data, filenameNotes)
                console.print(Text(f"Added tag '{tag}' to message '{message}'.", style='green'))
            except ValueError as e:
                console.print(Text(f"Error: {e}", 'red'))
        else:
            console.print(Text(f"Message '{message}' not found.", style='red'))

# Function to handle command "delete-tag"
def delete_tag(notes, args):
    if len(args) < 2:
        console.print(Text(f"Missing message or tag", style='red'))
    else:
        try:
            message = args[0]
            tag = args[1]
        except Exception as e:
            console.print(Text(f"Error: {e}", style='red'))
            return

        record = notes.find(message)
        if record:
            if record.delete_tag(tag):
                save_data(notes.data, filenameNotes)
                console.print(Text(f"Deleted tag '{tag}' from message '{message}'.", style='green'))
            else:
                console.print(Text(f"Tag '{tag}' not found in message '{message}'.", style='red'))
        else:
            console.print(Text(f"Message '{message}' not found.", style='red'))

# Function to handle command "all"
def show_all_notes(notes):
    if not notes.data:
        console.print(Text("No notes available.", style='red'))
    else:
        # print(notes.data.values())
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

    for note in notes.data.values():
        title = f"[bold]{note.title}[/bold]" if note.title else "[dim]—[/dim]"
        tags = ", ".join([p.value for p in note.tags]) if note.tags else "[dim]—[/dim]"

        table.add_row(title, tags)

    console.print(table)

# Function to handle command "show-message"
def show_message(notes, args):
    if len(args) < 1:
        console.print(Text(f"Missing message", style='red'))
    else:
        try:
            message = args[0]
        except Exception as e:
            console.print(Text(f"Error: {e}", style='red'))
            return

        record = notes.find(message)
        if record:
            print(record)
        else:
            console.print(Text(f"Message '{message}' not found.", style='red'))

# Function to handle command "edit-message"
def edit_message(notes, args):
    if len(args) < 2:
        console.print(Text(f"Missing message or new content", style='red'))
    else:
        try:
            message = args[0]
            new_message = args[1]
        except Exception as e:
            console.print(Text(f"Error: {e}", style='red'))
            return
        new_record = notes.find(new_message)
        if new_record:
            console.print(Text(f"New message already exsist.", style='red'))
            return
        record = notes.find(message)
        if record:
            tags_str = ", ".join(tag.value for tag in record.tags)  
            if tags_str:
                print(new_message + ', ' + tags_str)
                add_note(notes, (new_message, tags_str))
                delete_note(notes, [message])
                save_data(notes.data, filenameNotes)
                console.print(Text(f"Message '{message}' updated to '{new_message}'.", style='green'))
        else:
            console.print(Text(f"Error: Message format is incorrect for '{message}'.", style='red'))

# Function to handle command "delete_note"
def delete_note(notes, args):
    if len(args) < 1:
        console.print(Text(f"Missing message", style='red'))
    else:
        try:
            message = args[0]
        except Exception as e:
            console.print(Text(f"Error: {e}", style='red'))
            return

        record = notes.find(message)
        if record:

            for tag in record.tags:
                console.print(Text(f"Deleting tag: {tag.value}", style='yellow'))  
                record.delete_tag(tag.value)  
            if notes.delete(message):
                save_data(notes.data, filenameNotes)
                console.print(Text(f"Deleted message '{message}' and its associated tags.", style='green'))
            else:
                console.print(Text(f"Message '{message}' could not be deleted.", style='red'))
        else:
            console.print(Text(f"Message '{message}' not found.", style='red'))

# Function to handle command "search-tag"
def search_tag(notes, args):
    search_input = args[0].lower()
    results = []
    for record in notes.data.values(): 
        for tag in record.tags:
            if search_input in tag.value.lower(): 
                results.append(f"Message: {record.message} Tags: {tag.value}")

    if results:
        console.print(Text("Search Results:", style='green'))
        for result in results:
            console.print(Text(result, style='magenta'))
    else:
        console.print(Text(f"No tags found matching '{search_input}'.", style='red'))

# Function to handle command "search-message"
def search_message(notes, args):
    if not args:
        console.print(Text("Please provide a search input.", style='red'))
        return
    search_input = args[0].lower() 
    results = []
    for record in notes.data.values():  
        if search_input in record.message.value.lower():   
            tags_str = " ".join(tag.value for tag in record.tags)
            results.append(f"Message: {record.message} Tags: {tags_str}")

    if results:
        console.print(Text("Search Results:", style='green'))
        for result in results:
            console.print(Text(result, style='magenta'))
    else:
        console.print(Text(f"No messages found matching '{search_input}'.", style='red'))