#!/usr/bin/env python3
"""Multiple Coroutines"""

import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for n random delays,
    each up to max_delay seconds, and returns a sorted list of these delays.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay value in seconds.

    Returns:
        List[float]: A sorted list of n float values representing the delays.
    """

    wait_time = await asyncio.gather(
        *(wait_random(max_delay) for _ in range(n)))
    return sorted(wait_time)
