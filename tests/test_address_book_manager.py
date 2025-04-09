# test_addressbook_manager.py

import sys
import os
import pytest
from io import StringIO
from unittest.mock import patch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from modules.AddressBook_m.addressbook_m import AddressBook
from modules.Common_m.CONSTANT import filename  # Хоча filename тут не використовується в тестах
from services.file_manager import load_data, save_data  # save_data тут не використовується в тестах

from services.address_book_manager import (
    hello, add_contact, add_phone, add_birthday, show_all_contacts, show_phone, show_birthday,
    delete_contact, add_email, show_email, add_address, show_address, birthdays_all, birthdays,
    edit_address, edit_birthday, edit_email, edit_phone, delete_address, delete_birthday,
    delete_email, delete_phone
)

@pytest.fixture
def address_book():
    book = AddressBook()
    return book

def test_hello_output(address_book, capsys):
    hello(address_book)
    captured = capsys.readouterr()
    assert "How can I help you?" in captured.out

def test_show_all_contacts_empty(address_book, capsys):
    show_all_contacts(address_book)
    captured = capsys.readouterr()
    assert "No contacts in the address book." in captured.out

def test_birthdays_all_empty(address_book, capsys):
    birthdays_all(address_book)
    captured = capsys.readouterr()
    assert "No contacts with birthdays in the address book." in captured.out

def test_add_contact(address_book):
    add_contact(address_book, ["Name01"])
    assert "Name01" in address_book.data

def test_add_existing_contact(address_book, capsys):
    add_contact(address_book, ["Name01"])
    add_contact(address_book, ["Name01"])
    captured = capsys.readouterr()
    assert "Contact Name01 already exists." in captured.out

def test_add_contact_full_info(address_book):
    add_contact(address_book, ["Name02", "5551234321", "11.04.1987", "name02@mail.com", "Address 02"])
    assert "Name02" in address_book.data
    assert address_book.data["Name02"].phones[0].value == "5551234321"
    assert address_book.data["Name02"].birthday.value == "1987-04-11"
    assert address_book.data["Name02"].emails[0].value == "name02@mail.com"
    assert address_book.data["Name02"].address.value == "Address 02"

def test_add_phone(address_book, capsys):
    add_contact(address_book, ["Name01"])
    add_phone(address_book, ["Name01", "5551234567"])
    assert address_book.data["Name01"].phones[0].value == "5551234567"

def test_add_blank_phone(address_book, capsys):
    add_contact(address_book, ["Name01"])
    add_phone(address_book, ["Name01", ""])
    captured = capsys.readouterr()
    assert "Invalid phone number format." in captured.out

def test_add_second_phone(address_book):
    add_contact(address_book, ["Name01"])
    add_phone(address_book, ["Name01", "5551234567"])
    add_phone(address_book, ["Name01", "5550000001"])
    assert len(address_book.data["Name01"].phones) == 2
    assert "5550000001" in [p.value for p in address_book.data["Name01"].phones]

@pytest.mark.parametrize("invalid_phone", ["asdfghjkls", "911", "1234567890123"])
def test_add_invalid_phone(address_book, capsys, invalid_phone):
    add_contact(address_book, ["Name01"])
    add_phone(address_book, ["Name01", invalid_phone])
    captured = capsys.readouterr()
    assert "Invalid phone number format." in captured.out

def test_show_phone(address_book, capsys):
    add_contact(address_book, ["Name01", "5551234567"])
    show_phone(address_book, ["Name01"])
    captured = capsys.readouterr()
    assert "5551234567" in captured.out

def test_edit_phone(address_book, capsys):
    add_contact(address_book, ["Name01", "5551234567"])
    edit_phone(address_book, ["Name01", "5551234567", "5550000022"])
    assert address_book.data["Name01"].phones[0].value == "5550000022"

def test_edit_phone_non_existent_contact(address_book, capsys):
    edit_phone(address_book, ["NoName", "5551234567", "5550000022"])
    captured = capsys.readouterr()
    assert "Contact NoName not found." in captured.out

def test_edit_non_existent_phone(address_book, capsys):
    add_contact(address_book, ["Name01", "1111111111"])
    edit_phone(address_book, ["Name01", "0000000000", "5550000022"])
    captured = capsys.readouterr()
    assert "Phone number 0000000000 not found for Name01." in captured.out

@pytest.mark.parametrize("invalid_phone", ["asdfghjkls", "911", "1234567890123", ""])
def test_edit_invalid_phone(address_book, capsys, invalid_phone):
    add_contact(address_book, ["Name01", "1111111111"])
    edit_phone(address_book, ["Name01", "1111111111", invalid_phone])
    captured = capsys.readouterr()
    assert "Invalid new phone number format." in captured.out

def test_delete_phone(address_book, capsys):
    add_contact(address_book, ["Name01", "5550000001"])
    delete_phone(address_book, ["Name01", "5550000001"])
    assert not address_book.data["Name01"].phones

def test_delete_non_existent_phone(address_book, capsys):
    add_contact(address_book, ["Name01", "5550000001"])
    delete_phone(address_book, ["Name01", "6660000001"])
    captured = capsys.readouterr()
    assert "Phone number 6660000001 not found for Name01." in captured.out

def test_delete_phone_non_existent_contact(address_book, capsys):
    delete_phone(address_book, ["NoName", "5550000001"])
    captured = capsys.readouterr()
    assert "Contact NoName not found." in captured.out

