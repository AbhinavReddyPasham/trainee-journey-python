class Fibonacci:
    def __init__(self, n: int) -> None:
        self.n: int = n
        self.a: int = 0
        self.b: int = 1
        self.count: int = 0

    def __iter__(self) -> "Fibonacci":
        return self

    def __next__(self) -> int:
        if self.count >= self.n:
            raise StopIteration

        value: int = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1

        return value


fib = Fibonacci(10)

for num in fib:
    print(num)