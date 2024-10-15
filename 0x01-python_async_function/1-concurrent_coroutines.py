#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async"""

from typing import Callable, Coroutine
wait_random: Callable[[int], Coroutine[None, None, float]] = \
    __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Creates as many coroutines as defined by <max_delay>

    Parameters:
      n(int): the number of times to call wait_random
      max_delay(int): the delay value to pass to wait_random

    Returns:
      list of all return values of <max_delay> sorted in ascending
      order without using sort
    """
    result: list[float] = []

    for _ in range(n):
        delay: float = await wait_random(max_delay)
    return sorted(result)