from typing import Optional

import string
import random
from random import Random
from datetime import datetime, timezone

CHARS_FOR_UUID = string.ascii_uppercase + string.digits


def get_8_digit_UUID(rdm_gen: Optional[Random] = None) -> str:
    """Return an 8 digit UUID comprised of only capital letters and digits.

    `rdm_gen`: An optional `random.Random` object to be used instead of a seedless call to a `random` function. 
    If something other than a `random.Random` object is passed, this parameter is ignored.
    """
    if isinstance(rdm_gen, Random):
        return ''.join([rdm_gen.choice(CHARS_FOR_UUID) for _ in range(8)])
    return ''.join([random.choice(CHARS_FOR_UUID) for _ in range(8)])


def utc_now() -> datetime:
    """Callable wrapper for datetime utc now function.

    Return a datetime representing the current time in the UTC timezone.
    """
    tz_aware = datetime.now(timezone.utc)
    return tz_aware
