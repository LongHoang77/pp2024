import re
from datetime import datetime


class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"{self.name} ({self.student_id})"


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return self.name


class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student}")

    # Other methods related to student management can be added here


class CourseManager:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def list_courses(self):
        for i, course in enumerate(self.courses, 1):
            print(f"{i}. {course}")

    # Other methods related to course management can be added here


class MarkManager:
    def __init__(self):
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    # Other methods related to mark management can be added here


class StudentCourseManager:
    def __init__(self, student_manager, course_manager, mark_manager):
        self.student_manager = student_manager
        self.course_manager = course_manager
        self.mark_manager = mark_manager

    def input_student_information(self):
        # Implement input_student_information method here using StudentManager
        pass

    def input_course_information(self):
        # Implement input_course_information method here using CourseManager
        pass

    def select_course(self):
        # Implement select_course method here using CourseManager
        pass

    def select_student(self):
        # Implement select_student method here using StudentManager
        pass

    def input_student_marks(self):
        # Implement input_student_marks method here using MarkManager
        pass

    def display_student_marks(self):
        # Implement display_student_marks method here using MarkManager
        pass


def main():
    student_manager = StudentManager()
    course_manager = CourseManager()
    mark_manager = MarkManager()
    student_course_manager = StudentCourseManager(student_manager, course_manager, mark_manager)

    while True:
        print("\nMenu:")
        print("1. Enter student information")
        print("2. Enter course information")
        print("3. View student marks by course")
        print("4. Enter marks for students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            student_course_manager.input_student_information()
        elif choice == "2":
            student_course_manager.input_course_information()
        elif choice == "3":
            student_course_manager.display_student_marks()
        elif choice == "4":
            student_course_manager.input_student_marks()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
