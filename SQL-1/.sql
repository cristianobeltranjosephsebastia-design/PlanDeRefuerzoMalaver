CREATE DATABASE firstdb;
USE firstdb;

CREATE USER 'guru2b'@'localhost' IDENTIFIED BY 'contraseña';
GRANT ALL PRIVILEGES ON firstdb.* TO 'guru2b'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE sales_rep(
    employee_number INT PRIMARY KEY,
    surname VARCHAR(40),
    first_name VARCHAR(30),
    commission TINYINT,
    birthday DATE NULL
);

INSERT INTO sales_rep VALUES
(1,'Perez','Juan',10,NULL),
(2,'Garcia','Pedro',20,NULL),
(3,'Lopez','Carlos',30,NULL),
(4,'Rodriguez','Maria',40,NULL),
(5,'Sanchez','Jose',50,NULL);

SELECT commission
FROM sales_rep
WHERE surname = 'Gordimer';

SELECT * FROM sales_rep
ORDER BY surname ASC, first_name ASC;

SELECT * FROM sales_rep
ORDER BY commission DESC;

SELECT
    surname,
    first_name,
    CASE
        WHEN birthday IS NULL THEN NULL
        ELSE TIMESTAMPDIFF(YEAR, birthday, CURDATE())
    END AS age
FROM sales_rep;

CREATE TABLE sales(
    id INT PRIMARY KEY AUTO_INCREMENT,
    sales_rep INT,
    value DECIMAL(10,2),
    FOREIGN KEY (sales_rep) REFERENCES sales_rep(employee_number)
);

SELECT
    first_name,
    surname,
    value
FROM sales_rep sr
JOIN sales s ON s.sales_rep = sr.employee_number
WHERE first_name='Sol'
AND surname='Rive';

SELECT
    sales_rep,
    SUM(value) AS total
FROM sales
GROUP BY sales_rep
ORDER BY total DESC;

CREATE TABLE products(
    id INT UNSIGNED PRIMARY KEY,
    code INT(6) ZEROFILL
);

START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;
COMMIT;

CREATE USER 'developer'@'localhost' IDENTIFIED BY 'secure_password';
GRANT SELECT, INSERT, UPDATE ON myapp.* TO 'developer'@'localhost';
FLUSH PRIVILEGES;

SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

SELECT name FROM customers
WHERE id IN (
    SELECT customer_id
    FROM orders
    WHERE total > 1000
);

SELECT name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.id
    AND o.total > 1000
);

SELECT name, 'Customer' AS type FROM customers
UNION
SELECT name, 'Employee' AS type FROM employees
ORDER BY name;

CREATE VIEW high_value_customers AS
SELECT c.name, c.email, SUM(o.total) AS lifetime_value
FROM customers c
JOIN orders o ON c.id = o.customer_id
GROUP BY c.id
HAVING lifetime_value > 5000;

SELECT name,
    IF(salary > 50000,'High','Normal') AS level
FROM employees;


SELECT name,
    CASE
        WHEN salary > 70000 THEN 'Senior'
        WHEN salary > 50000 THEN 'Mid'
        ELSE 'Junior'
    END AS level
FROM employees;

-- Variable acumulativa
SET @total = 0;
SELECT @total := @total + price AS running_total, product
FROM orders
ORDER BY order_date;

DELIMITER //
CREATE PROCEDURE GetCustomerOrders(IN p_customer_id INT)
BEGIN
    SELECT * FROM orders
    WHERE customer_id = p_customer_id;
END //
DELIMITER ;

CALL GetCustomerOrders(42);

DELIMITER //
CREATE TRIGGER update_inventory
AFTER INSERT ON o
