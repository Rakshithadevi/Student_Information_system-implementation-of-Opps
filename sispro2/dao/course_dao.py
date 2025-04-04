from dao.db_connection import DBConnection
from models.course import Course

class CourseDAO:
    def __init__(self):
        self.db = DBConnection()

    def add_course(self, course):
        query = "INSERT INTO Course (CourseName, CourseCode, InstructorName) VALUES (%s, %s, %s)"
        values = (course.get_course_name(), course.get_course_code(), course.get_instructor_name())

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

    def get_course_by_id(self, course_id):
        query = "SELECT CourseID, CourseName, CourseCode, InstructorName FROM Course WHERE CourseID = %s"

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (course_id,))
                row = cursor.fetchone()

        return Course(*row) if row else None

    def assign_teacher(self, course_id, teacher_name):
        query = "UPDATE Course SET InstructorName = %s WHERE CourseID = %s"
        values = (teacher_name, course_id)

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

        print(f"Teacher {teacher_name} assigned to Course ID {course_id}.")


    def update_course_info(self, course_id, course_code, course_name, instructor_name):
            query = """
            UPDATE Course 
            SET CourseCode = %s, CourseName = %s, InstructorName = %s 
            WHERE CourseID = %s
            """
            values = (course_code, course_name, instructor_name, course_id)

            with self.db.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, values)
                    connection.commit()

            print(f"Course {course_id} information updated successfully.")
