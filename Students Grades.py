### Created a dictionary where the keys are student names and the values are their grades
students = {
    "John": "Grade A",
    "Alice": "Grade B",
    "Bob": "Grade C",
    "Emma": "Grade D"
}

name = input("Enter student name: ")

##Add a new student and grade.

students = {
    "John": "Grade A",
    "Alice": "Grade B",
    "Bob": "Grade C",
    "Emma": "Grade D"
}

name = input("Enter student name: ")
grade = input("Enter grade: ")

students[name] = grade

print(students)




##Update an existing student's grade.
students = {
    "John": "Grade A",
    "Alice": "Grade B",
    "Bob": "Grade C",
    "Emma": "Grade D"
}

name = input("Enter student name: ")

if name in students:
    grade = input("Enter new grade: ")
    students[name] = grade
    print("Grade updated.")
else:
    print("Student not found.")

    print(students)

##Print all student grades.
##Use a dictionary and basic operations with if / else


students = {
    "John": "Grade A",
    "Alice": "Grade B",
    "Bob": "Grade C",
    "Emma": "Grade D"
}

if students:
    print("All Student Grades:")

    for name, grade in students.items():
        print(name, ":", grade)
else:
    print("No student grades available.")
