from database import connect_db


def student_login():
    connection = connect_db()
    cursor = connection.cursor()

    student_username = input("Enter username:")
    student_password = input("Enter password:")

    query = """
     Select *from student_login
     Where username = %s
     AND password = %s;
    """
    cursor.execute(query, (student_username, student_password))
    student = cursor.fetchone()

    if student:
        print("Login successfully")
        return student[1]
    else:
        cursor.close()
        connection.close()
        print("Invalid credentials")
        return False

    cursor.close()
    connection.close()


def change_password(student_id):
    connection = connect_db()
    cursor = connection.cursor()

    current_password = input("Enter current password:")
    new_password = input("Enter New password:")
    confirm_new_password = input("Enter Confirm New password:")

    query = """
      Select *
      from student_login
      where student_id=%s
      and password =%s;
    """
    cursor.execute(query, (student_id,current_password))
    student = cursor.fetchone()

    if student:
        if new_password == confirm_new_password:
            query = """
             UPDATE student_login
             set password =%s
             where student_id =%s;
            """
            cursor.execute(query, (new_password,student_id))
            connection.commit()

            print("Password Changed.")
        else:
            print("New password and confirm new password not matched")

    else:
        print("Password is incorrect!")

    cursor.close()
    connection.close()
