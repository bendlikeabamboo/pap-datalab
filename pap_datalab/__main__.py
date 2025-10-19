"""
Python package for the reproducible creation and re-creation of PAP Datalab's Data
Assets.
"""

import click
import logging
from pap_datalab.utils import setup_logging
from pap_datalab import SCHEMAS, schema_registries

_logger = logging.getLogger("main")
setup_logging()


AVAILABLE_ENVIRONMENTS = {"local", "dev"}
DEBUG_LEVELS = {
    0,
    10,
    20,
    30,
    40,
    50,
}


@click.option("-d", "--debug_level", help=f"Choose from {DEBUG_LEVELS}", default=20)
@click.group
def cli(debug_level: int):
    _logger.setLevel(debug_level)


@click.option(
    "-e",
    "--environment",
    help=f"Choose between {AVAILABLE_ENVIRONMENTS}",
    required=True,
)
@cli.command
def ensure_setup(environment: str):
    """
    Ensure that the ClickHouse tables are properly setup for our notebook pipelines.
    """
    _logger.info("Running ensure-setup...")
    from pap_datalab.engine import PapDatalab
    from pap_datalab import models

    for database in SCHEMAS:
        engine = PapDatalab(environment).get_engine(database)
        _logger.info(f"Creating all tables for '{database}'...")
        for table_name, table in schema_registries[database].metadata.tables.items():
            _logger.info(f"\tCreating table in '{database}': {table_name}")

            schema_registries[database].metadata.create_all(
                engine, tables=[table], checkfirst=True
            )


if __name__ == "__main__":
    cli()
