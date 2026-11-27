"""CLI script for the practice_demo package. This will be called on the command line"""

import click

from practice_demo.practice_demo import hello_world, prime_factorize


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def practice_demo_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))

@click.command()
@click.argument("number", type=click.IntRange(min=2))
def factorize_cli(number):
    """Print the prime factorization of NUMBER."""
    factors = prime_factorize(number)
    click.echo(f"{number} = {' x '.join(map(str, factors))}")