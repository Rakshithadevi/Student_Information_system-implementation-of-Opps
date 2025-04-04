from dao.db_connection import DBConnection
from models.payment import Payment
from dao.student_dao import StudentDAO  # Import StudentDAO

class PaymentDAO:
    def __init__(self):
        self.db = DBConnection()
        self.student_dao = StudentDAO()  # Instantiate StudentDAO

    def record_payment(self, student_id, amount, payment_date):
        query = "INSERT INTO Payment (StudentID, Amount, PaymentDate) VALUES (%s, %s, %s)"
        values = (student_id, amount, payment_date)

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

    def get_payments_for_student(self, student_id):
        query = "SELECT PaymentID, StudentID, Amount, PaymentDate FROM Payment WHERE StudentID = %s"

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (student_id,))
                rows = cursor.fetchall()

        payments = []
        student = self.student_dao.get_student_by_id(student_id)  # Fetch student object

        for row in rows:
            payments.append(Payment(row[0], student, row[2], row[3]))

        return payments
