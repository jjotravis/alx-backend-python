#!/usr/bin/env python3
""" asynchronous coroutine that takes in an integer"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random amount of time
    and then returns the actual delay time.
    
    Args:
        max_delay (int): The maximum number of seconds to wait. Default is 10.
    
    Returns:
        float: The actual number of seconds the function waited."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
