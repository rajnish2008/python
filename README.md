# python

1 Task
####Python Grade Calculator

Description

This Python program takes a student's marks as input and determines the
grade using if, elif, and else statements.

Grade Criteria

Marks         Grade

90 or above   A
80--89        B
70--79        C
60--69        D
Below 60      F

Python Code

marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)

Explanation

1. Take input

marks = int(input("Enter your marks: "))

input() takes the marks from the user. Since input() normally
returns text, int() converts the input into an integer.

For example:

Enter your marks: 85

The variable marks will contain the integer 85.

2. Check for Grade A

if marks >= 90:
    grade = "A"

If the marks are 90 or greater, the grade is A.

Example:

95 → A
90 → A

3. Check for Grade B

elif marks >= 80:
    grade = "B"

If the first condition is false, Python checks this condition. Marks
from 80 to 89 receive B.

Example:

85 → B
80 → B

4. Check for Grade C

elif marks >= 70:
    grade = "C"

Marks from 70 to 79 receive C.

5. Check for Grade D

elif marks >= 60:
    grade = "D"

Marks from 60 to 69 receive D.

6. Grade F

else:
    grade = "F"

If none of the previous conditions is true, the marks are below 60, so
the grade is F.

How Python Checks the Conditions

Suppose the user enters 75:

marks = 75

Python checks:

75 >= 90  → False
75 >= 80  → False
75 >= 70  → True

Therefore:

grade = "C"

Python then skips the remaining elif and else blocks.

Sample Output

Enter your marks: 85
Your grade is: B



Enter your marks: 55
Your grade is: F
