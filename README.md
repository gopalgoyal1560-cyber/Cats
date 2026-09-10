# Database-Driven Cat Cafe & Adoption Management System

A desktop management application built with **Python, Tkinter, and SQLite3** for managing cat records, customers, employees, and adoption information through a graphical user interface.

The project was developed as a practical Python application to gain hands-on experience with **GUI development, database operations, SQL queries, and connecting Python applications with persistent data storage**.

## Features

* User login and signup system
* Dashboard for managing application data
* Cat record management

  * Add cat records
  * Search records
  * Update information
  * Delete records
  * Track availability and adoption status
* Customer management

  * Store customer information
  * Search and update records
  * Track adoption counts
* Adoption management

  * Record adoption information
  * Connect customers with cats
  * Check cat availability
  * Update adoption status
* Employee management

  * Store employee details
  * Search, update, and delete records
* SQLite database for persistent data storage
* Database backup and restore functionality
* Database record counting for dashboard statistics

## Tech Stack

* **Python**
* **Tkinter** — Desktop GUI
* **SQLite3** — Local relational database
* **SQL** — Database queries and CRUD operations
* **Pillow (PIL)** — Image handling

## Database & SQL

The application uses Python's built-in `sqlite3` module to communicate with a local SQLite database.

The project includes practical use of SQL operations such as:

```sql
SELECT
INSERT
UPDATE
DELETE
WHERE
COUNT
```

Parameterized queries are used for user-provided values, for example:

```python
cursor.execute(
    "SELECT * FROM customers WHERE id=?",
    (customer_id,)
)
```

The database contains separate tables for different application entities, including:

* `cats`
* `customers`
* `adoptions`
* `employees`
* `login`

The application retrieves query results using methods such as `fetchone()` and `fetchall()`.

## Project Structure

```text
training_project/
│
├── start.py              # Application entry point
├── login.py              # Login and signup interface
├── dashboard.py          # Main dashboard
├── cat.py                # Cat management interface
├── customers.py          # Customer management interface
├── adoption.py           # Adoption management interface
├── employee.py           # Employee management interface
├── settings.py           # Application/database settings
├── database.py           # SQLite database operations
├── data.db               # SQLite database
│
├── image.png             # Application assets
├── img.png               # Application assets
└── README.md
```

## Database Operations

Database functionality is centralized in `database.py`.

Examples of operations implemented include:

### Create / Insert

```python
cursor.execute(
    "INSERT INTO customers(name,phone,email,address,adoptions,reservation_date) VALUES (?,?,?,?,?,?)",
    (name, phone, email, address, total_adoption, reservation_date)
)
```

### Read

```python
cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()
```

### Search

```python
cursor.execute(
    "SELECT * FROM customers WHERE id=?",
    (customer_id,)
)
row = cursor.fetchone()
```

### Update

```python
cursor.execute(
    "UPDATE customers SET name=?, phone=?, email=? WHERE id=?",
    (name, phone, email, customer_id)
)
```

### Delete

```python
cursor.execute(
    "DELETE FROM customers WHERE id=?",
    (customer_id,)
)
```

## Backup & Restore

The application also includes database backup and restore functionality.

Database files can be copied to a user-selected location for backup, while an existing database can be replaced with a selected backup file.

## What I Learned

This project helped me develop practical experience with:

* Python application development
* Tkinter GUI development
* SQLite database integration
* Basic SQL and CRUD operations
* Parameterized SQL queries
* Fetching and processing database results in Python
* Managing multiple related data tables
* Persistent local data storage
* Database backup and restore
* Structuring a multi-file Python application

## Future Improvements

Possible improvements include:

* Adding stronger database relationships and foreign-key constraints
* Improving input validation
* Adding more advanced SQL queries and reporting
* Separating database logic from UI logic more cleanly
* Adding automated tests
* Improving authentication and password security
* Migrating to a server-based database for multi-user applications

## Disclaimer

This project was developed as a learning/training project to practice Python desktop application development and database integration. It is not intended to represent a production-ready management system.
