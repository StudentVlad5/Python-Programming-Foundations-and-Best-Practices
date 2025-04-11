from main_project.modules.AddressBook_m.record_m import Record
from main_project.modules.Common_m.CONSTANT import filename
from main_project.services.file_manager import save_data
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()

# Function to handle command "hello"
def hello(book):
    console.print("[bold blue]How can I help you?[/bold blue]")

# Function to handle command "add"
def add_contact(book, args):
    if not args or len(args) < 1:
        console.print("[bold red]Missing name[/bold red]")
        return

    try:
        name = args[0]
        phone = args[1] if len(args) > 1 else None
        birthday = args[2] if len(args) > 2 else None
        email = args[3] if len(args) > 3 else None
        address = args[4] if len(args) > 4 else None
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        return

    record = book.find(name)
    if record:
        console.print(f"[yellow]⚠️ Contact '{name}' already exists in your book[/yellow]")
        return

    record = Record(name)

    if phone:
        try:
            record.add_phone(phone)
        except ValueError as e:
            console.print(f"[red]❌ Invalid phone:[/red] {e}")

    if email:
        try:
            record.add_email(email)
        except ValueError as e:
            console.print(f"[red]❌ Invalid email:[/red] {e}")

    if birthday:
        try:
            record.add_birthday(birthday)
        except ValueError as e:
            console.print(f"[red]❌ Invalid birthday:[/red] {e}")

    if address:
        try:
            record.add_address(address)
        except ValueError as e:
            console.print(f"[red]❌ Invalid address:[/red] {e}")

    book.add_record(record)
    save_data(book.data, filename)

    saved_phone = str(record.phones[0]) if record.phones else None
    saved_email = str(record.emails[0]) if record.emails else None
    saved_birthday = str(record.birthday) if hasattr(record, 'birthday') else None
    saved_address = str(record.address) if hasattr(record, 'address') else None

    info_lines = [f"[bold green]✅ Added contact:[/bold green] [cyan]{name}[/cyan]"]

    if saved_phone:
        info_lines.append(f"[bold]📞 Phone:[/bold] {saved_phone}")
    if saved_email:
        info_lines.append(f"[bold]✉️  Email:[/bold] {saved_email}")
    if saved_birthday:
        info_lines.append(f"[bold]🎂 Birthday:[/bold] {saved_birthday}")
    if saved_address:
        info_lines.append(f"[bold]🏠 Address:[/bold] {saved_address}")

    console.print(
        Panel.fit(
            "\n".join(info_lines),
            title="📇 [bold cyan]Contact Added[/bold cyan]",
            border_style="green"
        )
    )

def add_name(book, args):
    if not args or len(args) < 1:
        console.print("[bold red]Missing name[/bold red]")
        return

    try:
        name = args[0]
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        return

    record = book.find(name)
    if record:
        console.print(f"[yellow]⚠️ Contact '{name}' already exists in your book[/yellow]")
        return

    record = Record(name)
    book.add_record(record)
    save_data(book.data, filename)
    show_contact(book, [name])


# Function to handle command "add-phone"
def add_phone(book, args):
    if not args or len(args) < 1:
        console.print("[red]Missing name[/red]")
        return

    try:
        name = args[0]
        phone = args[1] if len(args) > 1 else None
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        return

    record = book.find(name)
    if record:
        if phone:
            try:
                if record.add_phone(phone):
                    book.add_record(record)
                    save_data(book.data, filename)
                    console.print(f"[green]Added [bold]{name}[/bold] with phone [bold]{phone}[/bold].[/green]")
                    show_contact(book, [name])
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")

# Function to handle command "add-email"
def add_email(book, args):
    if not args or len(args) < 1:
        console.print("[red]Missing name[/red]")
        return

    try:
        name = args[0]
        email = args[1] if len(args) > 1 else None
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        return

    record = book.find(name)
    if record:
        if email:
            try:
                if record.add_email(email):
                    book.add_record(record)
                    save_data(book.data, filename)
                    console.print(f"[green]Added [bold]{name}[/bold] with email [bold]{email}[/bold].[/green]")
                    show_contact(book, [name])
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")

# Function to handle command "add-birthday"
def add_birthday(book, args):
    if not args or len(args) < 1:
        console.print("[red]Missing name[/red]")
        return

    try:
        name = args[0]
        birthday = args[1] if len(args) > 1 else None
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        return 

    record = book.find(name)
    if record:
        if birthday:
            try:
                if record.add_birthday(birthday):
                    book.add_record(record)
                    save_data(book.data, filename)
                    console.print(f"[green]Added [bold]{name}[/bold] with birthday [bold]{birthday}[/bold].[/green]")
                    show_contact(book, [name])
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")

# Function to handle command "add-address"
def add_address(book, args):
    if not args or len(args) < 1:
        console.print("[red]Missing name[/red]")
        return

    try:
        name = args[0]
        address = args[1] if len(args) > 1 else None
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        return 

    record = book.find(name)
    if record:
        if address:
            try:
                if record.add_address(address):
                    book.add_record(record)
                    save_data(book.data, filename)
                    console.print(f"[green]Added [bold]{name}[/bold] with address [bold]{address}[/bold].[/green]")
                    show_contact(book, [name])
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")

