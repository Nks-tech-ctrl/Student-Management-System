from auth import login
from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    view_profile,
)
from report import reports_menu
from student_auth import student_login,change_password


def admin_dashboard():
    while True:
        print("========== Admin Dashboard ==========")
        print("1.Add Student")
        print("2.View Student")
        print("3.Search Student")
        print("4.Update Student")
        print("5.Delete Student")
        print("6.Reports")
        print("7.Logout")

        choice = input("Enter choice:")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            reports_menu()
        elif choice == "7":
            print("Logout")
            break
        else:
            print("Invalid choice!")


def student_dashboard(student_id):
    while True:
        print("========== Student Dashboard ==========")
        print("1.View Profile")
        print("2.Change Password")
        print("3.Logout")

        choice = input("Enter your choice:")

        if choice == "1":
            view_profile(student_id)
        elif choice == "2":
            change_password(student_id)
        elif choice == "3":
            print("Logout")
            break
        else:
            print("Invalid choice")


def home_menu():
    while True:
        print("=========== Student Management System ===========")
        print("1.Admin login")
        print("2.Student Login")
        print("3. Exit")

        choice = input("Enter your input: ")

        if choice == "1":
            if login():
                admin_dashboard()
        elif choice == "2":
            student_id = student_login()

            if student_id:
                student_dashboard(student_id)
        elif choice == "3":
            print("Thanks for visiting.")
            break
        else:
            print("Invalid choice please try again!")


home_menu()
