'''
Solution description: the program starts with the input of the number of grades, it takes care that
user inputs corresponds to integer and accomplish value requirements, that also happens to grades' input.
To calculate rounded grades, I designed a method through residue of the grade divided by 5, because when
the residue is 1 or 2, the difference between next multiple of 5 and the grade is less than 3. In the
other hand, solution does not take care of grades above 38 to be rounded.
'''

#Author: Eng.(c) Andres Palacio Sanchez
#Date: 17/02/2023 - 5:45 p.m.
#Version: 1.0
#Language: Python 3.10

#function to determinate rounded grades
def grading_students():
    for i in range(0, len(grades)):
        if grades[i] >= 38:
            residue = grades[i] % 5
            if residue == 3: #case next multiple in +2
                grades[i] += 2
            elif residue == 4: #case next multiple in +1
                grades[i] += 1

#input number of grades
while True:
    try:
        n = int(input())
        if (1<n and n<60):
            break
        else:
            print("value is not acceptable (2 to 59)")
    except:
        print("input is not an integer")

grades = []

#grades' input
for i in range(0,n):
    while True:
        try:
            student_grade = int(input())
            if (0<student_grade and student_grade<100):
                break
            else:
                print("value is not acceptable (1 to 99)")
        except:
            print("input is not an integer")
    grades.append(student_grade)

grading_students()
print("\nrounded grades")
for i in grades:
    print(i)