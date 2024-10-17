#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async"""

from asyncio import run
from time import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for
    wait_n(n, max_delay).

    Parameters:
       n(int) - number of iterations
       max_delay(int) - sleep time between each iteration

    Returns total_time / n
    """
    before: float = time()
    res: float = run(wait_n(n, max_delay))
    after: float = time()
    return (after - before)/n