@pytest.mark.parametrize("invalid_phone", ["", "5550000001121", "911", "asdfghjklp"])
def test_delete_invalid_phone_input(address_book, capsys, invalid_phone):
    add_contact(address_book, ["Name01", "1234567890"])
    delete_phone(address_book, ["Name01", invalid_phone])
    captured = capsys.readouterr()
    if invalid_phone:
        assert f"Phone number {invalid_phone} not found for Name01." in captured.out
    else:
        assert "Please provide a phone number to delete." in captured.out

def test_add_email(address_book):
    add_contact(address_book, ["Name01"])
    add_email(address_book, ["Name01", "name01@mail.com"])
    assert "name01@mail.com" in [e.value for e in address_book.data["Name01"].emails]

def test_add_another_email(address_book):
    add_contact(address_book, ["Name01"])
    add_email(address_book, ["Name01", "name01@mail.com"])
    add_email(address_book, ["Name01", "name01two@mail.com"])
    assert len(address_book.data["Name01"].emails) == 2
    assert "name01two@mail.com" in [e.value for e in address_book.data["Name01"].emails]

def test_add_email_non_existent_contact(address_book, capsys):
    add_email(address_book, ["NoName", "name01two@mail.com"])
    captured = capsys.readouterr()
    assert "Contact NoName not found." in captured.out

def test_edit_email(address_book):
    add_contact(address_book, ["Name01"])
    add_email(address_book, ["Name01", "name01two@mail.com"])
    edit_email(address_book, ["Name01", "name01two@mail.com", "name01@mail-two.com"])
    assert "name01@mail-two.com" in [e.value for e in address_book.data["Name01"].emails]
    assert "name01two@mail.com" not in [e.value for e in address_book.data["Name01"].emails]

def test_show_email(address_book, capsys):
    add_contact(address_book, ["Name01"])
    add_email(address_book, ["Name01", "name01@mail.com"])
    show_email(address_book, ["Name01"])
    captured = capsys.readouterr()
    assert "name01@mail.com" in captured.out

def test_delete_email(address_book):
    add_contact(address_book, ["Name01"])
    add_email(address_book, ["Name01", "name01two@mail.com"])
    delete_email(address_book, ["Name01", "name01two@mail.com"])
    assert not address_book.data["Name01"].emails

def test_delete_non_existent_email(address_book, capsys):
    add_contact(address_book, ["Name01"])
    add_email(address_book, ["Name01", "name01@mail.com"])
    delete_email(address_book, ["Name01", "non-existent@mail.com"])
    captured = capsys.readouterr()
    assert "Email non-existent@mail.com not found for Name01." in captured.out

def test_add_birthday(address_book):
    add_contact(address_book, ["Name01"])
    add_birthday(address_book, ["Name01", "27.06.1999"])
    assert address_book.data["Name01"].birthday.value == "1999-06-27"

def test_add_birthday_again(address_book, capsys):
    add_contact(address_book, ["Name01"])
    add_birthday(address_book, ["Name01", "27.06.1999"])
    add_birthday(address_book, ["Name01", "12.04.1986"])
    captured = capsys.readouterr()
    assert "Birthday already exists for Name01. Use 'edit birthday' to change it." in captured.out
    assert address_book.data["Name01"].birthday.value == "1999-06-27" # Перевіряємо, що перше значення не змінилося

def test_show_birthday(address_book, capsys):
    add_contact(address_book, ["Name01"])
    add_birthday(address_book, ["Name01", "27.06.1999"])
    show_birthday(address_book, ["Name01"])
    captured = capsys.readouterr()
    assert "27.06.1999" in captured.out

def test_edit_birthday(address_book):
    add_contact(address_book, ["Name01"])
    add_birthday(address_book, ["Name01", "27.06.1999"])
    edit_birthday(address_book, ["Name01", "10.04.2001"])
    assert address_book.data["Name01"].birthday.value == "2001-04-10"

def test_delete_birthday(address_book):
    add_contact(address_book, ["Name01"])
    add_birthday(address_book, ["Name01", "27.06.1999"])
    delete_birthday(address_book, ["Name01"])
    assert address_book.data["Name01"].birthday is None

def test_show_birthday_not_set(address_book, capsys):
    add_contact(address_book, ["Name01"])
    show_birthday(address_book, ["Name01"])
    captured = capsys.readouterr()
    assert "Birthday is not set for Name01." in captured.out

def test_add_address(address_book):
    add_contact(address_book, ["Name01"])
    add_address(address_book, ["Name01", "USA, LA, Tree str. 987075"])
    assert address_book.data["Name01"].address.value == "USA, LA, Tree str. 987075"

def test_add_address_again(address_book):
    add_contact(address_book, ["Name01"])
    add_address(address_book, ["Name01", "USA, LA, Tree str. 987075"])
    add_address(address_book, ["Name01", "Canada, Toronto, Lake str. 387"])
    assert address_book.data["Name01"].address.value == "Canada, Toronto, Lake str. 387"

def test_show_address(address_book, capsys):
    add_contact(address_book, ["Name01"])
    add_address(address_book, ["Name01", "UK, London, Baker str. 221b"])
    show_address(address_book, ["Name01"])
    captured = capsys.readouterr()
    assert "UK, London, Baker str. 221b" in captured.out

def test_edit_address(address_book):
    add_contact(address_book, ["Name01"])
    add_address(address_book, ["Name01", "USA, LA, Tree str. 987075"])
    edit_address(address_book, ["Name01", "UK, London, Baker str. 221b"])
    assert address_book.data["Name01"].address.value == "UK, London, Baker str. 221b"

