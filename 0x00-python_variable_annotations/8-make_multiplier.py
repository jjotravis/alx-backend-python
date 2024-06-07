#!/usr/bin/env python3
"""type-annotated function
 that takes a float multiplier as argument
 returns a function that multiplies a float by multiplier
 """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create Multiplier function"""
    return lambda x: x * multiplier
