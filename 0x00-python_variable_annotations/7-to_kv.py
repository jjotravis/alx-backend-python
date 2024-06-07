#!/usr/bin/env python3
"""type-annotated function
hat takes a string k and an int OR float v as arguments and returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """Returns a tuple of string and a float"""
    return (k, float(v**2))
