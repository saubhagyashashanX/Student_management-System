#Start
def show_menu():
    print("Student Management System")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

students=[]
def add_student():
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
def view_student():
    if len(students)==0:
        print("No students found.")
    else:
        for student in students:
            print(f"Name: {student['name']}, Roll: {student['roll']}, Age: {student['age']}, Marks: {student['marks']}")
def search_student():
    Id=input("Enter the roll")
    found=False 
    for student in students:
        if Id==student['roll']:
            print(f"Name: {student['name']}, Roll: {student['roll']}, Age: {student['age']}, Marks: {student['marks']}")
            found=True
    if not found:
        print("Invalid Choice")

while True:
    show_menu()
    user_input=input("Enter your choice: ")
    if user_input=="1":
        add_student()
    elif user_input=="2":
        view_student()
    elif user_input=="3":
        search_student()
    elif user_input=="4":
        print("Updating Student...")
    elif user_input=="5":
        print("Deleting Student...")
    elif user_input=="6":
        break
    else:
        print("Invalid choice. Please try again.")
    
