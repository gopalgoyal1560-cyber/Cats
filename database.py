import sqlite3 as sq
import os
import shutil
from tkinter import filedialog, messagebox
cur = sq.connect("data.db")
cursor = cur.cursor()

def cat_data_add(name,breed,age,status,health):
    
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS cats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        breed TEXT,
        age INTEGER,
        status TEXT,
        health TEXT
        )
        """)
    cursor.execute(
        f"INSERT INTO cats (name,breed,age,status,health) VALUES (?,?,?,?,?)",
        (name,breed,age,status,health)
            )
    cur.commit()

def cat_data_show():
    cursor.execute("""SELECT * FROM "cats" """)
    return cursor.fetchall()

def cat_delete_data(id,parent):
    from tkinter import messagebox
    cursor.execute(
        "DELETE FROM cats WHERE id=?",
        (id,)
    )
    cur.commit()

    if cursor.rowcount == 0:
        messagebox.showerror(
            "Error",
            "The given ID is not present in the database.",
            parent=parent
        )
    else:
        messagebox.showinfo(
            "Success",
            "Cat deleted successfully.",
            parent=parent
        )

def cat_search_data(id,parent):
    from tkinter import messagebox
    cursor.execute(
        "SELECT * FROM cats WHERE id=?",
        (id,)
    )
    row = cursor.fetchone()
    if row:
        return row
    else:
        messagebox.showerror(
            "Error",
            "Cat not found.",
            parent=parent
        )

def cat_update_data(id,value,parent):
    from tkinter import messagebox
    cursor.execute(
        """UPDATE cats SET name = ?, breed = ?, age = ?, status = ?, health = ? Where id = ?""",
            (value[0],value[1],value[2],value[3],value[4],id)
    )
    cur.commit()
    if cursor.rowcount == 0:
        messagebox.showerror(
            "Error",
            "This cat cannot be updated.",
            parent=parent
        )
    else:
        messagebox.showinfo(
            "Success",
            "Cat Updated successfully.",
            parent=parent
        )

def customer_data_add(name,phone,email,address,total_adoption,reservation_date):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone INTEGER,
        email TEXT,
        address TEXT,
        adoptions INTEGER,
        reservation_date TEXT)
        """)
    cursor.execute(
        "INSERT INTO customers(name,phone,email,address,adoptions,reservation_date) VALUES (?,?,?,?,?,?)",
        (name,phone,email,address,total_adoption,reservation_date)
            )
    cur.commit()

def customer_data_show():
    cursor.execute("""SELECT * FROM "customers" """)
    return cursor.fetchall()


def customer_delete_data(id,parent):
    from tkinter import messagebox
    cursor.execute(
        "DELETE FROM customers WHERE id=?",
        (id,)
    )
    cur.commit()

    if cursor.rowcount == 0:
        messagebox.showerror(
            "Error",
            "The given ID is not present in the database.",
            parent=parent
        )
    else:
        messagebox.showinfo(
            "Success",
            "Customer deleted successfully.",
            parent=parent
        )

def customer_search_data(id,parent):
    from tkinter import messagebox
    cursor.execute(
        "SELECT * FROM customers WHERE id=?",
        (id,)
    )
    row = cursor.fetchone()
    if row == None:
        messagebox.showerror(
            "Error",
            "The given ID is not present in the database.",
            parent=parent
        )
    else:
        return row


def customer_update_data(id,value,parent):
    from tkinter import messagebox
    cursor.execute(
        """UPDATE customers SET name = ?, phone = ?, email = ?, address = ?, adoptions = ?,reservation_date = ? Where id = ?""",
            (value[0],value[1],value[2],value[3],value[4],value[5],id)
    )
    cur.commit()
    if cursor.rowcount == 0:
        messagebox.showerror(
            "Error",
            "This customer cannot be updated.",
            parent=parent
        )
    else:
        messagebox.showinfo(
            "Success",
            "Customer Updated successfully.",
            parent=parent
        )

