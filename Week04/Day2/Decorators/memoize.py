def memoize(func):

    cache = {}

    def wrapper(number):

        if number in cache:
            print("Getting result from cache")
            return cache[number]

        print("Result not cached")

        result = func(number)

        cache[number] = result

        return result

    return wrapper


@memoize
def square(number):

    print("Actually calculating:", number)

    return number * number


print(square(5))

print(square(5))

print(square(10))

print(square(10))