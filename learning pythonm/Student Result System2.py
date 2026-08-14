def add_students(students):
    name = input("Enter a student name : ")
    marks = add_marks()
    students.append({"name":name, "marks":marks})


def add_marks():
    total = int(input(f"Enter how many subjects? : "))
    marks = []
    for i in range(total):
        mark = float(input(f"Enter the {i+1} subject's mark : "))
        marks.append(mark)
    return marks

def cal_sum(marks):
    total = 0
    for mark in marks:
        total += mark
    return total 

def cal_average(marks):
    average = cal_sum(marks) / len(marks)
    return average

def result(average):
    if average >= 45:
        return 'Pass'
    else:
        return 'Fail'

def display_result(students):
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        avg = cal_average(student['marks'])
        print(f"Average of marks: {avg}")
        rst = result(avg)
        print(f"You are {rst} in this exam.")
        print("")


def main():
    students = []
    while True:
        add_students(students)
        another = input("Do you want to add any more student? (yes or no) ")

        if another != "yes":
            break

    display_result(students)


main()