# Function to handle command "all"
def show_all_contacts(book):
    table = Table(
        title="📒 [bold cyan]Address Book Contacts",
        title_style="bold white on blue",
        box=box.ROUNDED,
        border_style="bright_magenta",
        show_lines=True,
        padding=(0, 1)
    )

    table.add_column("👤 Name", style="bold green", no_wrap=True)
    table.add_column("📞 Phones", style="white")
    table.add_column("✉️  Emails", style="white")
    table.add_column("🎂 Birthday", style="white")
    table.add_column("🏠 Address", style="white")

    for record in book.data.values():
        name = f"[bold]{record.name}[/bold]" if record.name else "[dim]—[/dim]"
        phones = ", ".join([p.value for p in record.phones]) if record.phones else "[dim]—[/dim]"
        emails = ", ".join([e.value for e in record.emails]) if record.emails else "[dim]—[/dim]"
        birthday = record.birthday.value.strftime("%d.%m.%Y") if record.birthday else "[dim]—[/dim]"
        address = str(record.address) if record.address else "[dim]—[/dim]"

        table.add_row(name, phones, emails, birthday, address)

    console.print(table)

# Function to handle command "contact"
def show_contact(book, args):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)
        if record:
            print(record.show_contact())

# Function to handle command "phone"
def show_phone(book, args):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)
        if record:
            if len(record.phones) > 0:
                console.print(f"[green]Phones for [bold]{name}[/bold]: {record.show_phone()}[/green]")
            else:
                console.print(f"[red]Contact [bold]{name}[/bold]: doesn't have phones[/red]")
        else:
            console.print(f"[red]Error: [bold]{name}[/bold] not found.[/red]")

# Function to handle command "email"
def show_email(book, args):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)
        if record:
            if len(record.emails) > 0:
                console.print(f"[green]Emails for [bold]{name}[/bold]: {record.show_email()}[/green]")
            else:
                console.print(f"[red]Contact [bold]{name}[/bold]: doesn't have an email[/red]")
        else:
            console.print(f"[red]Error: [bold]{name}[/bold] not found.[/red]")

# Function to handle command "birthday"
def show_birthday(book, args):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)
        if record:
            if record.birthday:
                console.print(f"[green]Birthday for [bold]{name}[/bold]: {record.show_birthday()}[/green]")
            else:
                console.print(f"[red]Contact [bold]{name}[/bold]: doesn't have a birthday date[/red]")
        else:
            console.print(f"[red]Error: [bold]{name}[/bold] not found.[/red]")

# Function to handle command "address"
def show_address(book, args):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)
        if record:
            if record.address is not None:
                console.print(f"[green]Address for {name}: {record.address}[/green]")
            else:
                console.print(f"[red]Contact {name}: doesn't have address [/red]")
    else:
        console.print(f"[red]Error: {name} not found.[/red]")

# Function to handle command "delete"
def delete_contact(book, args):
    if len(args) == 1:
        name = args[0]
        if book.delete(name):
            console.print(f"[green]Deleted contact {name}.[/green]")
            save_data(book.data, filename)
        else:
            console.print(f"[red]Error: {name} not found.[/red]")
    else:
        console.print("[red]Error: Please provide a valid contact name.[/red]")

# Function to handle command "delete-phone"
def delete_phone(book, args):
    if len(args) == 2:
        name, phone = args[0], args[1]
        record = book.find(name)
        if record:
            if record.delete_phone(phone):
                console.print(f"[green]Deleted phone {phone} for {name}.[/green]")
                save_data(book.data, filename)
                show_contact(book, [name])
        else:
            console.print(f"[red]Error: {name} not found.[/red]")
    else:
        console.print(f"[red]Error: please add contact's name and phone.[/red]")

# Function to handle command "delete-email"
def delete_email(book, args):
    if len(args) == 2:
        name, email = args[0], args[1]
        record = book.find(name)
        if record:
            if record.delete_email(email):
                console.print(f"[green]Deleted email {email} for {name}.[/green]")
                save_data(book.data, filename)
                show_contact(book, [name])
                
        else:
            console.print(f"[red]Error: {name} not found.[/red]")
    else:
        console.print(f"[red]Error: Please provide the contact's name and email.[/red]")

# Function to handle command "delete-birthday"
def delete_birthday(book, args):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)
        if record:
            record.delete_birthday()
            console.print(f"[green]Deleted birthday for [bold]{name}[/bold].[/green]")
            save_data(book.data, filename)
            show_contact(book, [name])
        else:
            console.print(f"[red]Error: [bold]{name}[/bold] not found.[/red]")

# Function to handle command "delete-address"
def delete_address(book, args):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)
        if record:
            record.delete_address()
            console.print(f"[green]Deleted address for [bold]{name}[/bold].[/green]")
            save_data(book.data, filename)
            show_contact(book, [name])
        else:
            console.print(f"[red]Error: [bold]{name}[/bold] not found.[/red]")

