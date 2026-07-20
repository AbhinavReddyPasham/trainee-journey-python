import copy

employees = [
    {
        "name": "Alice",
        "skills": ["Python", "SQL"]
    },
    {
        "name": "Bob",
        "skills": ["Java", "Spring"]
    }
]

shallow = copy.copy(employees)
deep = copy.deepcopy(employees)

print("Before Modification")
print(employees)
print(shallow)
print(deep)

print()

employees[0]["skills"].append("FastAPI")


print("After modifying Shallow Copy")
print("Original :", employees)
print("Shallow  :", shallow)
print("Deep     :", deep)