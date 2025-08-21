
import sqlite3
from database.db_setup import create_tables
from menus.menu import main_menu

if __name__ == '__main__':
    connection = sqlite3.connect('school.db')
    cursor = connection.cursor()
    create_tables(cursor, connection)
    main_menu(cursor, connection)
    connection.close()
    print("\nThank you for using the School Management System!")
    print("All changes have been saved to the database.")
