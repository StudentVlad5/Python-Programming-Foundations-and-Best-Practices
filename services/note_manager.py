from termcolor import colored
from modules.Notes_m.record_m import Record
from services.file_manager import save_data
from modules.Common_m.CONSTANT import filenameNotes

# Function to handle command "add"
def add_note(notes, args):
    if not args or len(args) < 1:
        print(colored(f"Missing message", 'red'))
    else:
        try:
            message = args[0]
            tags = args[1:] if len(args) > 1 else None

        except Exception as e:
            print(colored(f"Error: {e}", 'red'))
            return

        record = notes.find(message)
        if record:
            print(colored(f"You already have message {message} in your note", 'red'))
        else:
            record = Record(message)
            try:
                if tags:
                    for tag in tags:
                        record.add_tag(tag)
            except ValueError as e:
                print(colored(f"Error: {e}", 'red'))

            notes.add_record(record)
            save_data(notes.data, filenameNotes)
            print(colored(f"Added {message} with tags {tags}.", 'green'))

# Function to handle command "add-tag"
def add_tag(notes, args):
    if len(args) < 2:
        print(colored(f"Missing message or tag", 'red'))
    else:
        try:
            message = args[0]
            tag = args[1]
        except Exception as e:
            print(colored(f"Error: {e}", 'red'))
            return

        record = notes.find(message)
        if record:
            try:
                record.add_tag(tag)
                save_data(notes.data, filenameNotes)
                print(colored(f"Added tag '{tag}' to message '{message}'.", 'green'))
            except ValueError as e:
                print(colored(f"Error: {e}", 'red'))
        else:
            print(colored(f"Message '{message}' not found.", 'red'))

# Function to handle command "delete-tag"
def delete_tag(notes, args):
    if len(args) < 2:
        print(colored(f"Missing message or tag", 'red'))
    else:
        try:
            message = args[0]
            tag = args[1]
        except Exception as e:
            print(colored(f"Error: {e}", 'red'))
            return

        record = notes.find(message)
        if record:
            if record.delete_tag(tag):
                save_data(notes.data, filenameNotes)
                print(colored(f"Deleted tag '{tag}' from message '{message}'.", 'green'))
            else:
                print(colored(f"Tag '{tag}' not found in message '{message}'.", 'red'))
        else:
            print(colored(f"Message '{message}' not found.", 'red'))

# Function to handle command "all"
def show_all_notes(notes):
    if not notes.data:
        print(colored("No notes available.", 'red'))
    else:
        print(notes)

# Function to handle command "show-message"
def show_message(notes, args):
    if len(args) < 1:
        print(colored(f"Missing message", 'red'))
    else:
        try:
            message = args[0]
        except Exception as e:
            print(colored(f"Error: {e}", 'red'))
            return

        record = notes.find(message)
        if record:
            print(record)
        else:
            print(colored(f"Message '{message}' not found.", 'red'))

# Function to handle command "edit-message"
def edit_message(notes, args):
    if len(args) < 2:
        print(colored(f"Missing message or new content", 'red'))
    else:
        try:
            message = args[0]
            new_message = args[1]
        except Exception as e:
            print(colored(f"Error: {e}", 'red'))
            return
        new_record = notes.find(new_message)
        if new_record:
            print(colored(f"New message already exsist.", 'red'))
            return
        record = notes.find(message)
        if record:
            tags_str = ", ".join(tag.value for tag in record.tags)  
            if tags_str:
                print(new_message + ', ' + tags_str)
                add_note(notes, (new_message, tags_str))
                delete_note(notes, [message])
                save_data(notes.data, filenameNotes)
                print(colored(f"Message '{message}' updated to '{new_message}'.", 'green'))
        else:
            print(colored(f"Error: Message format is incorrect for '{message}'.", 'red'))


# Function to handle command "delete_note"
def delete_note(notes, args):
    if len(args) < 1:
        print(colored(f"Missing message", 'red'))
    else:
        try:
            message = args[0]
        except Exception as e:
            print(colored(f"Error: {e}", 'red'))
            return

        record = notes.find(message)
        if record:

            for tag in record.tags:
                print(colored(f"Deleting tag: {tag.value}", 'yellow'))  
                record.delete_tag(tag.value)  
            if notes.delete(message):
                save_data(notes.data, filenameNotes)
                print(colored(f"Deleted message '{message}' and its associated tags.", 'green'))
            else:
                print(colored(f"Message '{message}' could not be deleted.", 'red'))
        else:
            print(colored(f"Message '{message}' not found.", 'red'))

# Function to handle command "search-tag"
def search_tag(notes, args):
    search_input = args[0].lower()
    results = []
    for record in notes.data.values(): 
        for tag in record.tags:
            if search_input in tag.value.lower(): 
                results.append(f"Message: {record.message} Tags: {tag.value}")

    if results:
        print(colored("Search Results:", 'green'))
        for result in results:
            print(colored(result, 'magenta'))
    else:
        print(colored(f"No tags found matching '{search_input}'.", 'red'))

# Function to handle command "search-message"
def search_message(notes, args):
    if not args:
        print(colored("Please provide a search input.", 'red'))
        return
    search_input = args[0].lower() 
    results = []
    for record in notes.data.values():  
        if search_input in record.message.value.lower():   
            tags_str = " ".join(tag.value for tag in record.tags)
            results.append(f"Message: {record.message} Tags: {tags_str}")

    if results:
        print(colored("Search Results:", 'green'))
        for result in results:
            print(colored(result, 'magenta'))
    else:
        print(colored(f"No messages found matching '{search_input}'.", 'red'))