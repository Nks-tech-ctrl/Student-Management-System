from auth import login


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
            print("Add student")
        elif choice == "2":
            print("View Student")
        elif choice == "3":
            print("Search student")
        elif choice == "4":
            print("Update Student")
        elif choice == "5":
            print("Delete Student")
        elif choice == "6":
            print("Reports")
        elif choice == "7":
            print("Logout")
            break
        else:
            print("Invalid choice!")


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
            print("Student Dashboard")
        elif choice == "3":
            print("Thanks for visiting.")
            break
        else:
            print("Invalid choice please try again!")


home_menu()
