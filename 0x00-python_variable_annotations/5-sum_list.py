#!/usr/bin/env python3
"""A smple annotated function"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums up a list of floats"""
    total: float = 0
    for num in input_list:
        total += num
    return total
