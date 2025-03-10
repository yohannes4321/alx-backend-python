#!/usr/bin/env python3
import asyncio
import random

wait_random=__import__('0-basic_async_syntax').wait_random


async def wait_n(n,max_delay=10):
    l=await asyncio.gather(
        *tuple(map(lambda _:wait_random(max_delay),range(n)))
    )
    return l
    
 
    

