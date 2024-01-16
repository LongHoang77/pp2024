import re
from datetime import datetime


def input_number_of_students():
    while True:
        num_students = input("Enter the number of students: ")
        if not num_students.isdigit():
            print("The number of students must be a positive integer. Please enter again.")
        elif int(num_students) <= 0:
            print("The number of students must be a positive integer. Please enter again.")
        else:
            return int(num_students)


def input_student_information():
    num_students = input_number_of_students()
    students = []
    student_ids = set()
    current_year = datetime.now().year

    for _ in range(num_students):
        while True:
            student_id = input("Enter student ID: ")
            if student_id in student_ids:
                print("Student ID already exists. Please enter a unique ID.")
            else:
                break
        student_name = input("Enter student name:")

        while True:
            student_dob = input("Enter the student's date of birth (dd/mm/yyyy): ")
            if re.match(r'^\d{2}/\d{2}/\d{4}$', student_dob):
                day, month, year = map(int, student_dob.split('/'))
                if (day > 0 and day <= 31) and (month > 0 and month <= 12) and (year > 0 and year <= current_year):
                    break
                else:
                    print("Invalid date of birth. Please enter again.")
            else:
                print("Incorrect date of birth format. Please enter again.")

        students.append({'id': student_id, 'name': student_name, 'dob': student_dob})
        student_ids.add(student_id)

    return students


def input_number_of_courses():
    return int(input("Enter the number of courses: "))


def input_course_information(existing_course_ids):
    while True:
        course_id = input("Enter course ID: ")
        if course_id in existing_course_ids:
            print("Course ID already exists. Please enter a different ID.")
        else:
            break

    course_name = input("Enter course name: ")
    existing_course_ids.add(course_id)

    return {'id': course_id, 'name': course_name}


def select_course(courses):
    print("List of courses:")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course['name']}")

    while True:
        choice = input("Select a course (1-%d): " % len(courses))
        if not choice.isdigit() or not (1 <= int(choice) <= len(courses)):
            print("Invalid choice. Please choose a number from 1 to", len(courses))
        else:
            course_index = int(choice) - 1
            return courses[course_index]


def select_student(students):
    print("List of students:")
    for i, student in enumerate(students):
        print(f"{i + 1}. {student['name']} ({student['id']})")

    while True:
        choice = input("Select a student (1-%d): " % len(students))
        if not choice.isdigit() or not (1 <= int(choice) <= len(students)):
            print("Invalid choice. Please choose a number from 1 to", len(students))
        else:
            student_index = int(choice) - 1
            return students[student_index]


def input_student_marks(students, courses, marks):
    if not courses:
        print("No course information. Please enter course information first.")
        return marks

    selected_course = select_course(courses)
    print(f"\nEnter marks for the course: {selected_course['name']}")

    while True:
        selected_student = select_student(students)
        mark = input(f"Enter marks for student {selected_student['name']}: ")
        if mark.isdigit():
            marks[(selected_student['id'], selected_course['id'])] = int(mark)
            another = input("Enter marks for another student? (yes/no): ").lower()
            if another != 'yes':
                break
        else:
            print("Invalid marks. Please enter an integer.")

    return marks


def list_courses(courses):
    print("List of courses:")
    for index, course in enumerate(courses):
        print(f"{index + 1}. {course['name']}")


def list_students(students):
    print("List of students:")
    for index, student in enumerate(students):
        print(f"{index + 1}. {student['name']} ({student['id']})")


def display_student_marks(students, courses, marks):
    if not courses:
        print("No course information. Please enter course information first.")
        return

    selected_course = select_course(courses)
    print(f"\nStudent marks for the course {selected_course['name']}:")

    for student in students:
        student_id = student['id']
        key = (student_id, selected_course['id'])
        if key in marks:
            mark = marks[key]
            print(f"Student {student['name']}: {mark}")
        else:
            print(f"Student {student['name']}: No marks available")


def main():
    students = []
    courses = []
    marks = {}

    while True:
        print("\nMenu:")
        print("1. Enter student information")
        print("2. Enter course information")
        print("3. View student marks by course")
        print("4. Enter marks for students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            students = input_student_information()
        elif choice == "2":
            num_courses = input_number_of_courses()
            existing_course_ids = set(course['id'] for course in courses)
            for _ in range(num_courses):
                course_info = input_course_information(existing_course_ids)
                courses.append(course_info)
        elif choice == "3":
            if not courses:
                print("No course information. Please enter course information first.")
                continue
            display_student_marks(students, courses, marks)
        elif choice == "4":
            marks.update(input_student_marks(students, courses, marks))
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
