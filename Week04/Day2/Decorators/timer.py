import time

def timer(func):

    def wrapper(a, b):

        start_time = time.perf_counter()

        result = func(a, b)

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print("Execution time:", execution_time)

        return result

    return wrapper


@timer
def add(a, b):

    time.sleep(1)

    return a + b


result = add(10, 20)

print("Result:", result)