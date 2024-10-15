#!/usr/bin/env python3
"""The basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a number between 0 and max_delay"""
    delay: float = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
