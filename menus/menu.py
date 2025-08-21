
from models.student import Student
from models.teacher import Teacher
from models.course import Course
from models.enrollment import Enrollment

def main_menu(cursor, connection):
    while True:
        print('\nMain Menu:')
        print('1. Manage Students')
        print('2. Manage Teachers')
        print('3. Manage Courses')
        print('4. Manage Enrollments')
        print('5. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            manage_students(cursor, connection)
        elif choice == '2':
            manage_teachers(cursor, connection)
        elif choice == '3':
            manage_courses(cursor, connection)
        elif choice == '4':
            manage_enrollments(cursor, connection)
        elif choice == '5':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')

def manage_students(cursor, connection):
    print('\nStudent Management:')
    print('1. Add New Student')
    print('2. Update Existing Student')
    print('3. Delete Student')
    print('4. View All Students')
    choice = input('Enter your choice: ')

    if choice == '1':
        StudentID = input('Enter Student ID: ')
        StudentName = input('Enter Student Name: ')
        student = Student(StudentID, StudentName)
        student.add_new_student(cursor, connection)
    elif choice == '2':
        StudentID = input('Enter Student ID to update: ')
        StudentName = input('Enter new Student Name: ')
        student = Student(StudentID, StudentName)
        student.update_student(cursor, connection)
    elif choice == '3':
        StudentID = input('Enter Student ID to delete: ')
        Student.delete_student(StudentID, cursor, connection)
    elif choice == '4':
        Student.print_all_students_details(cursor)
    else:
        print('Invalid choice.')

def manage_teachers(cursor, connection):
    print('\nTeacher Management:')
    print('1. Add New Teacher')
    print('2. View All Teachers')
    choice = input('Enter your choice: ')

    if choice == '1':
        TeacherID = input('Enter Teacher ID: ')
        TeacherName = input('Enter Teacher Name: ')
        teacher = Teacher(TeacherID, TeacherName)
        teacher.add_new_teacher(cursor, connection)
    elif choice == '2':
        Teacher.print_all_teachers_details(cursor)
    else:
        print('Invalid choice.')

def manage_courses(cursor, connection):
    print('\nCourse Management:')
    print('1. Add New Course')
    print('2. View All Courses')
    choice = input('Enter your choice: ')

    if choice == '1':
        CourseID = input('Enter Course ID: ')
        CourseName = input('Enter Course Name: ')
        TeacherID = input('Enter Teacher ID: ')
        course = Course(CourseID, CourseName, TeacherID)
        course.add_new_course(cursor, connection)
    elif choice == '2':
        Course.print_all_courses_details(cursor)
    else:
        print('Invalid choice.')

def manage_enrollments(cursor, connection):
    print('\nEnrollment Management:')
    print('1. Enroll Student in Course')
    print('2. View All Enrollments')
    choice = input('Enter your choice: ')

    if choice == '1':
        StudentID = input('Enter Student ID: ')
        CourseID = input('Enter Course ID: ')
        Enrollment.enroll_student(StudentID, CourseID, cursor, connection)
    elif choice == '2':
        Enrollment.print_all_enrollments(cursor)
    else:
        print('Invalid choice.')
