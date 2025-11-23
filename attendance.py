attendance_records = {}

def add_or_update_attendance():
    print("\n=== MARK/UPDATE ATTENDANCE ===")
    while True:
        student_name = input("Enter student name (or type 'EXIT' to finish): ").strip()
        student_name = student_name.lower()

        if student_name == "exit":
            break

        if not student_name:
            print("Name cannot be empty.")
            continue

        while True:
            status_input = input(f"Is {student_name} 'present' or 'absent'? (p/a): ").strip().lower()
            if status_input == 'p':
                status = "present"
                attendance_records[student_name] = status
                print(f"-> Attendance marked: {student_name} is {status}.")
                break
            elif status_input == 'a':
                status = "absent"
                attendance_records[student_name] = status
                print(f"-> Attendance marked: {student_name} is {status}.")
                break
            else:
                print("Invalid input. Please enter 'p' for present or 'a' for absent.")
        
        print("-" * 30)


def display_all_attendance():
    print("\n=== CURRENT ATTENDANCE LIST ===")
    if not attendance_records:
        print("No attendance data has been entered yet.")
        return

    for name, status in attendance_records.items():
        print(f"{name.capitalize()}: {status.upper()}")


def analyze_attendance_stats():
    print("\n=== ATTENDANCE ANALYSIS ===")
    total_students = len(attendance_records)

    if total_students == 0:
        print("Cannot perform analysis. No students in the record.")
        return

    present_count = list(attendance_records.values()).count("present")
    absent_count = total_students - present_count

    if total_students > 0:
        present_percentage = (present_count / total_students) * 100
    else:
        present_percentage = 0.0

    print("--- Summary ---")
    print(f"Total Students Count: {total_students}")
    print(f"Students Present: {present_count}")
    print(f"Students Absent: {absent_count}")
    print(f"Presentation Percentage: {present_percentage:.2f}%")
    print("---------------")


def student_attendance_system():
    while True:
        print("\n==============================")
        print("ATTENDANCE MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Mark/Update Attendance")
        print("2. View All Attendance")
        print("3. Analyze Attendance")
        print("4. Exit System")
        print("------------------------------")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_or_update_attendance()
        elif choice == "2":
            display_all_attendance()
        elif choice == "3":
            analyze_attendance_stats()
        elif choice == "4":
            print("\nExiting the system. Goodbye!")
            break
        else:
            print("\n*** ERROR: Invalid choice. Please select a number from 1 to 4. ***")

student_attendance_system()
