"""
This file acts as a single point of truth for various fields.

DO NOT change these until you check every place where the variables you
plan to change are used, so you can understand the effects.
"""
import string

# The version must be changed manually here.
API_VERSION = "0.1.0"

# UUID
UUID_MAX_LEN=8
CHARS_FOR_UUID = string.ascii_uppercase + string.digits

# Category Table
CATEGORY_MAX_NAME_LEN=32

#Transaction Table
TBL_MAX_PARTY_LEN=64
TBL_MAX_CURRENCY_LEN=4
TBL_AMOUNT_DECIMAL_POINTS=2
TBL_MAX_DESC_LEN=256