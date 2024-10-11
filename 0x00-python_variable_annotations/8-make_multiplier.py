#!/usr/bin/env python3
"""A smple annotated function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function"""
    return lambda num: multiplier * num
