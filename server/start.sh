#! /usr/bin/env sh
set -e

# prestart activities

# From this line you see this script must be run only when your terminal 
# has the uv python environment activated, or your docker image has the same version of python as the project
python3 creddie/prestart.py

# API startup
uvicorn creddie.main:app --host 0.0.0.0 --port 8080
