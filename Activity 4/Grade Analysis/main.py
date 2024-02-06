from functools import reduce
grade = []
point=[]
def AddGrade():
    global grade
    grade=list(map(int,input("Enter the grades for each student (comma-separated): ").split(",")))

    print("Student grade added successfully!\n")

def DisplayGrade():
    print("\nStudents Grade :")
    print(grade)

def CalculateGradePoints():
    global point
    print("Grade Points Calculated : ")
    point=list(map(lambda x:5.0  if x==100 else (4.0 if x>=90 else (3.0 if x>=80 else (2.0 if x>=70 else (1.0 if x>=60 else 0)))) ,grade))
    print(point)

def FilterStudents():
    th=float(input("Enter the threshold grade for students needing assistance: "))
    print("Students Needing Assistance:")
    n=list(filter(lambda x: x<th ,point))
    print(n)

def CalculateAverageGrade():
    avg=reduce(lambda x,y:x+y,grade)/len(grade)
    print("Average Grade : ",avg)



print("Welcome to the Student Grade Analysis System!\n")
print("1. Enter Student Grades\n2. Display Student Grades\n3. Calculate Grade Points\n4. Filter Students Needing Assistance\n5. Calculate Average Grade\n6. Exit")
while True:

    ch = int(input("Enter your choice: "))

    if ch == 1:
        AddGrade()
    elif ch == 2:
        DisplayGrade()
    elif ch == 3:
        CalculateGradePoints()
    elif ch == 4:
        FilterStudents()
    elif ch == 5:
        CalculateAverageGrade()
    elif ch == 6:
        print("Exiting the Student Grade Analysis System. Goodbye!")
        break