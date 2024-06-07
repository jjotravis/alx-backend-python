#!/usr/bin/env python3
"""type annotated function that takes float and int
returns sum as a float"""
from typing import Dict


def sum_mixed_list(mxd_lst: Dict[int, float]) -> float:
    """Returns sum of list as a float"""
    return sum(mxd_lst)
