students = {}

def add_student():
    name = input("Enter student name: ")
    if name in students:
        print(name, "is already in the system.")
        return
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    course = input("Enter student course: ")
    students[name] = {'Age': age, 'Grade': grade, 'Course': course}
    print(name, "has been added to the system.")

def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        del students[name]
        print(name, "has been removed from the system.")
    else:
        print("Student not found.")

def view_student():
    name = input("Enter student name to view: ")
    if name in students:
        print(name, "- Age:", students[name]['Age'], "Grade:", students[name]['Grade'], "Course:", students[name]['Course'])
    else:
        print("Student not found.")

def view_all_students():
    if not students:
        print("No students in the system.")
    else:
        print("Students in the system:")
        for name, details in students.items():
            print("-", name, "Age:", details['Age'], "Grade:", details['Grade'], "Course:", details['Course'])

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add a Student")
        print("2. Remove a Student")
        print("3. View a Student")
        print("4. View All Students")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            view_student()
        elif choice == '4':
            view_all_students()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
