# import asyncio
# import threading
# import multiprocessing
# import time


# # ==========================================
# # I/O BOUND TASK
# # ==========================================

# def io_task():
#     # Simulates waiting for network response
#     time.sleep(1)


# async def async_io_task():
#     # Non-blocking simulated network wait
#     await asyncio.sleep(1)


# # ==========================================
# # CPU BOUND TASK
# # ==========================================

# def cpu_task():
#     total = 0

#     for i in range(3_000_000):
#         total += i * i

#     return total


# async def async_cpu_task():
#     # Deliberately CPU-heavy with no await
#     # to demonstrate why asyncio does not
#     # help CPU-bound work.
#     return cpu_task()


# # ==========================================
# # THREADING - I/O
# # ==========================================

# def threading_io():

#     threads = []

#     start = time.perf_counter()

#     for _ in range(5):

#         thread = threading.Thread(
#             target=io_task
#         )

#         threads.append(thread)

#         thread.start()

#     for thread in threads:
#         thread.join()

#     end = time.perf_counter()

#     print(
#         f"Threading I/O: "
#         f"{end - start:.2f} seconds"
#     )


# # ==========================================
# # MULTIPROCESSING - I/O
# # ==========================================

# def multiprocessing_io():

#     processes = []

#     start = time.perf_counter()

#     for _ in range(5):

#         process = multiprocessing.Process(
#             target=io_task
#         )

#         processes.append(process)

#         process.start()

#     for process in processes:
#         process.join()

#     end = time.perf_counter()

#     print(
#         f"Multiprocessing I/O: "
#         f"{end - start:.2f} seconds"
#     )


# # ==========================================
# # ASYNCIO - I/O
# # ==========================================

# async def asyncio_io():

#     start = time.perf_counter()

#     await asyncio.gather(
#         *[
#             async_io_task()
#             for _ in range(5)
#         ]
#     )

#     end = time.perf_counter()

#     print(
#         f"Asyncio I/O: "
#         f"{end - start:.2f} seconds"
#     )


# # ==========================================
# # THREADING - CPU
# # ==========================================

# def threading_cpu():

#     threads = []

#     start = time.perf_counter()

#     for _ in range(5):

#         thread = threading.Thread(
#             target=cpu_task
#         )

#         threads.append(thread)

#         thread.start()

#     for thread in threads:
#         thread.join()

#     end = time.perf_counter()

#     print(
#         f"Threading CPU: "
#         f"{end - start:.2f} seconds"
#     )


# # ==========================================
# # MULTIPROCESSING - CPU
# # ==========================================

# def multiprocessing_cpu():

#     processes = []

#     start = time.perf_counter()

#     for _ in range(5):

#         process = multiprocessing.Process(
#             target=cpu_task
#         )

#         processes.append(process)

#         process.start()

#     for process in processes:
#         process.join()

#     end = time.perf_counter()

#     print(
#         f"Multiprocessing CPU: "
#         f"{end - start:.2f} seconds"
#     )


# # ==========================================
# # ASYNCIO - CPU
# # ==========================================

# async def asyncio_cpu():

#     start = time.perf_counter()

#     await asyncio.gather(
#         *[
#             async_cpu_task()
#             for _ in range(5)
#         ]
#     )

#     end = time.perf_counter()

#     print(
#         f"Asyncio CPU: "
#         f"{end - start:.2f} seconds"
#     )


# # ==========================================
# # MAIN
# # ==========================================

# if __name__ == "__main__":

#     print("\n--- I/O BOUND ---")

#     threading_io()

#     multiprocessing_io()

#     asyncio.run(asyncio_io())


#     print("\n--- CPU BOUND ---")

#     threading_cpu()

#     multiprocessing_cpu()

#     asyncio.run(asyncio_cpu())

import asyncio
import threading
import multiprocessing
import time


# I/O-bound task
def io_task():
    time.sleep(1)


# Async I/O-bound task
async def async_io_task():
    await asyncio.sleep(1)


# CPU-bound task
def cpu_task():
    total = 0

    for i in range(3_000_000):
        total += i * i

    return total


# Async CPU-bound task
async def async_cpu_task():
    return cpu_task()


# ---------------- THREADING ----------------

def threading_io():

    threads = []

    for _ in range(5):
        thread = threading.Thread(target=io_task)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def threading_cpu():

    threads = []

    for _ in range(5):
        thread = threading.Thread(target=cpu_task)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


# ---------------- MULTIPROCESSING ----------------

def multiprocessing_io():

    processes = []

    for _ in range(5):
        process = multiprocessing.Process(target=io_task)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


def multiprocessing_cpu():

    processes = []

    for _ in range(5):
        process = multiprocessing.Process(target=cpu_task)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


# ---------------- ASYNCIO ----------------

async def asyncio_io():

    await asyncio.gather(
        async_io_task(),
        async_io_task(),
        async_io_task(),
        async_io_task(),
        async_io_task()
    )


async def asyncio_cpu():

    await asyncio.gather(
        async_cpu_task(),
        async_cpu_task(),
        async_cpu_task(),
        async_cpu_task(),
        async_cpu_task()
    )


# Run I/O examples

threading_io()
multiprocessing_io()
asyncio.run(asyncio_io())


# Run CPU examples

threading_cpu()
multiprocessing_cpu()
asyncio.run(asyncio_cpu())

