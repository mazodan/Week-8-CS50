import cs50
from student import Student

students = []

for i in range(3):
    print("Name: ", end="")
    name = cs50.get_string()

    print("Dorm: ", end="")
    dorm = cs50.get_string()

    students.append(Student(name, dorm))

for student in students:
    print("name: {}".format(student.name))
    print("dorm: {}".format(student.dorm))
    print()