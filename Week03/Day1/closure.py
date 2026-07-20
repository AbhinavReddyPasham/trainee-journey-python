def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
my_counter = counter()

print(my_counter())
print(my_counter())
print(my_counter())
print(my_counter())
