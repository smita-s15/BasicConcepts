# Basic SQL Concepts

## 1. What is SQL?

- Structured Query Language.
- Used to manage and manipulate relational databases.

## 2. SQL Commands Categories Explained

- **DDL (Data Definition Language):**

  - Commands that define or modify the structure of the database objects like tables, indexes, and schemas.
  - Examples:
    - `CREATE`: Create new tables, databases, or other objects.
    - `ALTER`: Modify the structure of an existing object (e.g., add a column to a table).
    - `DROP`: Delete tables or other objects from the database permanently.
  - These commands affect the schema and structure, not the data itself.

- **DML (Data Manipulation Language):**

  - Commands used to manage data within tables.
  - Examples:
    - `SELECT`: Retrieve data from one or more tables.
    - `INSERT`: Add new rows (records) into tables.
    - `UPDATE`: Change existing data in tables.
    - `DELETE`: Remove data from tables.
  - These commands affect the data stored in the database.

- **DCL (Data Control Language):**

  - Commands that control access and permissions to the database and its objects.
  - Examples:
    - `GRANT`: Give users specific privileges like SELECT, INSERT, UPDATE, DELETE.
    - `REVOKE`: Remove previously granted privileges.
  - These commands help secure the database by managing user rights.

- **TCL (Transaction Control Language):**
  - Commands to manage transactions, i.e., groups of DML operations executed as a single unit.
  - Examples:
    - `COMMIT`: Save all changes made in the current transaction permanently.
    - `ROLLBACK`: Undo changes made since the last `COMMIT`.
    - `SAVEPOINT`: Create a point within a transaction to which you can rollback without affecting earlier operations.
  - These commands ensure data integrity and consistency during multiple operations.

## 3. Basic SQL Statements

### SELECT

- Retrieve data from tables.

```sql
SELECT column1, column2 FROM table_name;
```

### WHERE

- Filter rows based on conditions.

```sql
SELECT * FROM employees WHERE salary > 50000;
```

### INSERT

- Add new rows.

```sql
INSERT INTO employees (name, salary) VALUES ('John', 60000);
```

### UPDATE

- Modify existing rows.

```sql
UPDATE employees SET salary = 65000 WHERE name = 'John';
```

### DELETE

- Remove rows.

```sql
DELETE FROM employees WHERE name = 'John';
```

## 4. Joins

- Combine rows from two or more tables.

| Join Type  | Description                                   |
| ---------- | --------------------------------------------- |
| INNER JOIN | Rows with matching keys in both tables        |
| LEFT JOIN  | All rows from left table + matched from right |
| RIGHT JOIN | All rows from right table + matched from left |
| FULL JOIN  | All rows from both tables                     |

Example:

```sql
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;
```

## 5. GROUP BY and Aggregations Explained

- **GROUP BY** is used to group rows that have the same values in specified columns into summary rows.
- It helps in organizing data into categories and then performing calculations on each group.
- Often used with **aggregate functions** to compute summary statistics for each group.

### Common Aggregate Functions:

- `COUNT()` — Counts the number of rows in each group.
- `SUM()` — Calculates the total sum of values in a numeric column for each group.
- `AVG()` — Calculates the average value of a numeric column for each group.
- `MAX()` — Finds the maximum value in a column for each group.
- `MIN()` — Finds the minimum value in a column for each group.

```sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;
```

## 6. ORDER BY

- Sort results.

```sql
SELECT * FROM employees ORDER BY salary DESC;
```

## 7. SQL Constraints Explained

- **PRIMARY KEY**

  - Uniquely identifies each record in a table.
  - Values must be unique and NOT NULL.
  - Each table can have only one primary key.
  - Often used as the main identifier (e.g., `id` column).

- **FOREIGN KEY**

  - Enforces a link between data in two tables.
  - Ensures that a value in one table corresponds to a valid record in another table.
  - Maintains referential integrity.
  - Example: `orders.customer_id` references `customers.id`.

- **UNIQUE**

  - Ensures all values in a column are distinct.
  - Allows NULL values (but each NULL is treated as distinct).
  - Can be applied to one or multiple columns.

- **NOT NULL**

  - Ensures that a column cannot have NULL values.
  - Forces the field to always contain a value.

- **CHECK**

  - Ensures that all values in a column satisfy a specific condition.
  - Example: `CHECK (age >= 18)` ensures age cannot be less than 18.

- **DEFAULT**
  - Provides a default value for a column when none is specified during insertion.
  - Example: `DEFAULT CURRENT_TIMESTAMP` sets the current date/time if no value is provided.

## 8. Indexes

- Improve query performance.
- Created on columns used frequently in searches.

---

# Summary

- SQL is essential for querying and managing databases.
- Learn SELECT queries with filters, joins, grouping, and ordering.
- Understand data modification with INSERT, UPDATE, DELETE.
- Use constraints and indexes to ensure data integrity and speed.
