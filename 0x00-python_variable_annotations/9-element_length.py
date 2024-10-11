#!/usr/bin/env python3
"""A smple annotated function"""


from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> \
        List[Tuple[Sequence, int]]:
    """Returns a list and a sequence"""
    return [(i, len(i)) for i in lst]
