def add_student(students):
    """Adds a new student (name + marks) to the students list."""
    name = input("Enter student name: ")
    marks = enter_marks()
    students.append({"name": name, "marks": marks})


def enter_marks():
    """Asks how many subjects, then collects marks for each. Returns a list of marks."""
    num_subjects = int(input("How many subjects? "))
    marks = []
    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)
    return marks


def calculate_sum(marks):
    """Adds up marks manually, without using sum()."""
    total = 0
    for mark in marks:
        total = total + mark
    return total


def calculate_average(marks):
    """Average = sum / count."""
    total = calculate_sum(marks)
    return total / len(marks)


def pass_or_fail(average, passing_marks=40):
    """Returns 'Pass' if average meets the passing criteria, else 'Fail'."""
    if average >= passing_marks:
        return "Pass"
    else:
        return "Fail"


def find_highest(students):
    """Finds the student with the highest average marks."""
    top_student = students[0]
    top_average = calculate_average(top_student["marks"])

    for student in students:
        avg = calculate_average(student["marks"])
        if avg > top_average:
            top_average = avg
            top_student = student

    return top_student, top_average


def find_lowest(students):
    """Finds the student with the lowest average marks."""
    bottom_student = students[0]
    bottom_average = calculate_average(bottom_student["marks"])

    for student in students:
        avg = calculate_average(student["marks"])
        if avg < bottom_average:
            bottom_average = avg
            bottom_student = student

    return bottom_student, bottom_average


def display_results(students):
    """Prints each student's marks, average, and pass/fail status."""
    print("\n--- Student Results ---")
    for student in students:
        avg = calculate_average(student["marks"])
        result = pass_or_fail(avg)
        print(f"Name: {student['name']}")
        print(f"  Marks: {student['marks']}")
        print(f"  Average: {avg:.2f}")
        print(f"  Result: {result}")


def display_summary(students):
    """Prints the highest and lowest scoring students."""
    top_student, top_avg = find_highest(students)
    bottom_student, bottom_avg = find_lowest(students)

    print("\n--- Summary ---")
    print(f"Highest: {top_student['name']} (Average: {top_avg:.2f})")
    print(f"Lowest: {bottom_student['name']} (Average: {bottom_avg:.2f})")


def main():
    students = []

    while True:
        add_student(students)
        another = input("Add another student? (yes/no): ").strip().lower()
        if another != "yes":
            break

    display_results(students)
    display_summary(students)


main()