import asyncio


async def task_a():
    print("Task A started")

    await asyncio.sleep(3)

    print("Task A finished")
    return "Result A"


async def task_b():
    print("Task B started")

    await asyncio.sleep(2)

    print("Task B finished")
    return "Result B"


async def main():

    # Create and schedule Tasks
    t1 = asyncio.create_task(task_a())
    t2 = asyncio.create_task(task_b())

    # Wait for their results
    result1 = await t1
    result2 = await t2

    print(result1)
    print(result2)


asyncio.run(main())