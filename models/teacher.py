
import sqlite3

class Teacher:
    def __init__(self, TeacherID, TeacherName):
        self.TeacherID = TeacherID
        self.TeacherName = TeacherName

    def add_new_teacher(self, cursor, connection):
        try:
            cursor.execute("INSERT INTO Teachers (TeacherID, TeacherName) VALUES (?, ?)", (self.TeacherID, self.TeacherName))
            connection.commit()
            print('Teacher added successfully.')
        except sqlite3.IntegrityError:
            print('Error: Teacher ID already exists.')

    @staticmethod
    def print_all_teachers_details(cursor):
        cursor.execute("SELECT * FROM Teachers")
        teachers = cursor.fetchall()
        if teachers:
            print("All Teachers:")
            for teacher in teachers:
                print(f"Teacher ID: {teacher[0]}, Teacher Name: {teacher[1]}")
        else:
            print("No teachers found.")
