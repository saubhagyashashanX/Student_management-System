def add_student(students):
    name=input("Enter student name: ")
    roll=input("Enter student roll number: ")
    age=input("Enter student age: ")
    marks=input("Enter student marks: ")
    student={
            "name": name,
            "roll": roll,
            "age": age,
            "marks": marks
        }
    students.append(student)
def view_student(students):
    if len(students)==0:
        print("No students found.")
    else:
        for student in students:
            print(f"Name: {student['name']}, Roll: {student['roll']}, Age: {student['age']}, Marks: {student['marks']}")
def search_student(students):
    roll=input("Enter the roll")
    found=False 
    for student in students:
        if roll==student['roll']:
            print(f"Name: {student['name']}, Roll: {student['roll']}, Age: {student['age']}, Marks: {student['marks']}")
            found=True
            break
    if not found:
        print("Invalid Choice")
def update_student(students):
    roll=input("Enter the roll")
    found=False 
    for student in students:
        if roll==student['roll']:
            n=input("Enter new name")
            student['name']=n
            a=input("Enter new age")
            student['age']=a
            m=input("Enter new marks")
            student['marks']=m
            found=True
            break
    if not found:
        print("Invalid choice")
def delete_student(students):
    roll=input("Enter the roll")
    found=False
    for student in students:
        if roll==student['roll']:
            students.remove(student)
            found=True
            break
    if not found:
        print("Invalid choice")