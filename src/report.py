from database import connect_db
def reports_menu():
    while True:
        print("1.Total Students")
        print("2.Students by course")
        print("3.Students by Semester")
        print("4.Back")

        choice=input("Enter your choice(1/2/3/4):")

        if choice=="1":
            total_student()
        elif choice=="2":
            student_course()
        elif choice=="3":
            student_semester()
        elif choice=="4":
            print("Exit........")
            break
def total_student():
    connection=connect_db()
    cursor=connection.cursor()

    query="""
    select count(*) from students;
"""
    cursor.execute(query)
    total_student=cursor.fetchone()

    print(f"Total Student:{total_student[0]}")

    cursor.close()
    connection.close()

def student_course():
    connection=connect_db()
    cursor=connection.cursor()

    query="""
    Select Course,Count(*)
    From Students
    Group By course;
"""
    cursor.execute(query)
    courses=cursor.fetchall()

    for course in courses:
        print(f"course :{course[0]} , Total Students :{course[1]}")

    cursor.close()
    connection.close()

def student_semester():
    connection=connect_db()
    cursor=connection.cursor()

    query="""
    Select Semester ,count(*)
    From Students
    Group by semester;
"""
    cursor.execute(query)
    semesters=cursor.fetchall()
    
    for semester in semesters:
        print(f"semester :{semester[0]}, Total Students:{semester[1]}")

    cursor.close()
    connection.close()