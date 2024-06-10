#!/usr/bin/env python3
""" asynchronous coroutine that takes in an integer"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> 10:
    """waits for a random delay
    and eventually returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
