students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        students[student_id] = {
            "Name": name,
            "Age": age,
            "Course": course
        }

        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for sid, details in students.items():
                print("---------------------------")
                print("ID:", sid)
                print("Name:", details["Name"])
                print("Age:", details["Age"])
                print("Course:", details["Course"])

    elif choice == "3":
        student_id = input("Enter Student ID to search: ")

        if student_id in students:
            print("Student Found:")
            print("ID:", student_id)
            print("Name:", students[student_id]["Name"])
            print("Age:", students[student_id]["Age"])
            print("Course:", students[student_id]["Course"])
        else:
            print("Student not found.")

    elif choice == "4":
        student_id = input("Enter Student ID to delete: ")

        if student_id in students:
            del students[student_id]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")