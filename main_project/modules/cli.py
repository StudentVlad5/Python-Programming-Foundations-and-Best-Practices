import click
import contextlib
from modules.AddressBook_m.addressbook_m import AddressBook
#from modules.Notes_m.note_m import Note
from modules.Common_m.CONSTANT import filename, filenameNotes
#from modules.Common_m.dictionary import command_d
from services.file_manager import load_data, save_data

from services.address_book_manager import hello, add_contact, add_phone, add_birthday, show_all_contacts, show_phone, show_birthday, delete_contact, add_email, show_email, add_address, show_address, birthdays_all, birthdays, edit_address, edit_birthday, edit_email, edit_phone, delete_address, delete_birthday, delete_email, delete_phone, show_contact
from services.note_manager import add_note, show_all_notes, add_tag, delete_tag, show_note, delete_note, search_tag, search_message

book = AddressBook()
# notes = Note()

@contextlib.contextmanager
def before_exit():
    try:
        yield
    finally:
        # click.echo("Save data and exit")
        save_data(book.data, filename)
        # save_data(notes.data, filenameNotes)

@click.group()
def cli():
    """Проста утиліта для керування адресною книгою та нотатками."""
    pass

@cli.command()
def hello_cmd():
    """Вітається з користувачем."""
    hello()

@cli.command("all-contacts")
def all_contacts_cmd():
    """Показати всі контакти."""
    show_all_contacts(book)

@cli.command("all-birthdays")
def all_birthdays_cmd():
    """Показати всі дні народження."""
    birthdays_all(book)

@cli.command()
@click.argument("name")
@click.argument("phone")
@click.argument("birthday")
@click.argument("email")
@click.argument("address")
def add(name, phone, birthday, email, address):
    """Додати новий контакт."""
    add_contact(book, [name, phone, birthday, email, address])

@cli.command("add-phone")
@click.argument("name")
@click.argument("phone")
def add_phone_cmd(name, phone):
    """Додати телефон до існуючого контакту."""
    add_phone(book, [name, phone])

@cli.command("add-email")
@click.argument("name")
@click.argument("email")
def add_email_cmd(name, email):
    """Додати email до існуючого контакту."""
    add_email(book, [name, email])

@cli.command("add-birthday")
@click.argument("name")
@click.argument("birthday")
def add_birthday_cmd(name, birthday):
    """Додати день народження до існуючого контакту."""
    add_birthday(book, [name, birthday])

@cli.command("add-address")
@click.argument("name")
@click.argument("address")
def add_address_cmd(name, address):
    """Додати адресу до існуючого контакту."""
    add_address(book, [name, address])

@cli.command()
@click.argument("name")
def contact(name):
    """Показати інформацію про контакт."""
    show_contact(book, [name])

@cli.command()
@click.argument("name")
def phone(name):
    """Показати телефон контакту."""
    show_phone(book, [name])

@cli.command()
@click.argument("name")
def email(name):
    """Показати email контакту."""
    show_email(book, [name])

@cli.command()
@click.argument("name")
def address(name):
    """Показати адресу контакту."""
    show_address(book, [name])

@cli.command()
@click.argument("name")
def birthday_cmd(name):
    """Показати день народження контакту."""
    show_birthday(book, [name])

@cli.command()
@click.argument("date")
def birthdays_cmd(date):
    """Показати дні народження на задану дату."""
    birthdays(book, [date])

@cli.command("edit-address")
@click.argument("name")
@click.argument("new_address")
def edit_address_cmd(name, new_address):
    """Редагувати адресу контакту."""
    edit_address(book, [name, new_address])

@cli.command("edit-birthday")
@click.argument("name")
@click.argument("new_birthday")
def edit_birthday_cmd(name, new_birthday):
    """Редагувати день народження контакту."""
    edit_birthday(book, [name, new_birthday])

@cli.command("edit-email")
@click.argument("name")
@click.argument("old_email")
@click.argument("new_email")
def edit_email_cmd(name, old_email, new_email):
    """Редагувати email контакту."""
    edit_email(book, [name, old_email, new_email])

@cli.command("edit-phone")
@click.argument("name")
@click.argument("old_phone")
@click.argument("new_phone")
def edit_phone_cmd(name, old_phone, new_phone):
    """Редагувати телефон контакту."""
    edit_phone(book, [name, old_phone, new_phone])

@cli.command()
@click.argument("name")
def delete_cmd(name):
    """Видалити контакт."""
    delete_contact(book, [name])

@cli.command("delete-address")
@click.argument("name")
def delete_address_cmd(name):
    """Видалити адресу контакту."""
    delete_address(book, [name])

@cli.command("delete-birthday")
@click.argument("name")
def delete_birthday_cmd(name):
    """Видалити день народження контакту."""
    delete_birthday(book, [name])


def main():
    loaded_contacts = load_data(book, filename)
    sorted_loaded_contacts= sorted(loaded_contacts.items(), key=lambda x: x[0])
    book.data.update(sorted_loaded_contacts)

    with before_exit():
        cli()

    print("--- save data ---")
    save_data(book.data, filename)
    # save_data(notes.data, filenameNotes)

if __name__ == "__main__":
    main()