import time
from contextlib import contextmanager

@contextmanager
def timer():
    print("Entering Timer Context...")

    start_time = time.perf_counter()

    try:
        yield
    finally:
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        print(f"Execution Time: {execution_time:.6f} seconds")
        print("Exiting Timer Context...")


print("Program Started")

with timer():
    print("Executing some task...")

    total = 0
    for i in range(10_000_000):
        total += i

    print("Task Completed")

print("Program Ended")