#!/usr/bin/env python3
"""The basics of async"""

from asyncio import create_task, sleep
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Returns a number between 0 and max_delay"""
    delay: float = uniform(0, max_delay)
    await sleep(delay)
    return delay
