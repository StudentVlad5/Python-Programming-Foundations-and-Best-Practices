from .name_m import Name
from .phone_m import Phone
from .birthday_m import Birthday
from .email_m import Email
from .address_m import Address
from termcolor import colored
from services.errors_wrap import input_error

class Record:
    def __init__(self, name):
        try:
            self.name = Name(name)
        except ValueError as e:
            print(colored(f"Error: {e}", 'red'))
            self.name = None
        self.phones = []
        self.emails = []
        self.birthday = None
        self.address = None

    def add_phone(self, phone):
        try:
            valid_phone = Phone(phone) 
            self.phones.append(valid_phone)
            return 1
        except ValueError as e:
            print(colored(f"Error: {e}", 'red'))
            return 0

    def delete_phone(self, phone):
        try: 
            self.phones = [p for p in self.phones if p.value != phone]
            return 1
        except ValueError as e:
            print(colored(f"Error: {e}", 'red'))
            return 0

    def edit_phone(self, old_phone, new_phone):
        try:
            for p in self.phones:
                if p.value == old_phone:
                    self.add_phone(new_phone)
                    self.delete_phone(old_phone)
                    return 1
            raise ValueError(colored(f"Phone number {old_phone} not found.", 'red'))
        except ValueError as e:
            print(colored(f"Error: {e}", 'red'))
            return 0
    
    @input_error
    def add_birthday(self, birthday):
        if self.birthday is not None:
            print(colored(f"Birthday for {self.name.value} already exists.", 'red'))
            return 0
        try:
            self.birthday = Birthday(birthday)
            return 1
        except ValueError as e:
            print(colored(f"Error: {e}", 'red'))
            return 0
    
    def delete_birthday(self):
        self.birthday = None
    
    def edit_birthday(self, new_birthday):
        try:
            self.birthday = Birthday(new_birthday)
            return 1
        except ValueError as e:
            print(colored(f"Error: {e}", 'red'))
            return 0
    
    @input_error
    def show_birthday(self):
        if self.birthday is None:
            return f"{colored("Birthday for",'yellow')} {colored(self.name.value, 'red')}{colored(" is not set.", 'yellow')}"
        return self.birthday.value.strftime("%d.%m.%Y")

    def add_email(self, email):
        try:
            valid_email = Email(email) 
            self.emails.append(valid_email)
            return 1
        except ValueError as e:
            print(colored(f"Error: {e}", 'red'))
            return 0

    def delete_email(self, email):
        try: 
            self.emails = [em for em in self.emails if em.value != email]
            return 1
        except ValueError as e:
            print(colored(f"Error: {e}", 'red'))
            return 0

    def edit_email(self, old_email, new_email):
        try:
            for em in self.emails:
                if em.value == old_email:
                    self.add_email(new_email)
                    self.delete_email(old_email)
                    return 1
            raise ValueError(colored(f"Email {old_email} not found.", 'red'))
        except ValueError as e:
            print(colored(f"Error: {e}", 'red'))
            return 0
    
    def add_address(self, address):
        try:
            self.address = address
            return 1
        except ValueError as e:
            print(colored(f"Error: {e}", 'red'))
            return 0

    def delete_address(self):
        self.address = None

    def edit_address(self, new_address):
        try:
            self.address = Address(new_address)
            return 1
        except ValueError as e:
            print(colored(f"Error: {e}", 'red'))
            return 0
    
    
    def __str__(self):
        birthday_str = self.birthday.value.date().strftime("%d.%m.%Y") if self.birthday else "unknown date"
        address_str = self.address if self.address else "unknown"
        phones_str = "; ".join([str(p.value) for p in self.phones]) if self.phones else "no phones"
        emails_str = "; ".join([str(em.value) for em in self.emails]) if self.emails else "no emails"
        
        return (f"{colored('Contact name: ', 'light_cyan')}{colored(self.name.value, 'green')} "
        f"{colored('phones: ', 'light_cyan')} {colored(phones_str, 'green')} "
        f"{colored('birthday: ', 'light_cyan')} {colored(birthday_str, 'green')} "
        f"{colored('emails: ', 'light_cyan')} {colored(emails_str, 'green')} "
        f"{colored('address: ', 'light_cyan')} {colored(address_str, 'green')}")
