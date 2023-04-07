#!/usr/bin/env python3
'''executing multiple coroutines at the same time with async
'''
import asyncio
from typing import list


wait_random = __import__('0-basic_async_syntax').wait_random


asyn def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executing wait_random n times.
    '''
    delay_list = await asyncio.gather(
            delay_list.append(await wait_random(max_delay))

    )
    return sorted(delay_list)
