#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async"""
from typing import Callable, Coroutine, List, Union
wait_random: Callable[[int], Coroutine[None, None, float]] = \
    __import__("0-basic_async_syntax").wait_random


def insert_at(lst: List[Union[float]], val: float) -> int:
    """returns the index in lst to insert val"""
    length: int = len(lst)
    i: int = length - 1
    if not length:
        return 0
    while i >= 0:
        if lst[i] <= val:
            break
        i -= 1
    return i + 1


async def wait_n(n: int, max_delay: int) -> List:
    """Creates as many coroutines as defined by <max_delay>

    Parameters:
      n(int): the number of times to call wait_random
      max_delay(int): the delay value to pass to wait_random

    Returns:
      list of all return values of <max_delay> sorted in ascending
      order without using sort
    """
    result: List[Union[float]] = []

    for _ in range(n):
        delay: float = await wait_random(max_delay)
        result.insert(insert_at(result, delay), delay)
    return result
