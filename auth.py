from database import connect_db


def login():
    connection = connect_db()
    cursor = connection.cursor()
    username = input("Enter the username:")
    password = input("Enter the password:")

    query = "select *from admin where username =%s AND password=%s "
    cursor.execute(query, (username, password))

    result = cursor.fetchone()

    if result:
        print("Login successfull")
        return True
    else:
        print("Invalid credentials!")
        return False
