import tkinter as tk
from tkinter import messagebox
import database as d

ORANGE = "#F97F05"
BG = "#F6F7FB"
CARD = "#FFFFFF"
TEXT = "#333333"
LINE = "#DDDDDD"

def show_about():

    about = tk.Toplevel()
    about.title("About")
    about.geometry("420x300")
    about.resizable(False, False)
    about.configure(bg=CARD)

    tk.Label(
        about,
        text="Cat Cafe & Adoption Management\nSystem",
        font=("Segoe UI",18,"bold"),
        bg=CARD,
        fg=ORANGE
    ).pack(pady=(25,10))

    info = (
        "Version : 1.0\n\n"
        "Developed using\n"
        "Python\n"
        "Tkinter\n"
        "SQLite\n\n"
        "Developer\n"
        "Gopal"
    )

    tk.Label(
        about,
        text=info,
        justify="center",
        bg=CARD,
        fg=TEXT,
        font=("Segoe UI",11)
    ).pack()

    tk.Button(
        about,
        text="Close",
        bg=ORANGE,
        fg="white",
        relief="flat",
        width=15,
        command=about.destroy
    ).pack(pady=20)

def open_settings(root):
    win = tk.Toplevel(root)
    win.title("Settings")
    win.geometry("720x520")
    win.resizable(False, False)
    win.configure(bg=BG)

    # ================= HEADER =================

    header = tk.Frame(win, bg=ORANGE, height=70)
    header.pack(fill="x")
    header.pack_propagate(False)

    tk.Label(
        header,
        text="⚙ Settings",
        bg=ORANGE,
        fg="white",
        font=("Segoe UI", 22, "bold")
    ).pack(side="left", padx=25)

    # ================= BODY =================

    body = tk.Frame(win, bg=BG)
    body.pack(fill="both", expand=True, padx=20, pady=20)

    body.grid_columnconfigure(0, weight=1)
    body.grid_columnconfigure(1, weight=1)

    def card(title):

        outer = tk.Frame(
            body,
            bg=CARD,
            highlightbackground=LINE,
            highlightthickness=1
        )

        tk.Label(
            outer,
            text=title,
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 14, "bold")
        ).pack(anchor="w", padx=15, pady=15)

        return outer

    # ================= DATABASE =================

    db = card("Database")
    db.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)

    tk.Button(
        db,
        text="Backup Database",
        bg=ORANGE,
        fg="white",
        relief="flat",
        font=("Segoe UI", 11, "bold"),
        cursor="hand2",
        command=lambda: d.backup_database(win)
    ).pack(fill="x", padx=15, pady=8)

    tk.Button(
        db,
        text="Restore Database",
        bg=ORANGE,
        fg="white",
        relief="flat",
        font=("Segoe UI", 11, "bold"),
        cursor="hand2",
        command=lambda: d.restore_database(win)
    ).pack(fill="x", padx=15, pady=8)

    tk.Label(
        db,
        text="Database Path",
        bg=CARD,
        fg=TEXT,
        font=("Segoe UI", 10, "bold")
    ).pack(anchor="w", padx=15, pady=(20, 2))

    path = tk.Label(
        db,
        text=d.database_path(),
        bg=CARD,
        fg="blue",
        wraplength=260,
        justify="left"
    )

    path.pack(anchor="w", padx=15)

    tk.Label(
        db,
        text="Database Size",
        bg=CARD,
        fg=TEXT,
        font=("Segoe UI", 10, "bold")
    ).pack(anchor="w", padx=15, pady=(15, 2))

    tk.Label(
        db,
        text=d.database_size(),
        bg=CARD,
        fg=TEXT
    ).pack(anchor="w", padx=15)

    # ================= PREFERENCES =================

    pref = card("Preferences")
    pref.grid(row=0, column=1, sticky="nsew", padx=8, pady=8)

    confirm = tk.BooleanVar(value=True)
    refresh = tk.BooleanVar(value=True)

    tk.Checkbutton(
        pref,
        text="Confirm before deleting",
        variable=confirm,
        bg=CARD
    ).pack(anchor="w", padx=15, pady=8)

    tk.Checkbutton(
        pref,
        text="Auto Refresh Dashboard",
        variable=refresh,
        bg=CARD
    ).pack(anchor="w", padx=15)

    tk.Button(
    pref,
    text="About Application",
    bg=ORANGE,
    fg="white",
    relief="flat",
    font=("Segoe UI",11,"bold"),
    cursor="hand2",
    command=show_about
    ).pack(fill="x", padx=15, pady=20)

    