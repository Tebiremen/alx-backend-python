#!/usr/bin/env python3
'''executing multiple coroutines at the same time with async
'''
import asyncio
from typing import list


wait_random = __import__('0-basic_async_syntax').wait_random


asyn def wait_n(n: int, max_delay: int) -> List[float]:
    '''Test file for printing the correct output of the wait_n coroutine
    '''
    delay_list = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(delay_list)
