"""
Python package for the reproducible creation and re-creation of PAP Datalab's Data
Assets.
"""

import click

AVAILABLE_ENVIRONMENTS = {"local", "dev"}


@click.group
def cli():
    pass


@click.option("--environment", help=f"Choose between {AVAILABLE_ENVIRONMENTS}")
@cli.command
def ensure_setup(environment: str):
    """
    Ensure that the ClickHouse tables are properly setup for our notebook pipelines.
    """
    click.echo("Running ensure setup...")


if __name__ == "__main__":
    cli()
