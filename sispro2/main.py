try:
    from services.sis import SIS  # Import SIS from sis.py
except ModuleNotFoundError:
    print("Error: Could not find 'sis.py'. Ensure it exists in the correct directory.")

def main():
    sis = SIS()  # Create SIS instance

    while True:
        print("\nStudent Information System")
        print("1. Add Student")
        print("2. Enroll Student")
        print("3. Add Course")
        print("4. Add Teacher and Assign to Course")
        print("5. Assign Teacher")
        print("6. Record Payment")
        print("7. View Student Enrollments")
        print("8. View Payments by Student")
        print("9. Generate Enrollment Report")
        print("10. Exit")
        print("11. Update Student Information")
        print("12. Update Course Information")
        print("13. Update Teacher Information")

        choice = input("Enter choice: ")

        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            email = input("Email: ")
            phone = input("Phone Number: ")
            sis.add_student(first_name, last_name, dob, email, phone)

        elif choice == '2':
            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))
            sis.enroll_student(student_id, course_id)

        elif choice == '3':
            course_name = input("Course Name: ")
            course_code = input("Course Code: ")
            instructor_name = input("Instructor Name: ")
            sis.add_course(course_name, course_code, instructor_name)

        elif choice == "4":
            first_name = input("Enter teacher's first name: ")
            last_name = input("Enter teacher's last name: ")
            email = input("Enter teacher's email: ")
            course_id = int(input("Enter course ID to assign teacher: "))
            sis.add_teacher_and_assign_course(first_name, last_name, email, course_id)

        elif choice == '5':
            course_id = int(input("Enter Course ID: "))
            teacher_name = input("Enter Teacher Name: ")
            sis.assign_teacher(course_id, teacher_name)

        elif choice == '6':
            student_id = int(input("Enter Student ID: "))
            amount = float(input("Enter Payment Amount: "))
            sis.record_payment(student_id, amount)

        elif choice == '7':
            student_id = int(input("Enter Student ID: "))
            sis.view_student_enrollments(student_id)

        elif choice == '8':
            student_id = int(input("Enter Student ID: "))
            sis.view_payments_by_student(student_id)

        elif choice == '9':
            course_name = input("Enter Course Name for Report: ")
            sis.generate_enrollment_report(course_name)

        elif choice == '10':
            print("Exiting the Student Information System. Goodbye!")
            break

        # ✅ New Update Options
        elif choice == '11':
            student_id = int(input("Enter Student ID: "))
            first_name = input("Updated First Name: ")
            last_name = input("Updated Last Name: ")
            dob = input("Updated Date of Birth (YYYY-MM-DD): ")
            email = input("Updated Email: ")
            phone = input("Updated Phone Number: ")
            sis.update_student_info(student_id, first_name, last_name, dob, email, phone)

        elif choice == '12':
            course_id = int(input("Enter Course ID: "))
            course_code = input("Updated Course Code: ")
            course_name = input("Updated Course Name: ")
            instructor_name = input("Updated Instructor Name: ")
            sis.update_course_info(course_id, course_code, course_name, instructor_name)

        elif choice == '13':
            teacher_id = int(input("Enter Teacher ID: "))
            first_name = input("Updated First Name: ")
            last_name = input("Updated Last Name: ")
            email = input("Updated Email: ")
            sis.update_teacher_info(teacher_id, first_name, last_name, email)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
