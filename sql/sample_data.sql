USE student_management;

INSERT INTO admin (username, password)
VALUES
('admin', 'admin123');

INSERT INTO students
(first_name, last_name, gender, dob, phone, email, address, course, semester)
VALUES
('Rohan', 'Kumar', 'Male', '2005-08-15', '9876543211', 'rohan@gmail.com', 'Delhi', 'BCA', 2);

INSERT INTO student_login
(student_id, username, password)
VALUES
(1, 'rohan25', '123456');