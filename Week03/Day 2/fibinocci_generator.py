def fibinocci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
fib=fibinocci_generator(10)
for num in fib:
    print(num)