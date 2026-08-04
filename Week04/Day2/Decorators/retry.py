
import time
def retry(n, delay):
    def decorator(func):
        def wrapper():
            for attempt in range(1, n + 1):
                try:
                    return func()
                except Exception as error:
                    print(f"Attempt {attempt} failed: {error}")

                    if attempt < n:
                        time.sleep(delay)
                    else:
                        raise
        return wrapper
    return decorator
attempts = 0
@retry(3, 1)
def connect():
    global attempts
    attempts += 1
    print("Connecting...", attempts)
    if attempts < 3:
        raise ValueError("Connection failed")
    return "Connected successfully"
result = connect()
print(result)