# Function to handle command "edit-phone"
def edit_phone(book, args):
    if len(args) >= 3:
        name, old_phone, new_phone = args[0], args[1], args[2]
        record = book.find(name)
        if record:
            record.edit_phone(old_phone, new_phone)
            console.print(f"[green]Changed phone for [bold]{name}[/bold].[/green]")
            save_data(book.data, filename)
            show_contact(book,[name])
        else:
            console.print(f"[red]Error: [bold]{name}[/bold] not found.[/red]")
    else:
        console.print("[red]Please add correct name and two phone numbers.[/red]")

# Function to handle command "edit-email"
def edit_email(book, args):
    if len(args) >= 3:
        name, old_email, new_email = args[0], args[1], args[2]
        record = book.find(name)
        if record:
            record.edit_email(old_email, new_email)
            console.print(f"[green]Changed email for [bold]{name}[/bold].[/green]")
            save_data(book.data, filename)
            show_contact(book,[name])
        else:
            console.print(f"[red]Error: [bold]{name}[/bold] not found.[/red]")
    else:
        console.print("[red]Please add correct name and two emails.[/red]")

# Function to handle command "edit-birthday"
def edit_birthday(book, args):
    if len(args) >= 2:
        name, new_birthday = args[0], args[1]
        record = book.find(name)
        if record:
            try:
                record.edit_birthday(new_birthday)
                console.print(f"[green]Edited birthday for [bold]{name}[/bold].[/green]")
                save_data(book.data, filename)
                show_contact(book,[name])
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")
        else:
            console.print(f"[red]Error: [bold]{name}[/bold] not found.[/red]")
    else:
        console.print("[red]Please provide the name and a new birthday.[/red]")

# Function to handle command "edit-address"
def edit_address(book, args):
    if len(args) >= 2:
        name, new_address = args[0], args[1]
        record = book.find(name)
        if record:
            try:
                record.edit_address(new_address)
                console.print(f"[green]Edited address for [bold]{name}[/bold].[/green]")
                save_data(book.data, filename)
                show_contact(book,[name])
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")
        else:
            console.print(f"[red]Error: [bold]{name}[/bold] not found.[/red]")
    else:
        console.print("[red]Please provide the name and a new address.[/red]")

# Function to handle command "birthdays"
# see  birthdays [today + 7 days]
# see birthday (number of days)
def birthdays(book, args):
    if len(args) > 0 and args[0] is not None:
        days = args[0]
    else:
        days = 7
    try:
        days = int(days)
    except ValueError:
        console.print("[red]Error: Please provide a valid number of days.[/red]")
        return
    if days < 0:
        console.print("[red]Error: Please provide a positive number of days.[/red]")
        return
    upcoming = book.birthdays(days)
    
    if upcoming:
        console.print("[green]Upcoming birthdays:[/green]")
        for it in upcoming:
            console.print(f"[magenta]{it['name']}[/magenta] [yellow]on[/yellow] [magenta]{it['congratulation_date']}[/magenta]")
    else:
        console.print(f"[magenta]No upcoming birthdays in the next {days} days.[/magenta]")
        
# Function to handle command "birthdays-all"
# see all contact's birthdays 
def birthdays_all(book):
    table = Table(show_header=True, header_style="bold green")
    table.add_column("Name", style="magenta")
    table.add_column("Birthday", style="magenta")
    console.print("[green]All birthdays:[/green]")
    for record in book.data.values():
        birthday = record.show_birthday()
        table.add_row(record.name.value, birthday)
    console.print(table)

#search contact by name
def search_contact(book, args):
    if not args:
        console.print("[red]Please provide a search input.[/red]")
        return
    search_input = args[0].lower()
    results = []
    for record in book.data.values():  
        if search_input in record.name.value.lower():   
            results.append(record)
    if results:
        table = Table(
            title=f"🔍 [bold cyan]Search Results for '{search_input}'",
            title_style="bold white on dark_green",
            box=box.ROUNDED,
            border_style="bright_green",
            show_lines=True,
            padding=(0, 1)
        )

        table.add_column("👤 Name", style="bold green", no_wrap=True)
        table.add_column("📞 Phones", style="white")
        table.add_column("✉️  Emails", style="white")
        table.add_column("🎂 Birthday", style="white")
        table.add_column("🏠 Address", style="white")

        for record in results:
            name = f"[bold]{record.name}[/bold]" if record.name else "[dim]—[/dim]"
            phones = ", ".join([p.value for p in record.phones]) if record.phones else "[dim]—[/dim]"
            emails = ", ".join([e.value for e in record.emails]) if record.emails else "[dim]—[/dim]"
            birthday = record.birthday.value.strftime("%d.%m.%Y") if record.birthday else "[dim]—[/dim]"
            address = str(record.address) if record.address else "[dim]—[/dim]"

            table.add_row(name, phones, emails, birthday, address)

        console.print(table)
    else:
        console.print(f"[red]No messages found matching '{search_input}'.[/red]")