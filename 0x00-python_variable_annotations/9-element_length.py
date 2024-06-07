#!/usr/bin/env python3
"""type-annotate function for element length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """CLength for list of sequences"""
    return [(i, len(i)) for i in lst]
