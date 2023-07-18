# SQL - Introduction and Basics

## What's a Database?

A database is a structured collection of data organized and stored in a way that allows efficient data retrieval and management. It serves as a central repository for various types of information, making it easy to access, manipulate, and maintain data for a wide range of applications.

## What's a Relational Database?

A relational database is a type of database that stores and manages data in the form of tables. Each table consists of rows and columns, where each row represents a record, and each column represents a specific attribute of the data. The relationships between tables are established through keys, enabling efficient data retrieval and ensuring data integrity.

## What does SQL stand for?

SQL stands for Structured Query Language. It is a standard programming language used for managing and manipulating data in relational databases. SQL allows users to interact with databases by providing commands for performing various operations, such as querying data, inserting new records, updating existing data, and deleting records.

## What's MySQL?

MySQL is an open-source Relational Database Management System (RDBMS) based on SQL. It is widely used for web development and other applications due to its speed, reliability, and ease of use. MySQL is compatible with various operating systems and supports multiple programming languages, making it a popular choice for many developers.

## How to Create a Database in MySQL?

To create a database in MySQL, you can use the following SQL command:

```
CREATE DATABASE database_name;
```

Replace `database_name` with the desired name for your new database. This command will create a new database with the specified name.

## What does DDL and DML stand for?

DDL stands for Data Definition Language, and DML stands for Data Manipulation Language.

- DDL: DDL is used to define and manage the structure of the database. It includes commands for creating, altering, and deleting database objects such as tables, indexes, and views.
- DML: DML, on the other hand, is used to manipulate the data within the database. It includes commands for inserting, updating, and deleting data from tables.

## How to CREATE or ALTER a Table?

To create a new table in MySQL, you can use the following SQL command:

```
CREATE TABLE table_name (
    column1 datatype1 constraints,
    column2 datatype2 constraints,
    ...
);
```

Replace `table_name` with the desired name for your new table. Define the columns and their data types along with any constraints (e.g., primary key, foreign key) as required.

To alter an existing table, you can use the ALTER TABLE statement with various options like ADD COLUMN, MODIFY COLUMN, DROP COLUMN, etc., depending on the change you want to make.

## How to SELECT Data from a Table?

To retrieve data from a table in MySQL, you can use the SELECT statement:

```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

Replace `column1, column2, ...` with the names of the columns you want to retrieve. Use `*` to select all columns. Specify the `table_name` from which you want to fetch data. You can also use the optional `WHERE` clause to filter the data based on specific conditions.

## How to INSERT, UPDATE, or DELETE Data?

To insert data into a table, use the following SQL command:

```
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

Replace `table_name` with the name of the table you want to insert data into. Specify the values to be inserted for each column.

To update data in a table, use the UPDATE statement:

```
UPDATE table_name
SET column1 = new_value1, column2 = new_value2, ...
WHERE condition;
```

Replace `table_name` with the name of the table to update. Set new values for the desired columns, and use the `WHERE` clause to specify which rows to update.

To delete data from a table, use the DELETE statement:

```
DELETE FROM table_name
WHERE condition;
```

Replace `table_name` with the name of the table from which you want to delete data. Use the `WHERE` clause to specify which rows to delete based on certain conditions.

## What are Subqueries?

Subqueries, also known as nested queries or inner queries, are SQL queries that are embedded within another query. They allow you to perform complex operations and make queries more efficient by breaking them down into smaller, more manageable parts.

A typical example of a subquery is when you use a SELECT statement inside another SELECT, UPDATE, DELETE, or INSERT statement to retrieve or manipulate data based on the results of the inner query.

## How to Use MySQL Functions?

MySQL provides a wide range of built-in functions that allow you to perform various operations on data. Functions can be used in SELECT, WHERE, ORDER BY, and other clauses to modify or analyze data.

For example, to find the total number of rows in a table, you can use the COUNT() function:

```
SELECT COUNT(*) FROM table_name;
```

This will return the total number of rows in the specified table.

These are just some of the fundamental aspects of SQL and MySQL. As you delve deeper into SQL and database management, you'll encounter more advanced concepts and practices that will help you build efficient and robust database-driven applications.
