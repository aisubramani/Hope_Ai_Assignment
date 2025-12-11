-- A. Data Definition Laguage
-- 1. Create a Database
-- Create a Database named 'practice_db'
CREATE DATABASE practice_db;

-- swith to the new database
USE practice_db;

-- show database
SHOW DATABASES;
 
-- 2) Creating Tables
-- Create a table named 'students'
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique ID, auto-increment
    first_name VARCHAR(50) NOT NULL,            -- Cannot be NULL
    last_name VARCHAR(50),                      -- Optional
    email VARCHAR(100) UNIQUE,                  -- Must be unique
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Default to today's date
);

select * from students;

-- 3) Altering Tables
-- Add a new column 'phone_number' to the 'students' table
ALTER TABLE students ADD phone_number VARCHAR(15);

-- Modify the 'last_name' column to be NOT NULL
alter table students modify last_name varchar(50) not null;

-- Rename the 'students' table to 'university_students
ALTER TABLE students RENAME TO university_students;

-- Rename the 'students' table column old_column_name to new_column_name
ALTER TABLE university_students RENAME COLUMN phone_number TO phone_numbers;


-- 4) Dropping Tables
-- Drop the table 'university_students'
DROP TABLE university_students;

-- Dropping database
DROP DATABASE database_name;

-- 5) Creating Constraints
-- Create a table with constraints
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL UNIQUE,
    credits INT CHECK (credits BETWEEN 1 AND 5)  -- Ensure credits are between 1 and 5
);


-- Create a table with a foreign key
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Remove all rows from the 'students' table
TRUNCATE TABLE students;

-- To delete single column
-- ALTER TABLE table_name DROP COLUMN column_name;
select * from students;
alter table students drop column phone_number;
 
 -- move
 RENAME TABLE old_db_name.table1 TO new_db_name.table1;
 
 
 
 -- ----------------------------------
 -- Data Definition Language (DDL)
 -- Create database
 CREATE DATABASE database1;
 USE database1;
 SHOW DATABASES;
 
-- Create table
CREATE TABLE table_1(
student_id INT PRIMARY KEY AUTO_INCREMENT,
student_name VARCHAR(20) NOT NULL,
email_id VARCHAR(50) UNIQUE,
join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SHOW TABLES;

 -- Rename
 ALTER TABLE table_1 RENAME TO table1;
 ALTER TABLE table1 RENAME COLUMN join_date TO joined_date;
 
 -- Add
 ALTER TABLE table1 ADD phone_number VARCHAR(10);

 -- Modify
 ALTER TABLE table1 MODIFY phone_number INT(10);

 -- Create with forign key
 CREATE TABLE table2 (
 subject_id INT AUTO_INCREMENT PRIMARY KEY,
 age INT CHECK(age BETWEEN 1 AND 100),
 student_id  INT,
 FOREIGN KEY (student_id) REFERENCES table1(student_id )
 );
 
 -- Drop
 DROP DATABASE database1;
 DROP TABLE table1;
 ALTER TABLE table1 DROP COLUMN age;
 
 -- Delete all row
 TRUNCATE TABLE table1;

 
 
 
 