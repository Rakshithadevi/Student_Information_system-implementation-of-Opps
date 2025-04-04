from dao.db_connection import DBConnection

class EnrollmentDAO:
    def __init__(self):
        self.db = DBConnection()

    def enroll_student(self, student_id, course_id, enrollment_date):
        try:
            with self.db.get_connection() as connection:
                with connection.cursor() as cursor:
                    # ✅ Check if the student is already enrolled
                    check_query = """
                        SELECT COUNT(*) FROM Enrollment 
                        WHERE StudentID = %s AND CourseID = %s
                    """
                    cursor.execute(check_query, (student_id, course_id))
                    (count,) = cursor.fetchone()

                    if count > 0:
                        print(f"❌ Error: Student {student_id} is already enrolled in Course {course_id}.")
                        return  # Stop execution if student is already enrolled

                    # ✅ Insert enrollment if student is NOT already enrolled
                    query = "INSERT INTO Enrollment (StudentID, CourseID, EnrollmentDate) VALUES (%s, %s, %s)"
                    values = (student_id, course_id, enrollment_date)
                    cursor.execute(query, values)
                    connection.commit()
                    print("✅ Student enrolled successfully!")

        except Exception as e:
            print(f"❌ Error enrolling student: {e}")

    def get_enrollments_for_student(self, student_id):
        query = """
        SELECT c.CourseName
        FROM Enrollment e
        JOIN Course c ON e.CourseID = c.CourseID
        WHERE e.StudentID = %s
        """

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (student_id,))
                rows = cursor.fetchall()

        return [row[0] for row in rows]  # ✅ Returns course names

    def get_students_by_course(self, course_id):
        query = """
        SELECT s.StudentID, s.FirstName, s.LastName, s.Email
        FROM Enrollment e
        JOIN Student s ON e.StudentID = s.StudentID
        WHERE e.CourseID = %s
        """

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (course_id,))
                rows = cursor.fetchall()

        return [{"Student ID": row[0], "Name": f"{row[1]} {row[2]}", "Email": row[3]} for row in rows]

    def get_enrollments_by_course(self, course_name):
        query = """
            SELECT s.StudentID, s.FirstName, s.LastName, s.Email 
            FROM Enrollment e
            JOIN Student s ON e.StudentID = s.StudentID
            JOIN Course c ON e.CourseID = c.CourseID
            WHERE c.CourseName = %s
        """
        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (course_name,))
                rows = cursor.fetchall()
        return rows  # List of tuples (StudentID, FirstName, LastName, Email)
