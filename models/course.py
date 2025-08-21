
import sqlite3

class Course:
    def __init__(self, CourseID, CourseName, TeacherID):
        self.CourseID = CourseID
        self.CourseName = CourseName
        self.TeacherID = TeacherID

    def add_new_course(self, cursor, connection):
        try:
            cursor.execute("INSERT INTO Courses (CourseID, CourseName, TeacherID) VALUES (?, ?, ?)",
                           (self.CourseID, self.CourseName, self.TeacherID))
            connection.commit()
            print('Course added successfully.')
        except sqlite3.IntegrityError:
            print('Error: Course ID already exists.')

    @staticmethod
    def print_all_courses_details(cursor):
        cursor.execute("SELECT * FROM Courses")
        courses = cursor.fetchall()
        if courses:
            print("All Courses:")
            for course in courses:
                print(f"Course ID: {course[0]}, Course Name: {course[1]}, Teacher ID: {course[2]}")
        else:
            print("No courses found.")
