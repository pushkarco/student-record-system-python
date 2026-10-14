# Student Record and Academic Management System
# Python Programming Assignment
# Name: Pushkar Shinde
# PRN: 2126UDSM1081
# Department: AIDS
# Run with: python student_management.py

# Student Record and Academic Management System
# Python Programming Assignment

students = {}

def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")

def input_number(prompt, minimum, maximum):
    while True:
        try:
            value = float(input(prompt))
            if minimum <= value <= maximum:
                return value
            print(f"Enter a value between {minimum} and {maximum}.")
        except ValueError:
            print("Please enter a valid number.")

def display_student(student):
    print("\n----- STUDENT PROFILE -----")
    print("Roll Number:", student["roll_number"][0])
    print("Registration Number:", student["registration_number"][0])
    print("Date of Birth:", student["dob"][0])
    print("Name:", student["name"])
    print("Department:", student["department"])
    print("Subjects:", ", ".join(student["subjects"]))
    print("Marks:", student["marks"])
    print("Attendance:", student["attendance"])
    print("Address:", student["contact"]["address"])
    print("Email:", student["contact"]["email"])
    print("Clubs:", ", ".join(sorted(student["clubs"])) if student["clubs"] else "None")
    print("----------------------------")

def add_student():
    print("\n=== ADD STUDENT ===")
    roll = input_non_empty("Roll number: ")

    if roll in students:
        print("Error: A student with this roll number already exists.")
        return

    registration = input_non_empty("Registration number: ")
    dob = input_non_empty("Date of birth: ")
    name = input_non_empty("Name: ")
    department = input_non_empty("Department: ")

    while True:
        try:
            n = int(input("Number of subjects: "))
            if n > 0:
                break
            print("Enter at least 1 subject.")
        except ValueError:
            print("Enter a valid whole number.")

    subjects = []
    marks = {}
    attendance = {}

    for i in range(n):
        subject = input_non_empty(f"Subject {i+1}: ")
        if subject in subjects:
            print("Duplicate subject. Please enter it again.")
            while subject in subjects:
                subject = input_non_empty(f"Subject {i+1}: ")

        subjects.append(subject)
        marks[subject] = input_number(f"Marks for {subject} (0-100): ", 0, 100)
        attendance[subject] = input_number(
            f"Attendance for {subject} (0-100): ", 0, 100
        )

    address = input_non_empty("Address: ")
    email = input_non_empty("Email ID: ")

    clubs_input = input("Student clubs (comma separated, optional): ").strip()
    clubs = {club.strip() for club in clubs_input.split(",") if club.strip()}

    student = {
        "roll_number": (roll,),
        "registration_number": (registration,),
        "dob": (dob,),
        "name": name,
        "department": department,
        "subjects": subjects,
        "marks": marks,
        "attendance": attendance,
        "contact": {
            "address": address,
            "email": email
        },
        "clubs": clubs
    }

    students[roll] = student
    print("Student added successfully.")

def search_student():
    print("\n=== SEARCH STUDENT ===")
    roll = input_non_empty("Enter roll number: ")

    if roll in students:
        display_student(students[roll])
    else:
        print("Student not found.")

def update_student():
    print("\n=== UPDATE STUDENT ===")
    roll = input_non_empty("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    student = students[roll]
    print("1. Name")
    print("2. Department")
    print("3. Address")
    print("4. Email")
    print("5. Attendance")
    print("6. Marks")

    choice = input("Choose field to update: ").strip()

    if choice == "1":
        student["name"] = input_non_empty("New name: ")
    elif choice == "2":
        student["department"] = input_non_empty("New department: ")
    elif choice == "3":
        student["contact"]["address"] = input_non_empty("New address: ")
    elif choice == "4":
        student["contact"]["email"] = input_non_empty("New email: ")
    elif choice == "5":
        subject = input_non_empty("Subject: ")
        if subject in student["attendance"]:
            student["attendance"][subject] = input_number(
                "New attendance (0-100): ", 0, 100
            )
        else:
            print("Subject not found.")
            return
    elif choice == "6":
        subject = input_non_empty("Subject: ")
        if subject in student["marks"]:
            student["marks"][subject] = input_number(
                "New marks (0-100): ", 0, 100
            )
        else:
            print("Subject not found.")
            return
    else:
        print("Invalid choice.")
        return

    print("Record updated successfully.")

def delete_student():
    print("\n=== DELETE STUDENT ===")
    roll = input_non_empty("Enter roll number: ")

    if roll in students:
        del students[roll]
        print("Student record deleted successfully.")
    else:
        print("Student not found.")

def calculate_average():
    print("\n=== CALCULATE AVERAGE ===")
    roll = input_non_empty("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    marks = students[roll]["marks"]
    average = sum(marks.values()) / len(marks)
    print(f"Average marks of {students[roll]['name']}: {average:.2f}")

def highest_scorer():
    print("\n=== HIGHEST SCORER ===")

    if not students:
        print("No student records available.")
        return

    highest_roll = None
    highest_average = -1

    for roll, student in students.items():
        average = sum(student["marks"].values()) / len(student["marks"])
        if average > highest_average:
            highest_average = average
            highest_roll = roll

    student = students[highest_roll]
    print("Highest Scorer:")
    print("Name:", student["name"])
    print("Roll Number:", highest_roll)
    print(f"Average Marks: {highest_average:.2f}")

def list_by_department():
    print("\n=== STUDENTS BY DEPARTMENT ===")
    department = input_non_empty("Enter department: ")
    found = False

    for student in students.values():
        if student["department"].lower() == department.lower():
            print(f"{student['roll_number'][0]} - {student['name']}")
            found = True

    if not found:
        print("No student found in this department.")

def count_students():
    print("\n=== STUDENT COUNT ===")
    print("Total number of students:", len(students))

def display_all():
    print("\n=== ALL STUDENT RECORDS ===")

    if not students:
        print("No records available.")
        return

    for student in students.values():
        display_student(student)

def show_unique_data():
    print("\n=== UNIQUE DATA REPORT ===")
    departments = {student["department"] for student in students.values()}
    subjects = set()

    for student in students.values():
        subjects.update(student["subjects"])

    clubs = set()
    for student in students.values():
        clubs.update(student["clubs"])

    print("Departments:", ", ".join(sorted(departments)) if departments else "None")
    print("Subjects:", ", ".join(sorted(subjects)) if subjects else "None")
    print("Clubs:", ", ".join(sorted(clubs)) if clubs else "None")

def main():
    while True:
        print("\n==========================================")
        print(" STUDENT RECORD MANAGEMENT SYSTEM")
        print("==========================================")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Calculate Average Marks")
        print("6. Find Highest Scorer")
        print("7. List Students by Department")
        print("8. Count Students")
        print("9. Display All Records")
        print("10. Unique Data Report")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            calculate_average()
        elif choice == "6":
            highest_scorer()
        elif choice == "7":
            list_by_department()
        elif choice == "8":
            count_students()
        elif choice == "9":
            display_all()
        elif choice == "10":
            show_unique_data()
        elif choice == "0":
            print("Program ended.")
            break
        else:
            print("Invalid menu choice.")

if __name__ == "__main__":
    main()
