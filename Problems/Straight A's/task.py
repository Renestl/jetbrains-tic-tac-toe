# put your python code here
grades = input()

A_grade = 0
all_grades = len(grades.split())

for grade in grades:
    if grade == "A":
        A_grade += 1

print(round((A_grade / all_grades), 2))
