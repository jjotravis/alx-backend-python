#!/usr/bin/python3
"""type-annotated function that adds a list of floats"""


def sum_list(input_list: list[float]) -> float:
    """return sum as float"""
    return sum(input_list)
