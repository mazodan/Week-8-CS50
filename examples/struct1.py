#Basic file manipulation
import cs50
import csv
from student import Student

students = []

for i in range(3):
    print("Name: ", end="")
    name = cs50.get_string()

    print("Dorm: ", end="")
    dorm = cs50.get_string()

    students.append(Student(name, dorm))

file = open("students.csv", "w")
writer = csv.writer(file)

for student in students:
    writer.writerow((student.name, student.dorm))

file.close()