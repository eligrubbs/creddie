#!/usr/bin/env sh

set -e

./stop.sh

./validate_args.sh

docker compose up --build -d
