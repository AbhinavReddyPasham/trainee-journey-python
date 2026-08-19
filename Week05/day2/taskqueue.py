import asyncio
import random
semaphore = asyncio.Semaphore(3)
async def worker(task_id):
    async with semaphore:
        print(f"Task {task_id} started")
        delay = random.randint(1, 5)
        await asyncio.sleep(delay)

        print(f"Task {task_id} finished after {delay} seconds")
async def main():
    tasks = []
    for i in range(1, 11):
        task = asyncio.create_task(worker(i))
        tasks.append(task)
    await asyncio.gather(*tasks)
asyncio.run(main())