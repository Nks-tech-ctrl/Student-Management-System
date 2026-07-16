from database import connect_db

def student_login():
    connection=connect_db()
    cursor=connection.cursor()

    student_username=input("Enter username:")
    student_password=input("Enter password:")

    query="""
    Select *from student_login
    Where username = %s
    AND password = %s;
"""
    cursor.execute(query,(student_username,student_password))
    student=cursor.fetchone()

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