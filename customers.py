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
    ca = tk.Toplevel(root)
    ca.geometry("400x400")
    ca.config(bg = "#F97F05")
    ca.resizable(False, False)

    header = tk.Frame(ca,background = "#F97F05")
    header.pack(fill = 'y',pady = 5)

    label = tk.Label(header,text = "Add Customer Details",font=('Arial',20,'bold'),relief="flat",background="#F97F05",foreground="white")
    label.pack(pady = 10,padx =10)

    frame2 = tk.Frame(ca,background="#F97F05")
    frame2.pack(fill='y',expand=True)

    label2 = tk.Label(frame2,text = "Name of :",relief="flat",bg = "#F97F05",fg = "#F5F5F5",font=('Arial',15,'bold'))
    label2.grid(row = 2,column = 1,padx = 5,pady = 5,sticky='e')
    name = tk.Entry(frame2,width=30,relief="flat")
    name.grid(row = 2,column = 2,padx = 5,pady = 5)

    label3 = tk.Label(frame2,text = "Phone Number:",relief="flat",bg = "#F97F05",fg = "#F5F5F5",font=('Arial',15,'bold'))
    label3.grid(padx = 5,pady = 5,row = 3,column = 1,sticky="e")
    phone = tk.Entry(frame2,width=30,relief="flat")
    phone.grid(row = 3,column = 2,padx = 5,pady = 5)

    label4 = tk.Label(frame2,text = "E-mail Id :",relief="flat",bg = "#F97F05",fg = "#F5F5F5",font=('Arial',15,'bold'))
    label4.grid(padx = 5,pady = 5,row = 4,column = 1,sticky="e")
    email = tk.Entry(frame2,width=30,relief="flat")
    email.grid(row = 4,column = 2,padx = 5,pady = 5)

    label5 = tk.Label(frame2,text = "Address :",relief="flat",bg = "#F97F05",fg = "#F5F5F5",font=('Arial',15,'bold'))
    label5.grid(padx = 5,pady = 5,row = 5,column = 1,sticky="e")
    address = tk.Entry(frame2,width=30,relief="flat")
    address.grid(row = 5,column = 2,padx = 5,pady = 5)

    label6 = tk.Label(frame2,text = "Total Adoption :",relief="flat",bg = "#F97F05",fg = "#F5F5F5",font=('Arial',15,'bold'))
    label6.grid(padx = 5,pady = 5,row = 6,column = 1,sticky="e")
    total_adoption = tk.Entry(frame2,width=30,relief="flat")
    total_adoption.grid(row = 6,column = 2,padx = 5,pady = 5)
    
    label7 = tk.Label(frame2,text = "Reservation Date :",relief="flat",bg = "#F97F05",fg = "#F5F5F5",font=('Arial',15,'bold'))
    label7.grid(padx = 5,pady = 5,row = 7,column = 1,sticky="e")
    reservation_date = tk.Entry(frame2,width=30,relief="flat")
    reservation_date.grid(row = 7,column = 2,padx = 5,pady = 5)

    value = None
    def submit():
        nonlocal value
        value = (
            name.get(),phone.get(),email.get(),address.get(),total_adoption.get(),reservation_date.get()
        )
        ca.destroy()

    tk.Button(ca,text = "Add",command=submit,width=20,relief="flat").pack(padx = 5,pady = 5)
    root.wait_window(ca)
    return value

def show_data(content,rows):
    from tkinter import ttk
    import tkinter as tk
    tree = ttk.Treeview(content,columns=("id","name","phone","email","address","total_adoption","reservation_date"),show="headings")
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
    tree.heading("phone", text="Phone")
    tree.heading("email", text="E-mail")
    tree.heading("address", text="Address")
    tree.heading("total_adoption", text="Adoptions")
    tree.heading("reservation_date",text = "Reservation")

    tree.column("id", width=60,anchor="center")
    tree.column("name", width=100,anchor="center")
    tree.column("phone", width=100,anchor="center")
    tree.column("email", width=150,anchor="center")
    tree.column("address", width=180,anchor="center")
    tree.column("total_adoption", width=50,anchor="center")
    tree.column("reservation_date",width = 40,anchor="center")

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

    value = d.customer_search_data(id, root)

    if value is not None:

        ca = tk.Toplevel(root)
        ca.geometry("400x450")
        ca.config(bg="#F97F05")
        ca.resizable(False, False)

        header = tk.Frame(ca, bg="#F97F05")
        header.pack(fill="y", pady=5)

        tk.Label(header, text="Update Customer Details", font=("Arial", 25, "bold"), bg="#F97F05", fg="white").pack(pady=10)

        frame2 = tk.Frame(ca, bg="#F97F05")
        frame2.pack(fill="y", expand=True)

        tk.Label(frame2, text="Name :", bg="#F97F05", fg="#F5F5F5", font=("Arial", 15, "bold")).grid(row=1, column=1, padx=5, pady=5, sticky="e")
        name = tk.Entry(frame2, width=30, relief="flat"); name.grid(row=1, column=2, padx=5, pady=5); name.insert(0, value[1])

        tk.Label(frame2, text="Phone :", bg="#F97F05", fg="#F5F5F5", font=("Arial", 15, "bold")).grid(row=2, column=1, padx=5, pady=5, sticky="e")
        phone = tk.Entry(frame2, width=30, relief="flat"); phone.grid(row=2, column=2, padx=5, pady=5); phone.insert(0, value[2])

        tk.Label(frame2, text="Email :", bg="#F97F05", fg="#F5F5F5", font=("Arial", 15, "bold")).grid(row=3, column=1, padx=5, pady=5, sticky="e")
        email = tk.Entry(frame2, width=30, relief="flat"); email.grid(row=3, column=2, padx=5, pady=5); email.insert(0, value[3])

        tk.Label(frame2, text="Address :", bg="#F97F05", fg="#F5F5F5", font=("Arial", 15, "bold")).grid(row=4, column=1, padx=5, pady=5, sticky="e")
        address = tk.Entry(frame2, width=30, relief="flat"); address.grid(row=4, column=2, padx=5, pady=5); address.insert(0, value[4])

        tk.Label(frame2, text="Adoption Count :", bg="#F97F05", fg="#F5F5F5", font=("Arial", 15, "bold")).grid(row=5, column=1, padx=5, pady=5, sticky="e")
        total_adoption = tk.Entry(frame2, width=30, relief="flat"); total_adoption.grid(row=5, column=2, padx=5, pady=5); total_adoption.insert(0, value[5])

        tk.Label(frame2, text="Reservation Date :", bg="#F97F05", fg="#F5F5F5", font=("Arial", 15, "bold")).grid(row=6, column=1, padx=5, pady=5, sticky="e")
        reservation_date = tk.Entry(frame2, width=30, relief="flat"); reservation_date.grid(row=6, column=2, padx=5, pady=5); reservation_date.insert(0, value[6])

        value = None

        def submit():
            nonlocal value
            value = (
                name.get(),
                phone.get(),
                email.get(),
                address.get(),
                total_adoption.get(),
                reservation_date.get()
            )
            ca.destroy()

        tk.Button(ca, text="Update", command=submit, width=20, relief="flat").pack(padx=5, pady=5)

        root.wait_window(ca)

        if value is not None:
            d.customer_update_data(id, value, root)