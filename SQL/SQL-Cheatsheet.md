# Basic SQL Reference

## SELECT Statement

The `SELECT` statement is used to retrieve data from one or more tables.

```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

Example:
```sql
SELECT first_name, last_name
FROM employees
WHERE department = 'Sales';
```

## INSERT Statement

The `INSERT` statement is used to add new records to a table.

```sql
INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);
```

Example:
```sql
INSERT INTO customers (customer_name, email, phone)
VALUES ('John Doe', 'john@example.com', '555-1234');
```

## UPDATE Statement

The `UPDATE` statement is used to modify existing records in a table.

```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

Example:
```sql
UPDATE employees
SET salary = 55000
WHERE employee_id = 1001;
```

## DELETE Statement

The `DELETE` statement is used to remove records from a table.

```sql
DELETE FROM table_name
WHERE condition;
```

Example:
```sql
DELETE FROM orders
WHERE order_date < '2023-01-01';
```

## JOIN Clause

JOINs are used to combine rows from two or more tables based on a related column between them.

### INNER JOIN

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

Example:
```sql
SELECT orders.order_id, customers.customer_name
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id;
```

### LEFT JOIN

```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

Example:
```sql
SELECT employees.employee_name, departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id;
```

## GROUP BY Clause

The `GROUP BY` clause is used to group rows that have the same values in specified columns.

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1;
```

Example:
```sql
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department;
```

## HAVING Clause

The `HAVING` clause is used to specify a search condition for a group or an aggregate.

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1
HAVING condition;
```

Example:
```sql
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

## ORDER BY Clause

The `ORDER BY` clause is used to sort the result set in ascending or descending order.

```sql
SELECT column1, column2
FROM table_name
ORDER BY column1 [ASC|DESC];
```

Example:
```sql
SELECT product_name, price
FROM products
ORDER BY price DESC;
```