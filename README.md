# 🧪 pap-datalab
Data laboratory for __Punan ang Patlang__ project

# 📦 Dependencies
Using `pap-datalab` requires
- up-and-running instance of
[`pap-orchestrator`](https://github.com/bendlikeabamboo/pap-orchestrator) compose stack
- installation of [`poetry`](https://python-poetry.org/)
- `.env` file containing the following (this depends on your instance of 
`pap-orchestrator`)
    - `clickhouse_username`
    - `clickhouse_password`


# ✅ Instructions
## Database Structure

1. Under the `pap-orchestrator`'s compose stack, navigate to `pap-clickhouse`
1. In `pap-clickhouse`'s Web SQL UI (by default http://localhost:18123/), run all the
SQL files under `sql/database`. This will create databases separated by data source
1. Also in `pap-clickhouse`'s Web SQL UI, run all SQL files under `sql/table`. This
will create the initial set of tables with the specified schema under each 
database (but no data yet!)
## Populating the Database
1. Run `poetry install` in the repositories root folder to install all dependencies
1. Run all notebooks under `notebooks/`

## What's next
You should now have a sort of working database stack + data. You can of course add your
data apart from the one provided, create your own database & tables, etc. But, of
course, don't forget to share! Happy crunching! 😋
