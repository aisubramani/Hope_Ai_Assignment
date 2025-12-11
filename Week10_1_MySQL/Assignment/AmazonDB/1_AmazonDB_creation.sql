-- Amazon-themed MySQL assignment
-- Dr. Subramani 

-- Create AmazonDB
CREATE DATABASE amazondb;
USE amazondb;

-- Create 1. Users Table
CREATE TABLE users(
user_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100) NOT NULL,
email varchar(150) UNIQUE NOT NULL,
registered_date DATE NOT NULL,
membership ENUM("Basic", "Prime") DEFAULT "Basic"
);

-- Create 2. Products Table
CREATE TABLE products(
product_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(200) NOT NULL,
price DECIMAL(10,2) NOT NULL,
category VARCHAR(100) NOT NULL,
stock INT NOT NULL
);

-- Create 3. Orders Table
CREATE TABLE orders(
order_id INT PRIMARY KEY AUTO_INCREMENT,
user_id INT NOT NULL,
FOREIGN KEY (user_id) REFERENCES users(user_id),
order_date DATE NOT NULL,
total_amount DECIMAL(10,2) NOT NULL
);

-- Create 4. OrderDetails Table
CREATE TABLE orderdetails(
order_details_id INT PRIMARY KEY AUTO_INCREMENT,
order_id INT NOT NULL,
FOREIGN KEY (order_id) REFERENCES orders(order_id),
product_id INT NOT NULL,
FOREIGN KEY (product_id) REFERENCES products(product_id),
quantity INT NOT NULL
);

-- Data Insertion

-- Data Insert into 1. Users Table:
INSERT INTO Users (name, email, registered_date, membership) VALUES
('Alice Johnson', 'alice.j@example.com', '2024-01-15', 'Prime'),
('Bob Smith', 'bob.s@example.com', '2024-02-01', 'Basic'),
('Charlie Brown', 'charlie.b@example.com', '2024-03-10', 'Prime'),
('Daisy Ridley', 'daisy.r@example.com', '2024-04-12', 'Basic');
SELECT * from Users;

-- Data Insert into 2. Products Table:
INSERT INTO Products (name, price, category, stock) VALUES
('Echo Dot', 49.99, 'Electronics', 120),
('Kindle Paperwhite', 129.99, 'Books', 50),
('Fire Stick', 39.99, 'Electronics', 80),
('Yoga Mat', 19.99, 'Fitness', 200),
('Wireless Mouse', 24.99, 'Electronics', 150);
SELECT * from Products;

-- Data Insert into 3. Orders Table:
INSERT INTO Orders (user_id, order_date, total_amount) VALUES
(1, '2024-05-01', 79.98),
(2, '2024-05-03', 129.99),
(1, '2024-05-04', 49.99),
(3, '2024-05-05', 24.99);
SELECT * from Orders;

-- Data Insert into 4. OrderDetails Table:
INSERT INTO OrderDetails (order_id, product_id, quantity) VALUES
(1, 1, 2),
(2, 2, 1),
(3, 1, 1),
(4, 5, 1);
SELECT * from OrderDetails;

