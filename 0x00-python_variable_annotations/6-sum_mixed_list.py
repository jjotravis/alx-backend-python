#!/usr/bin/env python3
"""type annotated function that takes float and int
returns sum as a float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of list as a float"""
    return sum(mxd_lst)
