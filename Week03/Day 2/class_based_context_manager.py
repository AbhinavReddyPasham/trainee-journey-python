import time

class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        print("Timer Started...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.perf_counter()
        execution_time = end_time - self.start_time
        print(f"Execution Time: {execution_time:.6f} seconds")


with Timer():
    total = 0
    for i in range(1000000):
        total += i