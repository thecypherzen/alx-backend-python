#!/usr/bin/env python3
"""A smple annotated function"""


from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Sums up a list of floats"""
    return (k, v*v)
