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
        (first_name, last_name, gender, dob, phone, email, address, course, semester),
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
