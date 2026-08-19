from collections import deque
def task_a():
    print("Task A started")

    yield

    print("Task A resumed")

    yield

    print("Task A completed")
def task_b():
    print("Task B started")

    yield

    print("Task B resumed")

    yield

    print("Task B completed")

def event_loop(tasks):
    queue = deque(tasks)

    while queue:

        task = queue.popleft()

        try:
            # Resume task until next yield
            next(task)

            # Task paused, so schedule it again
            queue.append(task)

        except StopIteration:
            # Task has completed
            pass


event_loop([
    task_a(),
    task_b()
])