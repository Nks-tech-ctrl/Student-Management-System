from database import connect_db


def add_student():
    connection = connect_db()
    cursor = connection.cursor()
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    gender = input("Enter gender(Male/female/Other):")
    dob = input("Enter your DOB(YYYY-MM-DD):")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email-id: ")
    address = input("Enter Address")
    course = input("Enter Course Name:")
    semester = int(input("Enter Semester:"))

    query = """
    INSERT INTO students(
     first_name,
     last_name,
     gender,
     dob,
     phone,
     email,
     address,
     course,
     semester
    )
    Values(
       %s,
       %s,
       %s,
       %s,
       %s,
       %s,
       %s,
       %s,
       %s
    );
"""
    cursor.execute(
        query,
        (first_name, last_name, gender, dob, phone, email, address, course,
         semester),
    )
    connection.commit()
    print("Student Added successfully!")

    cursor.close()
    connection.close()


def view_students():
    connection = connect_db()
    cursor = connection.cursor()

    query = """
      Select *from students;
"""

    cursor.execute(query)

    students = cursor.fetchall()
    for student in students:
        print("-" * 50)
        print(f"Student ID      : {student[0]}")
        print(f"First Name      : {student[1]}")
        print(f"Last Name       : {student[2]}")
        print(f"Gender          : {student[3]}")
        print(f"DOB             : {student[4]}")
        print(f"Phone           : {student[5]}")
        print(f"Email           : {student[6]}")
        print(f"Address         : {student[7]}")
        print(f"Course          : {student[8]}")
        print(f"Semester        : {student[9]}")
        print(f"Addmission Date : {student[10]}")

        cursor.close()
        connection.close()


def search_student():
    connection = connect_db()
    cursor = connection.cursor()

    student_id = int(input("Enter student id : "))

    query = """ 
      SELECT *FROM students 
      where student_id = %s;
"""
    cursor.execute(query, (student_id, ))

    student = cursor.fetchone()

    if student:
        print("-" * 50)
        print(f"Student ID      : {student[0]}")
        print(f"First Name      : {student[1]}")
        print(f"Last Name       : {student[2]}")
        print(f"Gender          : {student[3]}")
        print(f"DOB             : {student[4]}")
        print(f"Phone           : {student[5]}")
        print(f"Email           : {student[6]}")
        print(f"Address         : {student[7]}")
        print(f"Course          : {student[8]}")
        print(f"Semester        : {student[9]}")
        print(f"Addmission Date : {student[10]}")
    else:
        print("Student Not Found!")

    cursor.close()
    connection.close()


def update_student():
    connection = connect_db()
    cursor = connection.cursor()

    student_id = int(input("Enter Student ID: "))

    query = """
    SELECT * FROM students
    WHERE student_id = %s;
    """

    cursor.execute(query, (student_id, ))
    student = cursor.fetchone()

    if student:
        print("Enter New Student Details")

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        gender = input("Enter Gender (Male/Female/Other): ")
        dob = input("Enter DOB (YYYY-MM-DD): ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email-id: ")
        address = input("Enter Address: ")
        course = input("Enter Course Name: ")
        semester = int(input("Enter Semester: "))

        query = """
        UPDATE students
        SET
            first_name = %s,
            last_name = %s,
            gender = %s,
            dob = %s,
            phone = %s,
            email = %s,
            address = %s,
            course = %s,
            semester = %s
        WHERE
            student_id = %s;
        """

        cursor.execute(
            query,
            (
                first_name,
                last_name,
                gender,
                dob,
                phone,
                email,
                address,
                course,
                semester,
                student_id,
            ),
        )

        connection.commit()
        print("Student Updated Successfully!")

    else:
        print("Student Not Found!")

    cursor.close()
    connection.close()


def delete_student():
    connection = connect_db()
    cursor = connection.cursor()

    student_id = int(input("Enter student id to delete: "))

    query = """
    Select  *from students
    where student_id=%s;
"""
    cursor.execute(query, (student_id, ))
    student = cursor.fetchone()

    if student:
        confirmation = input(
            "Are you sure you want to delete this student(yes/no):")
        if confirmation == "yes":
            query = """
             DELETE From students 
             Where student_id=%s;                        
"""
            cursor.execute(query, (student_id, ))
            connection.commit()
            print("Student deleted successfully")
        elif confirmation == "no":
            print("Deletion Cancelled")
        else:
            print("Invalid input!")
    else:
        print("Student Not Found!")

    cursor.close()
    connection.close()
