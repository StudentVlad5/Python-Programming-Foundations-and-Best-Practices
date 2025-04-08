from .name_m import Name
from .phone_m import Phone
from .birthday_m import Birthday
from .email_m import Email
from .address_m import Address
from services.errors_wrap import input_error
from rich.table import Table
from rich.console import Console
from rich.text import Text
from rich import box

console = Console()

class Record:
    def __init__(self, name):
        try:
            self.name = Name(name)
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")
            self.name = None
        self.phones = []
        self.emails = []
        self.birthday = None
        self.address = None
# add phone, birthday, address and email
    def add_phone(self, phone):
        try:
            valid_phone = Phone(phone) 
            self.phones.append(valid_phone)
            return 1
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")
            return 0

    @input_error
    def add_birthday(self, birthday):
        if self.birthday is not None:
            console.print(f"[red]Birthday for {self.name.value} already exists.[/red]")
            return 0
        try:
            self.birthday = Birthday(birthday)
            return 1
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")
            return 0
    
    def add_email(self, email):
        try:
            valid_email = Email(email) 
            self.emails.append(valid_email)
            return 1
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")
            return 0

    def add_address(self, address):
        try:
            self.address = address
            return 1
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")
            return 0

# delete phone, birthday, address and email
    def delete_phone(self, phone):
        try: 
            self.phones = [p for p in self.phones if p.value != phone]
            return 1
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")
            return 0

    def delete_birthday(self):
        self.birthday = None

    def delete_address(self):
        self.address = None

    def delete_email(self, email):
        try: 
            self.emails = [em for em in self.emails if em.value != email]
            return 1
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")
            return 0

# edit phone, birthday, address and email
    def edit_phone(self, old_phone, new_phone):
        try:
            for p in self.phones:
                if p.value == old_phone:
                    self.add_phone(new_phone)
                    self.delete_phone(old_phone)
                    return 1
            raise ValueError(console.print(f"[red]Phone number {old_phone} not found.[/red]"))
        
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")
            return 0

    def edit_birthday(self, new_birthday):
        try:
            self.birthday = Birthday(new_birthday)
            return 1
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")
            return 0
    
    def edit_email(self, old_email, new_email):
        try:
            for em in self.emails:
                if em.value == old_email:
                    self.add_email(new_email)
                    self.delete_email(old_email)
                    return 1
            raise ValueError(console.print(f"[red]Email {old_email} not found.[/red]"))
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")
            return 0

    def edit_address(self, new_address):
        try:
            self.address = Address(new_address)
            return 1
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")
            return 0

# show birthday, address, email, phone    
    @input_error
    def show_birthday(self):
        if self.birthday is None:
            return Text(f"Birthday for ", style="yellow") + Text(self.name.value, style="red") + Text(" is not set.", style="yellow")
        return self.birthday.value.strftime("%d.%m.%Y")

    def show_address(self):
        if self.address is None:
            return Text(f"Address for ", style="yellow") + Text(self.name.value, style="red") + Text(" is not set.", style="yellow")
        return self.address

    def show_email(self):
        if self.emails is None:
            return Text(f"Emails for ", style="yellow") + Text(self.name.value, style="red") + Text(" is not set.", style="yellow")
        return ', '.join(str(em.value) for em in self.emails)

    def show_phone(self):
        if self.phones is None:
            return Text(f"Phones for ", style="yellow") + Text(self.name.value, style="red") + Text(" is not set.", style="yellow")
        return ', '.join(str(p.value) for p in self.phones)
    
    def show_contact(self):
        if self.name is None:
            return Text("Name is not set.", style="yellow")
        table = Table(
        title=f"📇 [bold cyan]Contact Card for [green]{self.name}[/green]",
        title_style="bold white on dark_blue",
        box=box.DOUBLE_EDGE,
        border_style="bright_magenta",
        expand=False,
        padding=(0, 1)
    )

        table.add_column("📝 Field", style="bold white", justify="left", no_wrap=True)
        table.add_column("💬 Data", style="bold cyan", justify="left")

        phones_str = ", ".join([f"{str(p.value)}" for p in self.phones]) if self.phones else "[dim]— no phones —[/dim]"
        emails_str = ", ".join([f"{str(em.value)}" for em in self.emails]) if self.emails else "[dim]— no emails —[/dim]"
        birthday_str = f"{self.birthday.value.strftime('%d.%m.%Y')}" if self.birthday else "[dim]— not set —[/dim]"
        address_str = f"{self.address}" if self.address else "[dim]— not set —[/dim]"

        table.add_row("👤 Name", f"[bold]{self.name.value}[/bold]")
        table.add_row("📞 Phones", phones_str)
        table.add_row("✉️  Emails", emails_str)
        table.add_row("🎂 Birthday", birthday_str)
        table.add_row("🏠 Address", address_str)

        with console.capture() as capture:
            console.print(table)

        return capture.get()

    def __str__(self):
        birthday_str = self.birthday.value.date().strftime("%d.%m.%Y") if self.birthday else "unknown date"
        address_str = self.address if self.address else "unknown"
        phones_str = "; ".join([str(p.value) for p in self.phones]) if self.phones else "no phones"
        emails_str = "; ".join([str(em.value) for em in self.emails]) if self.emails else "no emails"
        
        contact_details = (
            Text("Contact name: ", style="light_cyan") + 
            Text(self.name.value, style="green") + 
            Text(" phones: ", style="light_cyan") + 
            Text(phones_str, style="green") + 
            Text(" birthday: ", style="light_cyan") + 
            Text(birthday_str, style="green") + 
            Text(" emails: ", style="light_cyan") + 
            Text(emails_str, style="green") + 
            Text(" address: ", style="light_cyan") + 
            Text(address_str, style="green")
        )
        return contact_details
