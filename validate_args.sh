#!/bin/bash

set -e

# Use the .env file you made
source .env

# Check that $PATH_TO_CSV_FILE is correct.

# Check if PATH_TO_CSV_FILE is set
if [ -z "$PATH_TO_CSV_FILE" ]; then
    echo "Error: \$PATH_TO_CSV_FILE is not set."
    exit 1
fi
# Check if the file has a ".csv" extension
if [[ "${PATH_TO_CSV_FILE: -4}" != ".csv" ]]; then
    echo "Error: The file $PATH_TO_CSV_FILE must have a .csv extension."
    exit 1
fi

if [ ! -f $PATH_TO_CSV_FILE ]; then
    touch $PATH_TO_CSV_FILE
    echo "Empty CSV file created: $PATH_TO_CSV_FILE"
fi

echo "PATH_TO_CSV_FILE validated."
