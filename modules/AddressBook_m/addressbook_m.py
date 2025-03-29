from collections import UserDict
from services.errors_wrap import input_error
from datetime import datetime, timedelta
from termcolor import colored

class AddressBook(UserDict):
    def add_record(self, record):
        if record.name is None:
            print(colored(f"Cannot add a record with an invalid name.", 'red'))
            return
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return 1
        else:
            print(f"{colored("Error: Record for",'yellow')} {colored(name, 'red')} {colored("not found.", 'yellow')}")
            return 0
    @input_error
    def birthdays(self, check_day=None):
        try: 
            check_date = datetime.strptime(check_day, "%d.%m.%Y")
        except ValueError:
            print(colored(f"The invalid data of the date {check_day}", 'red'))
            check_date = None
        today = check_date if check_date else datetime.today().date()

        search_period = 7
        upcoming_birthdays = []

        for user in self.data.values():
            if user.birthday is None:
                continue 

            birthday = user.birthday.value
            birthday_date = birthday.date()

            for delta in range(search_period + 1):
                check_date = today + timedelta(days=delta)

                if birthday_date.month == check_date.month and birthday_date.day == check_date.day:
                    upcoming_birthdays.append({
                        "name": user.name.value,
                        "congratulation_date": birthday_date.strftime("%d.%m.%Y")
                    })
                    break  

        sorted_upcoming_birthdays = sorted(upcoming_birthdays, key=lambda x: datetime.strptime(x["congratulation_date"], "%d.%m.%Y"))
        
        return sorted_upcoming_birthdays
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
