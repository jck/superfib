import click

from .superfib import superfib

@click.command()
@click.argument('n', type=click.INT)
def main(n):
    superfib(n)
