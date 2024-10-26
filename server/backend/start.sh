#! /usr/bin/env sh
set -e

uvicorn creddie.main:app --host 0.0.0.0 --port 8080