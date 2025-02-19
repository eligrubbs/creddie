#!/usr/bin/env sh

set -e

docker compose down

docker image prune -f
