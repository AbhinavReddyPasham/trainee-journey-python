import time
from collections.abc import Callable
from typing import Any


def timer(func: Callable[..., Any]) -> Callable[..., Any]:

    def wrapper(a: Any, b: Any) -> Any:
        start_time = time.perf_counter()

        result = func(a, b)

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print("Execution time:", execution_time)

        return result

    return wrapper


@timer
def add(a: int, b: int) -> int:
    time.sleep(1)
    return a + b