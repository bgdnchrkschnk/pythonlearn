import click

# First example:
@click.command()
def hello_world():
    click.echo("Hello world!")



# Second example
@click.command()
@click.option("--count", default=1, help="Number of greetings")
@click.option("--name", prompt="Your name", help="The person to greet")
def hello(count, name):
    for i in range(count):
        click.echo(f'Hello {name}!')


if __name__ == "__main__":
    hello_world()
    hello()