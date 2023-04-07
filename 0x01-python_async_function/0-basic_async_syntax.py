#!/usr/bin/env python3
'''The basics of task 0's module.
'''
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
