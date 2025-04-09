from modules.AddressBook_m.addressbook_m import AddressBook
#from modules.Notes_m.note_m import Note
#from modules.Common_m.CONSTANT import filename, filenameNotes
#from modules.Common_m.dictionary import command_d
from services.file_manager import load_data, save_data

from services.address_book_manager import hello, add_contact, add_phone, add_birthday, show_all_contacts, show_phone, show_birthday, delete_contact, add_email, show_email, add_address, show_address, birthdays_all, birthdays, edit_address, edit_birthday, edit_email, edit_phone, delete_address, delete_birthday, delete_email, delete_phone
#from services.note_manager import add_note, show_all_notes, add_tag, delete_tag, show_message, edit_message, delete_note, search_tag, search_message

def main():
    filename = "testab.pkl"
    book = AddressBook()
    #notes = Note()

    loaded_contacts = load_data(book, filename)
    sorted_loaded_contacts= sorted(loaded_contacts.items(), key=lambda x: x[0])
    book.data.update(sorted_loaded_contacts)

    print("--- show_all_contacts ---")
    show_all_contacts(book)

    print("--- add contact ---")
    add_contact(book, ["Name01"])
    print("--- add contact with existing name ---")
    add_contact(book, ["Name01"])
    show_all_contacts(book)

    print("--- add phone ---")
    show_phone(book, ["Name01"])
    add_phone(book, ["Name01", "5551234567"])
    show_phone(book, ["Name01"])
    add_phone(book, ["Name01", "5550000001"])
    show_phone(book, ["Name01"])
    print("--- edit phone ---")
    edit_phone(book, ["Name01", "5551234567", "5550000022"])
    show_phone(book, ["Name01"])
    print("--- delete phone ---")
    delete_phone(book, ["Name01", "5550000001"])
    show_phone(book, ["Name01"])
    print("--- delete non-existent phone ---")
    delete_phone(book, ["Name01", "6660000001"])

    print("--- add email ---")
    add_email(book,["Name01","name01@mail.com"])
    show_email(book, ["Name01"])
    print("--- add another email ---")
    add_email(book,["Name01","name01two@mail.com"])
    show_email(book, ["Name01"])
    edit_email(book,["Name01", "name01two@mail.com","name01@mail-two.com"])
    show_email(book, ["Name01"])
    print("--- delete email ---")
    delete_email(book,["Name01","name01two@mail.com"])
    print("delete non-existent email")
    print("--- delete non-existent email ---")
    delete_email(book,["Name01","non-existent@mail.com"])

    print("--- add birthday ---")
    add_birthday(book, ["Name01", "27.06.1999"])
    show_birthday(book, ["Name01"])
    print("--- add birthday again---")
    add_birthday(book, ["Name01", "12.04.1986"])
    show_birthday(book, ["Name01"])
    print("--- edit birthday ---")
    edit_birthday(book, ["Name01", "10.04.2001"])
    show_birthday(book, ["Name01"])
    print("--- delete birthday ---")
    delete_birthday(book,["Name01"])
    show_birthday(book, ["Name01"])



    print("--- add address ---")
    add_address(book, ["Name01","USA, LA, Tree str. 987075"])
    show_address(book, ["Name01"])
    print("--- add address again ---")
    add_address(book, ["Name01","Canada, Toronto, Lake str. 387"])
    show_address(book, ["Name01"])
    print("--- edit address ---")
    edit_address(book, ["Name01","UK, London, Baker str. 221b"])
    show_address(book, ["Name01"])
    print("--- delete address ---")
    delete_address(book, ["Name01"])
    show_address(book, ["Name01"])
    print("--- delete address again ---")
    delete_address(book, ["Name01"])
    show_address(book, ["Name01"])


    print("--- show all contacts ---")
    show_all_contacts(book)

    print("--- add contacts with full info ---")
    add_contact(book,["Name02","5551234321", "11.04.1987", "name02@mail.com","Address 02"])
    add_contact(book,["Name03","5553333333", "10.04.2001", "name03@mail.com","Address 03"])
    add_contact(book,["Name03","5553333333", "29.06.2001", "name04@mail.com","Address 04"])
    add_contact(book,["Name04","5554444444", "19.07.1998", "name04@mail.com","Address 04"])
    show_all_contacts(book)

    print("--- birthdays_all(book) ---")
    birthdays_all(book)

    print("--- birthdays(book, args) ---")
    birthdays(book,["10.04.2025"])
    birthdays(book,["11.04.2025"])
    birthdays(book,["11.04.2032"])
    birthdays(book,["18.07.1998"])

    print("--- delete contact ---")
    delete_contact(book, ["Name01"])
    show_all_contacts(book)

    print("--- save data to file ---")
    save_data(book.data, filename)
    # save_data(notes.data, filenameNotes)

if __name__ == "__main__":
    main()