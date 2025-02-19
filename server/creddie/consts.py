"""
List of constants that Creddie uses.
"""

import pathlib
# The application is dockerized and will always store data here.
PATH_TO_CSV_FILE=pathlib.Path("./data.csv").resolve()

CATEGORIES=[
    "Dining", "Groceries", "Shopping", "Home Spending", "Transit", "Entertainment",
    "Bills", "Fees", "Gifts", "Health", "Work", "Travel", "Income"
]

# In chars
MAX_DESCRIPTION_LEN=256
MAX_PARTY_LEN=32
MAX_CURRENCY_LEN=4
