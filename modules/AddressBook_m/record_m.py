from .name_m import Name
from .phone_m import Phone
from .birthday_m import Birthday
from termcolor import colored
from services.errors_wrap import input_error

class Record:
    def __init__(self, name):
        try:
            self.name = Name(name)
        except ValueError as e:
            print(f"Error: {e}")
            self.name = None
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        try:
            valid_phone = Phone(phone) 
            self.phones.append(valid_phone)
            return 1
        except ValueError as e:
            print(f"Error: {e}")
            return 0

    def delete_phone(self, phone):
        try: 
            self.phones = [p for p in self.phones if p.value != phone]
            return 1
        except ValueError as e:
            print(f"Error: {e}")
            return 0

    def edit_phone(self, old_phone, new_phone):
        try:
            for p in self.phones:
                if p.value == old_phone:
                    self.add_phone(new_phone)
                    self.delete_phone(old_phone)
                    return 1
            raise ValueError(f"Phone number {old_phone} not found.")
        except ValueError as e:
            print(f"Error: {e}")
            return 0
    @input_error
    def add_birthday(self, birthday):
        if self.birthday is not None:
            print(f"Birthday for {self.name.value} already exists.")
            return 0
        try:
            self.birthday = Birthday(birthday)
            return 1
        except ValueError as e:
            print(f"Error: {e}")
            return 0
    
    def delete_birthday(self):
        self.birthday = None
    
    def edit_birthday(self, new_birthday):
        try:
            self.birthday = Birthday(new_birthday)
            return 1
        except ValueError as e:
            print(f"Error: {e}")
            return 0
    @input_error
    def show_birthday(self):
        if self.birthday is None:
            return f"{colored("Birthday for",'yellow')} {colored(self.name.value, 'red')}{colored(" is not set.", 'yellow')}"
        return self.birthday.value.strftime("%d.%m.%Y")

    def __str__(self):
        birthday_str = self.birthday.value.date().strftime("%d.%m.%Y") if self.birthday else "unknown date"
        phones_str = "; ".join([str(p.value) for p in self.phones]) if self.phones else "no phones"
        return f"{colored("Contact name: ",'light_cyan')} {colored(self.name.value.ljust(10), 'green')}{colored("birthday: ", 'light_cyan')}  {colored(birthday_str.ljust(15), 'green')}{colored(" phones: ",'light_cyan')} {colored(phones_str, 'green')}"
