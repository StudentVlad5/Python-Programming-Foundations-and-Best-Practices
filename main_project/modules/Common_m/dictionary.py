from main_project.services.address_book_manager import hello, add_contact, add_phone, add_birthday, show_all_contacts, show_phone, show_birthday, delete_contact, add_email, show_email, add_address, show_address, birthdays_all, birthdays, edit_address, edit_birthday, edit_email, edit_phone, delete_address, delete_birthday, delete_email, delete_phone, show_contact, search_contact, add_name
from main_project.services.note_manager import add_note, show_all_notes, add_tag, delete_tag, show_note, edit_title, delete_note, search_tag, search_message
from main_project.services.commands_logs import all_logs, logs_by_date, stats_by_date
from main_project.services.help_manager import help

def command_d(book, notes):
    command_d = {
            "hello": hello,
            "help": lambda _: help(),
        #  addressBook commands
            "all-contacts": lambda _: show_all_contacts(book),
            "all-birthdays": lambda _: birthdays_all(book),
            "add": lambda args: add_contact(book, args),
            "add-name": lambda args: add_name(book, args),
            "add-phone": lambda args: add_phone(book, args),
            "add-email": lambda args: add_email(book, args),
            "add-birthday": lambda args: add_birthday(book, args),
            "add-address": lambda args: add_address(book, args),
            "contact": lambda args: show_contact(book, args),
            "phone": lambda args: show_phone(book, args),
            "email": lambda args: show_email(book, args),
            "address": lambda args: show_address(book, args),
            "birthday": lambda args: show_birthday(book, args),
            "birthdays": lambda args: birthdays(book, args),
            "edit-address": lambda args: edit_address(book, args),
            "edit-birthday": lambda args: edit_birthday(book, args),
            "edit-email": lambda args: edit_email(book, args),
            "edit-phone": lambda args: edit_phone(book, args),
            "delete": lambda args: delete_contact(book, args),
            "delete-address": lambda args: delete_address(book, args),
            "delete-birthday": lambda args: delete_birthday(book, args),
            "delete-email": lambda args: delete_email(book, args),
            "delete-phone": lambda args: delete_phone(book, args),
            "search-contact": lambda args: search_contact(book, args),
            
        #  notes commands
            "all-notes": lambda _: show_all_notes(notes),
            "add-note": lambda args: add_note(notes, args),
            "add-tag": lambda args: add_tag(notes, args),
            "show-note": lambda args: show_note(notes, args),
            "edit-title": lambda args: edit_title(notes, args),
            "search-tag": lambda args: search_tag(notes, args),
            "search-message": lambda args: search_message(notes, args),
            "delete-note": lambda args: delete_note(notes, args),
            "delete-tag": lambda args: delete_tag(notes, args),
        # logs command
            "all-logs": lambda _: all_logs(),
            "logs-by-date": lambda date: logs_by_date(date),
            "stats-by-date": lambda args: stats_by_date(args),
        }
    return command_d

def command_d_keys(book=None, notes=None):
    command_d_keys=[]
    command_d = {
            "hello": hello,
        #  addressBook commands
            "all-contacts": lambda _: show_all_contacts(book),
            "all-birthdays": lambda _: birthdays_all(book),
            "add": lambda args: add_contact(book, args),
            "add-name": lambda args: add_name(book, args),
            "add-phone": lambda args: add_phone(book, args),
            "add-email": lambda args: add_email(book, args),
            "add-birthday": lambda args: add_birthday(book, args),
            "add-address": lambda args: add_address(book, args),
            "contact": lambda args: show_contact(book, args),
            "phone": lambda args: show_phone(book, args),
            "email": lambda args: show_email(book, args),
            "address": lambda args: show_address(book, args),
            "birthday": lambda args: show_birthday(book, args),
            "birthdays": lambda args: birthdays(book, args),
            "edit-address": lambda args: edit_address(book, args),
            "edit-birthday": lambda args: edit_birthday(book, args),
            "edit-email": lambda args: edit_email(book, args),
            "edit-phone": lambda args: edit_phone(book, args),
            "delete": lambda args: delete_contact(book, args),
            "delete-address": lambda args: delete_address(book, args),
            "delete-birthday": lambda args: delete_birthday(book, args),
            "delete-email": lambda args: delete_email(book, args),
            "search-contact": lambda args: search_contact(book, args),
            "delete-phone": lambda args: delete_phone(book, args),
            
        #  notes commands
            "all-notes": lambda _: show_all_notes(notes),
            "add-note": lambda args: add_note(notes, args),
            "add-tag": lambda args: add_tag(notes, args),
            "show-note": lambda args: show_note(notes, args),
            "edit-title": lambda args: edit_title(notes, args),
            "search-tag": lambda args: search_tag(notes, args),
            "search-message": lambda args: search_message(notes, args),
            "delete-note": lambda args: delete_note(notes, args),
            "delete-tag": lambda args: delete_tag(notes, args),
        # other
            "all-logs": lambda _: all_logs(),
            "logs-by-date": lambda date: logs_by_date(date),
            "stats-by-date": lambda args: stats_by_date(args),
            "help": lambda _: help(),
            "exit": None,
            "close": None

        }
    for command in command_d.keys():
        command_d_keys.append(command)
    return command_d_keys


command_list = [
    "hello",
    #  addressBook commands
    "all-contacts",
    "all-birthdays",
    "add name phone(10num) birthday email address",
    "add-name name",
    "add-phone name phone(10num)",
    "add-email name email",
    "add-birthday name birthday(dd.mm.yyyy)",
    "add-address name address",
    "contact name",
    "phone name",
    "email name",
    "address name",
    "birthday name",
    "birthdays number_of_days_from_today",
    "edit-address name new_address",
    "edit-birthday name new_birthday",
    "edit-email name old_email new_birthday",
    "edit-phone name old_phone new_phone",
    "delete name",
    "delete-address name",
    "delete-birthday name",
    "delete-email name email",
    "delete-phone name phone",
    "search-contact name",
    # notes command
    "all-notes",
    "add-note title tags",
    "add-tag title tag",
    "show-note title",
    "edit-title title new_title",
    "search-tag search_text",
    "search-message search_text",
    "delete-note title",
    "delete-tag title tag",
    # other commands
    "all-logs",
    "logs-by-date date (YYYY-MM-DD)",
    "stats-by-date date (YYYY-MM-DD)",
    "help",
    "close", 
    "exit"
]
