#!/usr/bin/env python3
"""Executing multiple coroutines at the same time wtoith async"""

from typing import Callable, Coroutine, List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """Creates as many coroutines as defined by <max_delay>

    Parameters:
      n(int): the number of times to call wait_random
      max_delay(int): the delay value to pass to wait_random

    Returns:
      list of all return values of <max_delay> sorted in ascending
      order without using sort
    """
    result: List[float] = []

    for _ in range(n):
        delay: float = await wait_random(max_delay)
        result.append(delay)
    return sorted(result)
