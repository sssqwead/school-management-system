
def create_tables(cursor, connection):
    cursor.execute("CREATE TABLE IF NOT EXISTS Students (StudentID INTEGER PRIMARY KEY, StudentName TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Teachers (TeacherID INTEGER PRIMARY KEY, TeacherName TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Courses (CourseID INTEGER PRIMARY KEY, CourseName TEXT, TeacherID INTEGER, FOREIGN KEY (TeacherID) REFERENCES Teachers (TeacherID))")
    cursor.execute("CREATE TABLE IF NOT EXISTS Enrollments (EnrollmentID INTEGER PRIMARY KEY AUTOINCREMENT, StudentID INTEGER, CourseID INTEGER, FOREIGN KEY (StudentID) REFERENCES Students (StudentID), FOREIGN KEY (CourseID) REFERENCES Courses (CourseID))")
    connection.commit()
