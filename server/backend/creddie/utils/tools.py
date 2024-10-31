from typing import Optional

import random
from random import Random
from datetime import datetime, timezone

from ..consts import CHARS_FOR_UUID, UUID_MAX_LEN


def get_UUID(rdm_gen: Optional[Random] = None) -> str:
    """Return a `UUID_MAX_LEN` digit UUID comprised of only capital letters and digits.

    `rdm_gen`: An optional `random.Random` object to be used instead of a seedless call to a `random` function. 
    If something other than a `random.Random` object is passed, this parameter is ignored.
    """
    if isinstance(rdm_gen, Random):
        return ''.join([rdm_gen.choice(CHARS_FOR_UUID) for _ in range(UUID_MAX_LEN)])
    return ''.join([random.choice(CHARS_FOR_UUID) for _ in range(UUID_MAX_LEN)])


def utc_now() -> datetime:
    """Callable wrapper for datetime utc now function.

    Return a datetime representing the current time in the UTC timezone.
    """
    tz_aware = datetime.now(timezone.utc)
    return tz_aware
