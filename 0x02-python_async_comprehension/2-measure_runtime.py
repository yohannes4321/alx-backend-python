#!/usr/bin/env python3
""" asyncio.gather """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Executes async_comprehension 4 times in parallel and returns runtime """
    
    start = time.perf_counter()  # Use time.perf_counter for precise measurement
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    stop = time.perf_counter()
    
    return stop - start
