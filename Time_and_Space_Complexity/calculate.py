"""
You can estimate time complexity and space complexity in Python using some tools:

Time Complexity:
You can't directly get Big O, but you can measure how long your code takes to run using the time or timeit module.

Example using time:
"""
import time

start = time.time()
# your code here
end = time.time()
print("Time taken:", end - start)

"""
Example using timeit for more accurate results:
"""
import timeit

# Replace 'your_function' with your actual function name
# print(timeit.timeit('your_function()', setup='from __main__ import your_function', number=1000))

"""
Space Complexity:
You can check memory usage with the sys or tracemalloc module.

Example using sys:
"""
import sys

a = [1] * 1000
print("Memory used by 'a':", sys.getsizeof(a))

"""
Example using tracemalloc to track memory usage during execution:
"""
import tracemalloc

tracemalloc.start()
# your code here
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current} bytes; Peak: {peak} bytes")
tracemalloc.stop()

"""
Note: These methods give actual usage, not Big O notation. Big O is usually determined by analyzing the code logic, not by running it.
"""