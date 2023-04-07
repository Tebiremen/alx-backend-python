#!/usr/bin/env python3
'''Run time for four parallel comprehensions.
'''
import asyncio
import time
from importlib import import_module as using


com = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executes async_comprehension 4 times and measures the
    total execution time.
    '''
    start_time = time.time()
    await asyncio.gather(comp(), comp(), comp(), comp())
    return time.time() - start_time
