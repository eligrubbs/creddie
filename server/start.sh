#! /usr/bin/env sh
set -e

# prestart activities

# From this line you see this script must be run from `server` directory 
# as this is the root of the uv project and has (or will have after you run this)
# the `.venv` directory of the project in it
uv run python3 creddie/prestart.py
# API startup

uv run uvicorn creddie.main:app --host 0.0.0.0 --port 8080
