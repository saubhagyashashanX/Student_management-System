def load_students(students):
    with open("students.txt","r") as file:
        for line in file:
            line=line.strip()
            data=line.split(",")
            student={
                "name":data[0],
                "roll":data[1],
                "age":data[2],
                "marks":data[3]
            }
            students.append(student)
    return students
    
def save_students(students):
    with open("students.txt","w") as file:
        for student in students:
            file.write(f"{student['name']},{student['roll']},{student['age']},{student['marks']}")
    