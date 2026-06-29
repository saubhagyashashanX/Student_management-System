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
    
while True:
    show_menu()
    user_input=input("Enter your choice: ")
    if user_input=="1":
        print("Adding Student...")
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
    elif user_input=="2":
        print("Viewing Student...")
    elif user_input=="3":
        print("Searching Student...")
    elif user_input=="4":
        print("Updating Student...")
    elif user_input=="5":
        print("Deleting Student...")
    elif user_input=="6":
        break
    else:
        print("Invalid choice. Please try again.")
    
