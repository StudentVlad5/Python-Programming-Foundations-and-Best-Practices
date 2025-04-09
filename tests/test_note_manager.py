from modules.Notes_m.note_m import Note
from services.file_manager import load_data, save_data
#from modules.Common_m.CONSTANT import filenameNotes
from services.file_manager import load_data, save_data
from services.note_manager import add_note, show_all_notes, add_tag, delete_tag, show_message, edit_message, delete_note, search_tag, search_message

def main():
    filenameNotes = "notes_test.pkl"
    notes = Note()
    notes.data.update(load_data(notes, filenameNotes))
    
    print("--- show all notes ---")
    show_all_notes(notes)

    print("--- add note ---")
    add_note(notes, ("new_message 01", "tag01"))
    add_note(notes, ("new multiline message\nline 01\nline 02\n", "multiline"))
    add_note(notes, ("new_message 02", "tag02"))
    add_note(notes, ("new_message 01 02", "tag01"))
    add_note(notes, ("new_message_03", "tag03"))

    print("--- search message ---")
    search_message(notes, "multiline")
    search_message(notes, "new_message_03")

    print("--- show_message ---")
    show_message(notes, "new_message_03")

    show_all_notes(notes)




if __name__ == "__main__":
    main()