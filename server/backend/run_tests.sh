#! /usr/bin/env sh
set -e

export MODE="testing"
# run alembic upgrades
alembic upgrade head

# Make sure dev dependencies are installed before running
pytest