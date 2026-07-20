def add_student(name, students=[]):
    students.append(name)
    return students

print(add_student("Alice"))
print(add_student("Bob"))
print(add_student("Charlie"))