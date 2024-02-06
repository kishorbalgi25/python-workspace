students = {}

def AddStudent():
    ID = input("Enter student ID: ")
    name = input("Enter student name: ")
    department = input("Enter department: ")
    skills = input("Enter skills (comma-separated): ").split(', ')
    students[ID] = {'Name': name, 'Department': department, 'Skills': skills}
    print("Student added successfully!\n")

def DisplayStudents():
    print("\nList of Students:")
    for ID, details in students.items():
        print(f"ID: {ID}, Name: {details['Name']}, Department: {details['Department']}, Skills: {details['Skills']}")
    print()

def SearchStudent():
    department = input("Enter the department to search: ")
    print(f"\nStudents in {department}:")
    c=0
    for id,details in students.items():
            if(students[id]['Department']==department):
                print(f"- ID: {id}, Name: {details['Name']}, Department: {details['Department']}, Skills: {details['Skills']}")
                c+=1
    if c==0:
        print(f"\nNo students found in {department}.\n")

def UpdateStudent():
    ID = input("Enter the student ID to update: ")
    if ID in students:
        nskills = input("Enter new skills (comma-separated): ").split(', ')
        students[ID]['Skills'] = nskills
        print("Student skills updated successfully!\n")
    else:
        print("Student not found.\n")

def RemoveStudent():
    ID = input("Enter the student ID to remove: ")
    if ID in students:
        del students[ID]
        print("Student removed from the placement system.\n")
    else:
        print("Student not found.\n")

def GenerateReports():
    department = input("Enter the department to generate placement reports: ")
    JobPos = ['QA Engineer','Staff Engineer','Software Engineer']
    print(f"\nPlacement Report for {department} Students:")
    c=0
    for id,details in students.items():
        if (students[ID]['Department']==department):
            x=len(students[id]['Skills'])+1
            post=JobPos[x]
            print(f"- {details['Name']} is eligible for {post} positions.")
            c+=1
    if c==0:
        print(f"\nNo placement report available for {department}.\n")

print("Welcome to the Student Placement System!\n")
print("1. Add Students\n2. Display Students\n3. Search for Students by Department\n4. Update Student Skills\n5. Remove Student\n6. Generate Placement Reports\n7. Exit\n")
while True:

    ch = int(input("Enter your choice: "))

    if ch == 1:
        AddStudent()
    elif ch == 2:
        DisplayStudents()
    elif ch == 3:
        SearchStudent()
    elif ch == 4:
        UpdateStudent()
    elif ch == 5:
        RemoveStudent()
    elif ch == 6:
        GenerateReports()
    elif ch == 7:
        break
