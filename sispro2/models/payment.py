class Payment:
    def __init__(self, payment_id, student, amount, payment_date):
        self.__payment_id = payment_id
        self.__student = student
        self.__amount = amount
        self.__payment_date = payment_date

        # Add payment to student's payment history using the getter
        student.get_payments().append(self)

    # Getter methods
    def get_payment_id(self):  # <-- Add this method
        return self.__payment_id

    def get_student(self):
        return self.__student

    def get_payment_amount(self):
        return self.__amount

    def get_payment_date(self):
        return self.__payment_date
