# Student Grade Tracker Program

students = {}   # Store student names and marks

def calculate_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"

while True:
    print("\n===== STUDENT GRADE TRACKER =====")
    print("1. Add Student Mark")
    print("2. View All Students & Grades")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    # Add student
    if choice == "1":
        name = input("Enter student name: ")
        try:
            mark = float(input("Enter mark (0–100): "))
            if 0 <= mark <= 100:
                grade = calculate_grade(mark)
                students[name] = (mark, grade)
                print(f"{name}'s grade recorded successfully!")
            else:
                print("Mark must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # View students
    elif choice == "2":
        if len(students) == 0:
            print("\nNo students recorded yet.")
        else:
            print("\n--- Student Grades ---")
            for name, info in students.items():
                mark, grade = info
                print(f"{name}: {mark}% → Grade {grade}")

    # Exit
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")