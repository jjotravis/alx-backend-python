#!/usr/bin/env python3
"""duck-typed annotations"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Retrieves first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
