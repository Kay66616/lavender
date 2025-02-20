# Simple Student Records Management

students = {}

while True:
    print("\n1. Add Student\n2. Update Student\n3. Show Students\n4. Average Grade\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":  # Add Student
        name = input("Enter name: ")
        age = input("Enter age: ")
        grade = float(input("Enter grade: "))
        students[name] = {"Age": age, "Grade": grade}
        print("Student added!")

    elif choice == "2":  # Update Student
        name = input("Enter name to update: ")
        if name in students:
            students[name]["Age"] = input("New age: ") or students[name]["Age"]
            students[name]["Grade"] = float(input("New grade: ") or students[name]["Grade"])
            print("Student updated!")
        else:
            print("Student not found.")

    elif choice == "3":  # Show Students
        if students:
            for name, info in students.items():
                print(f"{name}: Age {info['Age']}, Grade {info['Grade']}")
        else:
            print("No students added yet.")

    elif choice == "4":  # Average Grade
        if students:
            avg = sum(s["Grade"] for s in students.values()) / len(students)
            print(f"Average Grade: {avg:.2f}")
        else:
            print("No students to calculate average.")

    elif choice == "5":  # Exit
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
