-- Create Database
CREATE DATABASE IF NOT EXISTS student_management;
USE student_management;


-- Admin Table

CREATE TABLE admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);


-- Students Table

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    dob DATE NOT NULL,
    phone VARCHAR(15) UNIQUE,
    email VARCHAR(100) UNIQUE,
    address TEXT,
    course VARCHAR(50),
    semester INT,
    admission_date DATE DEFAULT (CURRENT_DATE)
);


-- Student Login Table

CREATE TABLE student_login (
    login_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT UNIQUE,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
        ON DELETE CASCADE
);