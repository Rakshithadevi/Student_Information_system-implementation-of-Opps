from dao.db_connection import DBConnection
from models.teacher import Teacher

class TeacherDAO:
    def __init__(self):
        self.db = DBConnection()

    def add_teacher(self, teacher):
        query = "INSERT INTO Teacher (FirstName, LastName, Email) VALUES (%s, %s, %s)"
        values = (teacher.get_first_name(), teacher.get_last_name(), teacher.get_email())

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

        print(f"Teacher {teacher.get_first_name()} {teacher.get_last_name()} added successfully.")

    def get_teacher_by_id(self, teacher_id):
        query = "SELECT TeacherID, FirstName, LastName, Email FROM Teacher WHERE TeacherID = %s"

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (teacher_id,))
                row = cursor.fetchone()

        return Teacher(*row) if row else None

    def update_teacher_info(self, teacher_id, first_name, last_name, email):
        query = """
        UPDATE Teacher 
        SET FirstName = %s, LastName = %s, Email = %s 
        WHERE TeacherID = %s
        """
        values = (first_name, last_name, email, teacher_id)

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

        print(f"Teacher {teacher_id} information updated successfully.")