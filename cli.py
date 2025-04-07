from modules.AddressBook_m.addressbook_m import AddressBook
from modules.Notes_m.note_m import Note
from modules.Common_m.CONSTANT import filename, filenameNotes
from modules.Common_m.dictionary import command_d
from services.file_manager import load_data, save_data

from services.address_book_manager import hello, add_contact, add_phone, add_birthday, show_all_contacts, show_phone, show_birthday, delete_contact, add_email, show_email, add_address, show_address, birthdays_all, birthdays, edit_address, edit_birthday, edit_email, edit_phone, delete_address, delete_birthday, delete_email, delete_phone
from services.note_manager import add_note, show_all_notes, add_tag, delete_tag, show_message, edit_message, delete_note, search_tag, search_message

def main():
    book = AddressBook()
    notes = Note()

    # load and sort data
    loaded_contacts = load_data(book, filename)
    sorted_loaded_contacts= sorted(loaded_contacts.items(), key=lambda x: x[0])
    book.data.update(sorted_loaded_contacts)
    loaded_notes = load_data(notes, filenameNotes)
    notes.data.update(loaded_notes)

    # print("filename", filename)
    # print(book)
    # print("filenameNotes", filenameNotes)
    # print(notes)

    print("contact")
    show_all_contacts(book)
    print("notes")
    show_all_notes(notes)

    print('search_tag(notes, "react")')
    search_tag(notes, "react")
    print('search_tag(notes, "tag_not_exist")')
    search_tag(notes, "tag_not_exist")

    record_Jane = book.find("Jane")
    print(record_Jane)

    show_all_contacts(book)



    # save data to file
    # save_data(book.data, filename)
    # save_data(notes.data, filenameNotes)

if __name__ == "__main__":
    main()