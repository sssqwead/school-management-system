
import sqlite3

class Enrollment:
    @staticmethod
    def enroll_student(StudentID, CourseID, cursor, connection):
        cursor.execute("INSERT INTO Enrollments (StudentID, CourseID) VALUES (?, ?)", (StudentID, CourseID))
        connection.commit()
        print('Student enrolled successfully.')

    @staticmethod
    def print_all_enrollments(cursor):
        cursor.execute("SELECT e.EnrollmentID, s.StudentName, c.CourseName FROM Enrollments e JOIN Students s ON e.StudentID = s.StudentID JOIN Courses c ON e.CourseID = c.CourseID")
        enrollments = cursor.fetchall()
        if enrollments:
            print("All Enrollments:")
            for enrollment in enrollments:
                print(f"Enrollment ID: {enrollment[0]}, Student Name: {enrollment[1]}, Course Name: {enrollment[2]}")
        else:
            print("No enrollments found.")
