# import copy

# employees = [
#     {
#         "name": "Alice",
#         "skills": ["Python", "SQL"]
#     },
#     {
#         "name": "Bob",
#         "skills": ["Java", "Spring"]
#     }
# ]

# shallow = copy.copy(employees)
# deep = copy.deepcopy(employees)

# print("Before Modification")
# print(employees)
# print(shallow)
# print(deep)

# print()

# employees[0]["skills"].append("FastAPI")


# print("After modifying Shallow Copy")
# print("Original :", employees)
# print("Shallow  :", shallow)
# print("Deep     :", deep)

cars=[1,2,3,4,6,7,8,9,10];
print(cars[1:5])