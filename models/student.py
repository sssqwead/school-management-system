
import sqlite3

class Student:
    def __init__(self, StudentID, StudentName):
        self.StudentID = StudentID
        self.StudentName = StudentName

    def print_student_details(self):
        print(f'Student ID: {self.StudentID}, Student Name: {self.StudentName}')

    def add_new_student(self, cursor, connection):
        try:
            cursor.execute("INSERT INTO Students (StudentID, StudentName) VALUES (?, ?)", (self.StudentID, self.StudentName))
            connection.commit()
            print('Student added successfully.')
        except sqlite3.IntegrityError:
            print('Error: Student ID already exists.')

    def update_student(self, cursor, connection):
        cursor.execute("UPDATE Students SET StudentName = ? WHERE StudentID = ?", (self.StudentName, self.StudentID))
        connection.commit()
        print('Student updated successfully.')

    @staticmethod
    def delete_student(StudentID, cursor, connection):
        cursor.execute("DELETE FROM Students WHERE StudentID = ?", (StudentID,))
        connection.commit()
        print('Student deleted successfully.')

    @staticmethod
    def print_all_students_details(cursor):
        cursor.execute("SELECT * FROM Students")
        students = cursor.fetchall()
        if students:
            print("All Students:")
            for student in students:
                print(f"Student ID: {student[0]}, Student Name: {student[1]}")
        else:
            print("No students found.")
