from functools import reduce


list=[1,2,34,5]

result = reduce(lambda x, y: x if x > y else y, list)
print(result)