from main_project.modules.Common_m.field import Field


class Address(Field):
    def __init__(self, value):
        if value is None:
            raise ValueError("[red]Invalid address format:[/red]", f"[red]{value}[/red]")
        super().__init__(value)
        
