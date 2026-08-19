import asyncio
class FakeConnection:
    def __init__(self, id):
        self.id = id
    async def execute(self, query):
        print(f"Connection {self.id}: Executing -> {query}")
        await asyncio.sleep(3)
        print(f"Connection {self.id}: Query Completed")
class ResourcePool:
    def __init__(self, size):
        self.queue = asyncio.Queue()
        # Create fixed number of connections
        for i in range(1, size + 1):
            self.queue.put_nowait(FakeConnection(i))
    async def acquire(self):
        print("Waiting for a free connection...")
        conn = await self.queue.get()
        print(f"Connection {conn.id} Acquired")
        return conn

    async def release(self, conn):
        print(f"Connection {conn.id} Released")
        await self.queue.put(conn)
        
async def worker(task_id, pool):

    print(f"\nTask {task_id} Started")

    conn = await pool.acquire()

    try:
        await conn.execute(f"SELECT * FROM USERS -- Task {task_id}")
        print(f"Task {task_id} Finished Work")

    finally:
        await pool.release(conn)


async def main():

    # Only TWO connections
    pool = ResourcePool(2)

    tasks = [
        asyncio.create_task(worker(1, pool)),
        asyncio.create_task(worker(2, pool)),
        asyncio.create_task(worker(3, pool)),
        asyncio.create_task(worker(4, pool)),
    ]

    await asyncio.gather(*tasks)


asyncio.run(main())