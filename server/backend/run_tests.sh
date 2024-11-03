#! /usr/bin/env sh
set -e

export MODE="development"
export DATABASE_URI="sqlite:///./TestDB.db"

# run alembic upgrades
alembic downgrade base
alembic upgrade head

# Make sure dev dependencies are installed before running
# `|| true` ensures TestDB is always cleaned up regardless of pytest pass/fail
pytest || true

rm ./TestDB.db
