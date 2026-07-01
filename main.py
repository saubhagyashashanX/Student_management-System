from student import *
from fileHandler import save_students,load_students
def show_menu():
    print("Student Management System")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

students=[]
students=load_students()
while True:
    show_menu()
    user_input=input("Enter your choice: ")
    if user_input=="1":
        add_student(students)
        save_students(students)
    elif user_input=="2":
        view_student(students)
        save_students(students)
    elif user_input=="3":
        search_student(students)
        save_students(students)
    elif user_input=="4":
        update_student(students)
        save_students(students)
    elif user_input=="5":
        delete_student(students)
        save_students(students)
    elif user_input=="6":
        break
    else:
        print("Invalid choice. Please try again.")
    