def adoption_data_add(customer_id,cat_id,name,phone,address,date,status):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS adoptions(
    customer_id INTEGER,
    cat_id INTEGER,
    adopter_name TEXT,
    phone INTEGER,
    address TEXT,
    adoption_date TEXT,
    status TEXT)
    """)
    cursor.execute("INSERT INTO adoptions (customer_id,cat_id,adopter_name,phone,address,adoption_date,status) VALUES(?,?,?,?,?,?,?)",
    (customer_id,cat_id,name,phone,address,date,status))
    cur.commit()

def adoption_data_show():
    cursor.execute(
        "SELECT * FROM adoptions"
    )
    return cursor.fetchall()


def adoption_delete_data(id,parent):
    from tkinter import messagebox
    cursor.execute(
        "DELETE FROM adoptions WHERE cat_id=?",
        (id,)
    )
    cur.commit()
    if cursor.rowcount==0:
        messagebox.showerror(
            "Error",
            "Adoption ID not found",
            parent=parent
        )
    else:
        messagebox.showinfo(
            "Success",
            "Adoption deleted",
            parent=parent
        )

def adoption_search_data(id,parent):
    from tkinter import messagebox
    cursor.execute(
        "SELECT * FROM adoptions WHERE cat_id=?",
        (id,)
    )
    row = cursor.fetchone()

    if row is None:
        messagebox.showerror(
            "Error",
            "The given ID is not present in the database.",
            parent=parent
        )
    else:
        return row

def adoption_update_data(id,value,parent):
    from tkinter import messagebox
    cursor.execute(
    """
    UPDATE adoptions SET adoption_date=?,status=? WHERE cat_id=?""",
    (value[0],value[1],id))
    cur.commit()
    if cursor.rowcount == 0:
        messagebox.showerror(
            "Error",
            "This adoption data cannot be updated.",
            parent=parent
        )
    else:
        messagebox.showinfo(
            "Success",
            "Updated successfully.",
            parent=parent
        )

def employee_data_add(name, phone, email, designation, salary, joining_date):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone INTEGER,
        email TEXT,
        designation TEXT,
        salary INTEGER,
        joining_date TEXT)
        """)
    cursor.execute(
        "INSERT INTO employees(name,phone,email,designation,salary,joining_date) VALUES (?,?,?,?,?,?)",
        (name, phone, email, designation, salary, joining_date)
    )
    cur.commit()


def employee_data_show():
    cursor.execute("""SELECT * FROM employees""")
    return cursor.fetchall()


def employee_delete_data(id, parent):
    from tkinter import messagebox
    cursor.execute(
        "DELETE FROM employees WHERE id=?",
        (id,)
    )
    cur.commit()

    if cursor.rowcount == 0:
        messagebox.showerror(
            "Error",
            "The given ID is not present in the database.",
            parent=parent
        )
    else:
        messagebox.showinfo(
            "Success",
            "Employee deleted successfully.",
            parent=parent
        )


def employee_search_data(id, parent):
    from tkinter import messagebox
    cursor.execute(
        "SELECT * FROM employees WHERE id=?",
        (id,)
    )
    row = cursor.fetchone()

    if row is None:
        messagebox.showerror(
            "Error",
            "The given ID is not present in the database.",
            parent=parent
        )
    else:
        return row


def employee_update_data(id, value, parent):
    from tkinter import messagebox
    cursor.execute(
        """UPDATE employees
        SET name=?, phone=?, email=?, designation=?, salary=?, joining_date=?
        WHERE id=?""",
        (value[0], value[1], value[2], value[3], value[4], value[5], id)
    )
    cur.commit()

    if cursor.rowcount == 0:
        messagebox.showerror(
            "Error",
            "This employee cannot be updated.",
            parent=parent
        )
    else:
        messagebox.showinfo(
            "Success",
            "Employee updated successfully.",
            parent=parent
        )

def fetch_cusomter_for_adoption(customer_id,cat_id,parent):
    from tkinter import messagebox
    cursor.execute("SELECT name,phone,address FROM customers WHERE id = ?",
        (customer_id,)
        )
    row = cursor.fetchone()
    cursor.execute("SELECT status FROM cats WHERE id = ?",
         (cat_id,)          
        )
    row2 = cursor.fetchone()
    if (row and row2) and (row2[0] == "available" or row2[0] == "Available"):
        return row
    elif row and row[0] != "available":
        messagebox.showwarning("Missing","Cat is not available",parent=parent)
    else:
        messagebox.showerror("Error","Cutomer do not exist",parent=parent)

