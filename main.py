#Start
while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    user_input=input("Enter your choice: ")
    if user_input=="1":
        print("Adding Student...")
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
    
