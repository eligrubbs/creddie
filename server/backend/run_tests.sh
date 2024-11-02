#! /usr/bin/env sh
set -e

export MODE="development"
export DATABASE_URI="sqlite:///./TestDB.db"

# run alembic upgrades
alembic downgrade base
alembic upgrade head

# Make sure dev dependencies are installed before running
pytest

rm ./TestDB.db
