def calculate_grade(average):
    if average >= 90:
        return "S"
    elif average >= 80:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def student_details():
    print("STUDENT MARKS AND GRADE CALCULATION")
    print("-----------------------------------")

    name = input("Enter student name: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    marks = []

    for i in range(1, 4):
        mark = float(input(f"Enter marks for Subject {i}: "))

        if mark < 0 or mark > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
            return

        marks.append(mark)

    average = sum(marks) / 3
    grade = calculate_grade(average)

    print("\n----- STUDENT RESULT -----")
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Subject Marks:", marks)
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)


if __name__ == "__main__":
    student_details()