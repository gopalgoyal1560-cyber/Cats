def buttons(root,btn,f1,f2,f3,f4):
    import tkinter as tk
    menu=tk.Menu(root,tearoff=0)
    menu.add_command(label="Add", command=f1)
    menu.add_command(label="Update",command=f4)
    menu.add_command( label="Delete",command=f2)
    menu.add_command(label="Search",command=f3)
    
    x=btn.winfo_rootx()+btn.winfo_width()
    y=btn.winfo_rooty()
    menu.tk_popup(x,y)

def add_data(root):
    import tkinter as tk
    import database as d
    ad = tk.Toplevel(root)
    ad.geometry("400x330")
    ad.config(bg="#F97F05")
    ad.resizable(False, False)

    # Header
    header = tk.Frame(ad, bg="#F97F05")
    header.pack(fill='x', pady=5)

    title = tk.Label(
        header,
        text="Add Adoption Details",
        font=("Arial", 20, "bold"),
        bg="#F97F05",
        fg="white"
    )
    title.pack(pady=10)

    # Form Frame
    frame = tk.Frame(ad, bg="#F97F05")
    frame.pack(fill='both', expand=True)

    tk.Label(
        frame,
        text="Customer ID :",
        bg="#F97F05",
        fg="white",
        font=("Arial", 15, "bold")
    ).grid(row=0, column=0, padx=10, pady=8, sticky="e")

    customer_id = tk.Entry(frame, width=30, relief="flat")
    customer_id.grid(row=0, column=1, padx=10, pady=8)

    # Cat ID
    tk.Label(
        frame,
        text="Cat ID :",
        bg="#F97F05",
        fg="white",
        font=("Arial", 15, "bold")
    ).grid(row=1, column=0, padx=10, pady=8, sticky="e")

    cat_id = tk.Entry(frame, width=30, relief="flat")
    cat_id.grid(row=1, column=1, padx=10, pady=8)

    tk.Label(
        frame,
        text="Adoption Date :",
        bg="#F97F05",
        fg="white",
        font=("Arial", 15, "bold")
    ).grid(row=5, column=0, padx=10, pady=8, sticky="e")

    adoption_date = tk.Entry(frame, width=30, relief="flat")
    adoption_date.grid(row=5, column=1, padx=10, pady=8)

    # Status
    tk.Label(
        frame,
        text="Status :",
        bg="#F97F05",
        fg="white",
        font=("Arial", 15, "bold")
    ).grid(row=6, column=0, padx=10, pady=8, sticky="e")

    status = tk.Entry(frame, width=30, relief="flat")
    status.grid(row=6, column=1, padx=10, pady=8)

    value = None

    def submit():
        row = d.fetch_cusomter_for_adoption(customer_id.get(),cat_id.get(),root)
        nonlocal value
        value = (
            customer_id.get(),
            cat_id.get(),
            row[0],
            row[1],
            row[2],
            adoption_date.get(),
            status.get()
        )
        ad.destroy()

    tk.Button(
        ad,
        text="Add",
        command=submit,
        width=20,
        relief="flat"
    ).pack(pady=10)

    root.wait_window(ad)
    return value
def show_data(cont,rows):
    import tkinter as tk
    from tkinter import ttk
    columns=("customer_id","cat_id","name","phone","address","date","status")
    tree=ttk.Treeview(cont,columns=("customer_id","cat_id","name","phone","address","date","status"),show="headings")
    style =  ttk.Style()
    style.theme_use("clam")
    style.configure(                
         "Treeview",
        background="white",
        foreground="#333333",
        rowheight=25,
        fieldbackground="white",
        borderwidth=0,
        relief="flat",
        font=("Segoe UI", 10)
    )
    style.configure(
          "Treeview.Heading",
        background="#ff7f00",
        foreground="white",
        relief="flat",
        font=("Segoe UI", 10, "bold"),
        padding=8
    )
    style.map(
    "Treeview",
    background=[
        ("selected", "#ffb347")
    ],
    foreground=[
        ("selected", "black")
    ]   
        )
    
    style.map(
    "Treeview.Heading",
    background=[("active", "#ff9500")]
    )
    scroll = ttk.Scrollbar(cont,orient="vertical",command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    scroll.pack(side = "right",fill='y')
    tree.pack(fill="both", expand=True, padx=20, pady=20)
    for col in columns:
        tree.heading(col,text=col)
    tree.column("customer_id", width=70, anchor="center")
    tree.column("cat_id", width=80, anchor="center")
    tree.column("name", width=180, anchor="center")
    tree.column("phone", width=130, anchor="center")
    tree.column("address", width=220, anchor="center")
    tree.column("date", width=130, anchor="center")
    tree.column("status", width=120, anchor="center")
        
    for item in tree.get_children():
        tree.delete(item)
    for row in rows:
        tree.insert("",tk.END,values=row)

def update_data(id, root):

    import database as d
    import tkinter as tk

    value = d.adoption_search_data(id,root)
    if value is not None:
        ad = tk.Toplevel(root)
        ad.geometry("400x230")
        ad.config(bg="#F97F05")
        ad.resizable(False, False)

        header = tk.Frame(ad, bg="#F97F05")
        header.pack(fill="x", pady=5)

        title = tk.Label(
            header,
            text="Update Adoption Details",
            font=("Arial", 20, "bold"),
            bg="#F97F05",
            fg="white"
        )
        title.pack(pady=10)
        frame = tk.Frame(ad, bg="#F97F05")
        frame.pack(fill="both", expand=True)

        tk.Label(
            frame,
            text="Adoption Date :",
            bg="#F97F05",
            fg="white",
            font=("Arial", 15, "bold")
        ).grid(row=4, column=0, padx=10, pady=8, sticky="e")

        adoption_date = tk.Entry(frame, width=30, relief="flat")
        adoption_date.grid(row=4, column=1, padx=10, pady=8)
        adoption_date.insert(0, value[5])

        tk.Label(
            frame,
            text="Adoption Status :",
            bg="#F97F05",
            fg="white",
            font=("Arial", 15, "bold")
        ).grid(row=5, column=0, padx=10, pady=8, sticky="e")

        status = tk.Entry(frame, width=30, relief="flat")
        status.grid(row=5, column=1, padx=10, pady=8)
        status.insert(0, value[6])

        updated_value = None

        def submit():
            nonlocal updated_value
            updated_value = (
                adoption_date.get(),
                status.get()
            )
            ad.destroy()

        tk.Button(
            ad,
            text="Update",
            command=submit,
            width=20,
            relief="flat"
        ).pack(pady=10)

        root.wait_window(ad)
        d.adoption_update_data(id, updated_value,root)