import click
import contextlib

@contextlib.contextmanager
def goodbye_message():
    try:
        yield
    finally:
        click.echo("Дякую за використання утиліти!")

@click.group()
def cli():
    """Проста утиліта."""
    pass

@cli.command()
def hello():
    """Вітається."""
    click.echo("Привіт!")

@cli.command()
@click.argument("name")
def greet(name):
    """Вітається з ім'ям."""
    click.echo(f"Привіт, {name}!")

if __name__ == "__main__":
    with goodbye_message():
        cli()