#!/usr/bin/env python3
"""Calls wait_n"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay between each call
    Returns:
        list of delays"""

    task = [task_wait_random(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(task)]
