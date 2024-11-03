#! /usr/bin/env sh
set -e

# Let DB start
python creddie/db/db_prestart.py

# alembic migrations
alembic upgrade head

# add default data if not in the table
python creddie/db/initial_data.py
