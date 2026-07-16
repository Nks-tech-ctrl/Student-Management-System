# Student Management System

This is a simple **Student Management System** built using **Python** and **MySQL**. I created this project to improve my understanding of Python, SQL, database connectivity, and Git/GitHub. It is a command-line application where an administrator can manage student records, and students can log in to view their profile and change their password.

---

## Features

### Admin

- Admin Login
- Add Student
- View All Students
- Search Student
- Update Student Details
- Delete Student
- View Reports
  - Total Students
  - Students by Course
  - Students by Semester
- Logout

### Student

- Student Login
- View Profile
- Change Password
- Logout

---

## Tech Stack

- Python
- MySQL
- mysql-connector-python
- Git & GitHub

---

## Project Structure

```
Student-Management-System/
│
├── src/
│   ├── main.py
│   ├── auth.py
│   ├── student.py
│   ├── student_auth.py
│   ├── report.py
│   ├── database.py
│   └── config.py
│
├── sql/
│   └── schema.sql
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Database

The project uses MySQL as the backend database.

### Tables

- admin
- students
- student_login

The database structure is available in:

```
sql/schema.sql
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Nks-tech-ctrl/Student-Management-System.git
```

### 2. Open the project

```bash
cd Student-Management-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate it

**Windows**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create the database

Open MySQL Workbench and run:

```
sql/schema.sql
```

### 7. Update database credentials

Open `src/config.py` and enter your MySQL username and password.

### 8. Run the project

```bash
cd src
python main.py
```

---

## What I Learned

While building this project, I learned:

- Working with Python modules and functions
- Connecting Python with MySQL
- CRUD operations
- Writing SQL queries
- Using foreign keys
- Building a simple login system
- Organizing code into multiple files
- Using Git branches and merging them
- Uploading and managing projects on GitHub

This project gave me practical experience with Python and MySQL and helped me understand how a simple database application works.

---

## Future Improvements

Some features I would like to add later:

- Password hashing
- Forgot Password
- Attendance Management
- Marks Management
- Export student data to CSV
- GUI using Tkinter
- Web version using Django

---

## Author

**Nikhil Singh**



---

**Thank you for checking out this project. If you have any suggestions or feedback, feel free to open an issue or connect with me on GitHub.**