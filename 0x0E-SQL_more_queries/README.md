# SQL - More queries

## How to Create a New MySQL User

To create a new MySQL user, follow these steps:

1. Log in to MySQL as a user with administrative privileges using the `mysql` command-line client.
2. Execute the `CREATE USER` command to create the new user. Replace 'new_username' with the desired username, and 'password' with the desired password.
Example:

```
CREATE USER 'new_username'@'localhost' IDENTIFIED BY 'password';
```

Optionally, grant specific privileges to the user using the `GRANT` statement. For instance, to grant all privileges on a specific database to the new user:

```
GRANT ALL PRIVILEGES ON database_name.* TO 'new_username'@'localhost';
```

## How to Manage Privileges for a User to a Database or Table

To manage privileges for a user in MySQL, use the `GRANT` and `REVOKE` statements. The `GRANT` statement allows you to grant specific privileges, while the `REVOKE` statement revokes granted privileges.

Example - Granting privileges:

```
GRANT SELECT, INSERT ON database_name.table_name TO 'username'@'host';
```

Example - Revoking privileges:

```
REVOKE DELETE ON database_name.table_name FROM 'username'@'host';
```

## What's a PRIMARY KEY

A PRIMARY KEY is a database constraint that uniquely identifies each row in a table. It ensures that the designated column(s) contain unique and non-null values. Each table can have only one PRIMARY KEY.

Example:

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50)
);
```

## What's a FOREIGN KEY

A FOREIGN KEY is a database constraint that establishes a relationship between two tables. It ensures referential integrity by enforcing that the values in a column of one table correspond to the values in the primary key column of another table.

Example:

```
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

## How to Use NOT NULL and UNIQUE Constraints

The NOT NULL constraint ensures that a column does not contain any null values, meaning it must always have a value.

Example:

```
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50) NOT NULL
);
```

The UNIQUE constraint ensures that the values in the specified column(s) are unique across the table.

Example:

```
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) UNIQUE
);
```

## How to Retrieve Data from Multiple Tables in One Request

To retrieve data from multiple tables in one request, use the JOIN operation. JOIN allows you to combine rows from two or more tables based on related columns.

Example:

```
SELECT employees.employee_name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id;
```

## What Are Subqueries

Subqueries, also known as nested queries or inner queries, are SQL techniques that involve embedding one query (inner query) within another query (outer query). Subqueries are used to retrieve data based on the results of another query, allowing you to build more complex and dynamic SQL statements.

Example:

```
SELECT product_name
FROM products
WHERE product_id NOT IN (SELECT product_id FROM orders);
```

## What Are JOIN and UNION

JOIN is a fundamental operation in SQL that allows you to combine rows from two or more tables based on related columns. There are various types of joins, including INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.

UNION is a set operation that allows you to combine the results of two or more SELECT queries into a single result set. It automatically removes duplicate rows, but you can use UNION ALL to include duplicate rows.

Example:

```
SELECT employee_name FROM employees
UNION
SELECT contractor_name FROM contractors;
```
