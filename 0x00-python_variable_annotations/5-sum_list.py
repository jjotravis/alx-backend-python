#!/usr/bin/env python3
"""type-annotated function that adds a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum as float"""
    return sum(input_list)
