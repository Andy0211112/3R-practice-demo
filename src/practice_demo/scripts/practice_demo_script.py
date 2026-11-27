"""CLI script for the practice_demo package. This will be called on the command line"""

import click

from practice_demo.practice_demo import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def practice_demo_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))