def cat_status_update(cat_id,new_status):
    if new_status == "Adopted":
        cursor.execute("""UPDATE cats SET status = ? WHERE id = ?""",
        ("Adopted",cat_id)
        )
    else:
        cursor.execute("""UPDATE cats SET status = ? WHERE id = ?""",
        ("Available",cat_id)
        )

def fetch_customer_for_adoption_3(customer_id):
    cursor.execute("SELECT name,phone,address FROM customers WHERE id = ?",
        (customer_id,)
        )
    return cursor.fetchone()

def update_customer_for_adoption(id,name,phone,address):
    cursor.execute("""UPDATE adoptions SET adopter_name=?,phone=?,address=? WHERE customer_id = ?""",
    (name,phone,address,id)
    )

def update_adoption_count(id,parent):
    from tkinter import messagebox
    result = messagebox.askyesno("Confirmation","Do you want to increment customer adoption count right now?",parent=parent)
    cursor.execute("""UPDATE customers SET adoptions = adoptions+1 WHERE id = ?""",
    (id,)
    )

def login_signup(password,name,email,parent):
        from tkinter import messagebox
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS login(
            password TEXT PRIMARY KEY,
            name TEXT,
            email TEXT UNIQUE)
            """)
        cursor.execute(
            "INSERT INTO login(password,name,email) VALUES (?,?,?)",
            (password,name,email)
        )
        cur.commit()
        if cursor.rowcount != 0:
            messagebox.showinfo("Successfully Signup","Account is created",parent = parent)
        else:
            messagebox.showerror("Error","Cannot sign up",parent = parent)

def login(email, password,parent):
    from tkinter import messagebox
    cursor.execute("""
        SELECT * FROM login
        WHERE email = ? AND password = ?
    """, (email, password))

    user = cursor.fetchone()

    if user:
        return True
    else:
        messagebox.showerror("Login Failed", "Invalid email or password.",parent = parent)
        return False
    
def get_row_count(table_name):
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    return cursor.fetchone()[0]


# =====================================================
# SETTINGS MODULE FUNCTIONS
# =====================================================

DATABASE_NAME = "data.db"


def database_path():
    """Return absolute path of the database."""
    return os.path.abspath(DATABASE_NAME)


def database_size():
    """Return database size in KB or MB."""
    try:
        size = os.path.getsize(DATABASE_NAME)

        if size < 1024 * 1024:
            return f"{size/1024:.2f} KB"
        else:
            return f"{size/(1024*1024):.2f} MB"

    except:
        return "Unknown"


def backup_database(parent):
    """Backup database to a user selected location."""

    filename = filedialog.asksaveasfilename(
        parent=parent,
        title="Backup Database",
        defaultextension=".db",
        initialfile="CatCafe_Backup.db",
        filetypes=[
            ("SQLite Database", "*.db"),
            ("All Files", "*.*")
        ]
    )

    if not filename:
        return

    try:
        cur.commit()                 # Save latest changes
        shutil.copy2(DATABASE_NAME, filename)

        messagebox.showinfo(
            "Backup Complete",
            "Database backed up successfully.",
            parent=parent
        )

    except Exception as e:

        messagebox.showerror(
            "Backup Failed",
            str(e),
            parent=parent
        )


def restore_database(parent):
    """Restore database from a backup."""

    filename = filedialog.askopenfilename(
        parent=parent,
        title="Restore Database",
        filetypes=[
            ("SQLite Database", "*.db"),
            ("All Files", "*.*")
        ]
    )

    if not filename:
        return

    answer = messagebox.askyesno(
        "Restore Database",
        "Current database will be replaced.\n\nContinue?",
        parent=parent
    )

    if not answer:
        return

    try:

        cur.commit()
        # cur.close()

        shutil.copy2(filename, DATABASE_NAME)

        cur2, cursor2
        cur2 = sq.connect(DATABASE_NAME)
        cursor2 = cur.cursor()

        messagebox.showinfo(
            "Restore Complete",
            "Database restored successfully.\n\nRestart the application to reload all data.",
            parent=parent
        )

    except Exception as e:

        messagebox.showerror(
            "Restore Failed",
            str(e),
            parent=parent
        )