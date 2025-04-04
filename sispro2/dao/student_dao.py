from dao.db_connection import DBConnection
from models.student import Student

class StudentDAO:
    def __init__(self):
        self.db = DBConnection()

    def add_student(self, student):
        query = "INSERT INTO Student (FirstName, LastName, DateOfBirth, Email, PhoneNumber) VALUES (%s, %s, %s, %s, %s)"
        values = (student.get_first_name(), student.get_last_name(), student.get_date_of_birth(), student.get_email(), student.get_phone_no())

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

    def get_student_by_id(self, student_id):
        query = "SELECT StudentID, FirstName, LastName, DateOfBirth, Email, PhoneNumber FROM Student WHERE StudentID = %s"

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (student_id,))
                row = cursor.fetchone()

        return Student(*row) if row else None

    def update_balance(self, student_id, amount):
        # Make sure Balance column exists in the Student table
        query = "UPDATE Student SET Balance = Balance - %s WHERE StudentID = %s"
        values = (amount, student_id)

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

    def update_student_info(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        query = """
        UPDATE Student 
        SET FirstName = %s, LastName = %s, DateOfBirth = %s, Email = %s, PhoneNumber = %s 
        WHERE StudentID = %s
        """
        values = (first_name, last_name, date_of_birth, email, phone_number, student_id)

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

        print(f"Student {student_id} information updated successfully.")
