from database import connect_db

def student_login():
    connection=connect_db()
    cursor=connection.cursor()

    student_username=input("Enter username:")
    student_password=int(input("Enter password:"))