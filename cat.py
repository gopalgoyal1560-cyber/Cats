
def buttons(root,btn,f1,f2,f3,f4):
    import tkinter as tk
    menu = tk.Menu(root,tearoff=0)
    menu.add_command(label="Add",command=f1)
    menu.add_command(label="Update",command=f4)
    menu.add_command(label="Delete",command=f2)
    menu.add_command(label="Search",command=f3)
    
    x = btn.winfo_rootx() + btn.winfo_width()
    y = btn.winfo_rooty()
    menu.tk_popup(x,y)

def add_data(root):
    import tkinter as tk
    from tkinter import ttk
    ca = tk.Toplevel(root)
    ca.geometry("400x400")
    ca.config(bg="#F97F05")
    ca.resizable(False, False)

    header = tk.Frame(ca, background="#F97F05")
    header.pack(fill='y', pady=5)

    label = tk.Label(header,text="Add Cat Details",font=('Arial', 25, 'bold'),bg="#F97F05",fg="white")
    label.pack(pady=10, padx=10)

    frame2 = tk.Frame(ca, background="#F97F05")
    frame2.pack(fill='y', expand=True)

    label2 = tk.Label(frame2,text="Name of Cat :",bg="#F97F05",fg="#F5F5F5",font=('Arial', 15, 'bold'))
    label2.grid(row=1, column=1, padx=5, pady=5)
    name = tk.Entry(frame2, width=30, relief="flat")
    name.grid(row=1, column=2, padx=5, pady=5)

    label3 = tk.Label(frame2,text="Breed of Cat :",bg="#F97F05",fg="#F5F5F5",font=('Arial', 15, 'bold'))
    label3.grid(row=2, column=1, padx=5, pady=5)
    breed = tk.Entry(frame2, width=30, relief="flat")
    breed.grid(row=2, column=2, padx=5, pady=5)

    label4 = tk.Label(frame2,text="Age of Cat :",bg="#F97F05",fg="#F5F5F5",font=('Arial', 15, 'bold'))
    label4.grid(row=3, column=1, padx=5, pady=5)
    age = tk.Entry(frame2, width=30, relief="flat")
    age.grid(row=3, column=2, padx=5, pady=5)

    label5 = tk.Label(frame2,text="Status of Cat :",bg="#F97F05",fg="#F5F5F5",font=('Arial', 15, 'bold'))
    label5.grid(row=4, column=1, padx=5, pady=5)
    status = ttk.Combobox(frame2, width=20, values=["Adopted","Available","Dead","Missing"],font=('Arial',11,'bold'))
    status.grid(row=4, column=2, padx=5, pady=5)

    label6 = tk.Label(frame2,text="Health of Cat :",bg="#F97F05",fg="#F5F5F5",font=('Arial', 15, 'bold'))
    label6.grid(row=5, column=1, padx=5, pady=5)
    health = ttk.Combobox(frame2, width=20, font=('Arial',11,'bold'),values=["Good","Poor","Average"])
    health.grid(row=5, column=2, padx=5, pady=5)
    value = None
    def submit():
        nonlocal value
        value = (name.get(),breed.get(),age.get(),status.get(),health.get())
        ca.destroy()
    tk.Button(ca,text="Add",command=submit,width=20,relief="flat").pack(padx=5, pady=5)
    root.wait_window(ca)
    return value

def show_data(content,rows):
    from tkinter import ttk
    import tkinter as tk
    tree = ttk.Treeview(content,columns=("id","name","breed","age","status","health"),show="headings")
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

    tree.heading("id", text="ID")
    tree.heading("name", text="Name")
    tree.heading("breed", text="Breed")
    tree.heading("age", text="Age")
    tree.heading("status", text="Status")
    tree.heading("health", text="Health")

    tree.column("id", width=80, anchor="center")
    tree.column("name", width=170, anchor="center")
    tree.column("breed", width=160, anchor="center")
    tree.column("age", width=70, anchor="center")
    tree.column("status", width=140, anchor="center")
    tree.column("health", width=160, anchor="center")

    scroll = ttk.Scrollbar(content,orient="vertical",command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    scroll.pack(side = "right",fill='y')

    tree.pack(fill="both", expand=True, padx=20, pady=20)
    for item in tree.get_children():
        tree.delete(item)
    for row in rows:
        tree.insert("",tk.END,values=row)
    
def update_data(id,root):
    import database as d
    import tkinter as tk
    from tkinter import ttk
    value = d.cat_search_data(id, root)
    if value is not None:
        ca = tk.Toplevel(root)
        ca.geometry("400x400")
        ca.config(bg="#F97F05")
        ca.resizable(False, False)

        header = tk.Frame(ca, bg="#F97F05")
        header.pack(fill="y", pady=5)

        tk.Label(header, text="Update Cat Details", font=("Arial", 25, "bold"), bg="#F97F05", fg="white").pack(pady=10)

        frame2 = tk.Frame(ca, bg="#F97F05")
        frame2.pack(fill="y", expand=True)

        tk.Label(frame2, text="Name of Cat :", bg="#F97F05", fg="#F5F5F5", font=("Arial", 15, "bold")).grid(row=1, column=1, padx=5, pady=5, sticky="e")
        name = tk.Entry(frame2, width=30, relief="flat")
        name.grid(row=1, column=2, padx=5, pady=5)
        name.insert(0, value[1])

        tk.Label(frame2, text="Breed of Cat :", bg="#F97F05", fg="#F5F5F5", font=("Arial", 15, "bold")).grid(row=2, column=1, padx=5, pady=5, sticky="e")
        breed = tk.Entry(frame2, width=30, relief="flat")
        breed.grid(row=2, column=2, padx=5, pady=5)
        breed.insert(0, value[2])

        tk.Label(frame2, text="Age of Cat :", bg="#F97F05", fg="#F5F5F5", font=("Arial", 15, "bold")).grid(row=3, column=1, padx=5, pady=5, sticky="e")
        age = tk.Entry(frame2, width=30, relief="flat")
        age.grid(row=3, column=2, padx=5, pady=5)
        age.insert(0, value[3])

        tk.Label(frame2, text="Status of Cat :", bg="#F97F05", fg="#F5F5F5", font=("Arial", 15, "bold")).grid(row=4, column=1, padx=5, pady=5, sticky="e")
        status = ttk.Combobox(frame2, width=20, font = ('Arial',11,'bold'),values=["Adopted","Available","Dead","Missing"])
        status.grid(row=4, column=2, padx=5, pady=5)
        status.insert(0,value[4])

        tk.Label(frame2, text="Health of Cat :", bg="#F97F05", fg="#F5F5F5", font=("Arial", 15, "bold")).grid(row=5, column=1, padx=5, pady=5, sticky="e")
        health = ttk.Combobox(frame2, width=20, values = ["Good","Poor","Average"],font = ('Arial',11,'bold'))
        health.grid(row=5, column=2, padx=5, pady=5)
        health.insert(0, value[5])

        value = None

        def submit():
            nonlocal value
            value = (name.get(), breed.get(), age.get(), status.get(), health.get())
            ca.destroy()

        tk.Button(ca, text="Update", command=submit, width=20, relief="flat").pack(padx=5, pady=5)

        root.wait_window(ca)
        d.cat_update_data(id, value, root)


            