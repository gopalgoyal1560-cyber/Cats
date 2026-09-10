def dashboard_open(parent):    
    import tkinter as tk
    from tkinter import ttk
    import database as d
    import employee as e
    import adoption as a
    import customers as c
    import settings as s
    from datetime import datetime

    root = tk.Toplevel(parent)
    root.title("Cat Cafe & Adoption Management System")
    root.geometry("1450x850")
    root.minsize(1200,700)
    root.configure(bg="#F6F7FB")

    ORANGE = "#F97F05"
    DARK = "#2C2C2C"
    BG = "#F6F7FB"
    CARD = "#FFFFFF"
    LINE = "#E8E8E8"
    HOVER = "#FFF3E6"
    TEXT = "#333333"
    SUBTEXT = "#777777"

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Sidebar.TButton",font=("Segoe UI", 11),padding=10,background="white",foreground="#333333",relief="flat")
    style.map("Sidebar.TButton",background=[("active", HOVER)])
    style.configure("Title.TLabel",font=("Segoe UI", 25, "bold"),background=BG,foreground=TEXT)
    style.configure("CardTitle.TLabel",font=("Segoe UI", 11, "bold"),foreground="#666666",background=CARD)
    style.configure("CardValue.TLabel",font=("Segoe UI", 24, "bold"),foreground=ORANGE,background=CARD)
    style.configure("Section.TLabel",font=("Segoe UI", 15, "bold"),foreground=TEXT,background=CARD)

    header = tk.Frame(root,bg=ORANGE,height=75)
    header.pack(fill="x")
    header.pack_propagate(False)

    left = tk.Frame(header,bg=ORANGE)
    left.pack(side="left",padx=25)

    tk.Label(left,text="🐱",bg=ORANGE,fg="white",font=("Segoe UI Emoji",24)).pack(side="left")
    tk.Label(left,text=" Cat Cafe & Adoption Management System",bg=ORANGE,fg="white",font=("Segoe UI",22,"bold")).pack(side="left")

    right = tk.Frame(header,bg=ORANGE)
    right.pack(side="right",padx=30)

    tk.Label(right,text="Welcome, Admin",bg=ORANGE,fg="white",font=("Segoe UI",12,"bold")).pack(anchor="e")

    body = tk.Frame(root,bg=BG)
    body.pack(fill="both", expand=True)

    sidebar = tk.Frame(body,bg="white",width=180,highlightbackground=LINE,highlightthickness=1)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)

    logo_frame = tk.Frame(sidebar,bg="white")
    logo_frame.pack(pady=25)
    tk.Label(logo_frame,text="🐱", bg="white",fg=ORANGE,font=("Segoe UI Emoji",32)).pack()
    tk.Label(logo_frame, text="Cat Cafe", bg="white", fg=ORANGE, font=("Segoe UI",20,"bold")).pack()

    cont = tk.Frame(body,bg=BG)
    cont.pack(side="left",fill="both",expand=True,padx=25,pady=25)

    bt = {}
    current = {"button":None}

    def activate(name):
        if current["button"]:
            current["button"].configure(bg="white",fg=TEXT)
        b = bt[name]
        b.configure(bg=ORANGE,fg="white")
        current["button"] = b
    buttons = [("🏠","Dashboard"),("🐱","Cats"),("👥","Customers"),("❤️","Adoption"),("👨‍💼","Employees"),("⚙️","Settings")]

    for icon,text in buttons:
        b = tk.Button(sidebar,text=f"{icon} {text}",bg="white",fg=TEXT,activebackground=HOVER,activeforeground=TEXT,
            relief="flat",anchor="w",padx=20,pady=10,font=("Segoe UI",11,"bold"),cursor="hand2")
        b.pack(fill="x",padx=10,pady=2)
        bt[text]=b
        
    def dash(cont):
        ORANGE = "#F97F05"
        BG = "#F6F7FB"
        CARD = "white"
        TEXT = "#333333"
        SUB = "#777777"

        for widget in cont.winfo_children():
            widget.destroy()

        cont.configure(bg=BG)
        top = tk.Frame(cont, bg=BG)
        top.pack(fill="x", pady=(0,20))

        left_top = tk.Frame(top, bg=BG)
        left_top.pack(side="left")

        tk.Label(left_top,text="Dashboard",bg=BG,fg=TEXT,font=("Segoe UI",26,"bold")).pack(anchor="w")
        tk.Label(left_top,text="Last Updated : " + datetime.now().strftime("%d %b %Y   %I:%M:%S %p"),bg=BG,fg="#666666",font=("Segoe UI",10)).pack(anchor="w", pady=(2,0))
        
        right_top = tk.Frame(top, bg=BG)
        right_top.pack(side="right")

        refresh = tk.Button(right_top,text="⟳ Refresh",relief="flat",bg=ORANGE,fg="white",font=("Segoe UI",10,"bold"),cursor="hand2",command=lambda: dash(cont))
        refresh.pack(anchor="e")

        tk.Label(right_top,text="🟢 Database Connected",bg=BG,fg="green",font=("Segoe UI",9,"bold")).pack(anchor="e", pady=(5,0))
        try:
            total_cats = d.get_row_count("cats")
        except:
            total_cats = 0
        try:
            customers = d.get_row_count("customers")
        except:
            customers = 0
        try:
            adoptions = d.get_row_count("adoptions")
        except:
            adoptions = 0
        try:
            employees = d.get_row_count("employees")
        except:
            employees = 0
        
        cards = tk.Frame(cont,bg=BG)
        cards.pack(fill="x")

        data = [("🐱","Cats",total_cats),("👥","Customers",customers),("❤️","Adoptions",adoptions),("👨‍💼","Employees",employees)]
        for icon,title,value in data:
            outer = tk.Frame(cards, bg="#DDDDDD",cursor="hand2")
            outer.pack(side="left", expand=True, fill="x", padx=8)

            card = tk.Frame(outer,bg=CARD,height=140)
            card.pack(fill="both",padx=1,pady=1)
            
            tk.Label(card,text=icon,bg=CARD,fg=ORANGE,font=("Segoe UI Emoji",24)).pack(pady=(18,4))
            tk.Label(card,text=title,bg=CARD,fg=SUB,font=("Segoe UI",11,"bold")).pack()
            tk.Label(card,text=str(value), bg=CARD,fg=TEXT,font=("Segoe UI",24,"bold")).pack(pady=(4,10))
        
        workspace = tk.Frame( cont, bg=BG)
        workspace.pack(fill="both",expand=True,pady=20)

        workspace.grid_columnconfigure(0,weight=1)
        workspace.grid_columnconfigure(1,weight=1)
        workspace.grid_rowconfigure(0,weight=1)
        workspace.grid_rowconfigure(1,weight=1)

        def panel(parent,title):
            frame = tk.Frame(parent,bg="white",highlightbackground="#DDDDDD",highlightthickness=1)
            tk.Label(frame,text=title,bg="white",fg=TEXT,font=("Segoe UI",14,"bold")).pack(anchor="w",padx=15,pady=12)
            return frame
        recent = panel(workspace,"Recent Adoptions")
        recent.grid(row=0,column=0,sticky="nsew",padx=6,pady=6)
        
        actions = panel(workspace,"Quick Actions")
        actions.grid(row=0,rowspan=2,column=1,sticky="nsew",padx=6,pady=6)

        customers_frame = panel(workspace,"Latest Customers")
        customers_frame.grid(row=1,column=0,sticky="nsew",padx=6,pady=6)

        style = ttk.Style()
        style.configure("Dashboard.Treeview",rowheight=28,font=("Segoe UI",10),background="white",fieldbackground="white",borderwidth=0)
        style.configure("Dashboard.Treeview.Heading",font=("Segoe UI",10,"bold"),background=ORANGE,foreground="white",relief="flat")
        style.map("Dashboard.Treeview", background=[("selected","#FFE0BF")], foreground=[("selected","black")])

        recent_tree = ttk.Treeview(recent,style="Dashboard.Treeview",columns=("Cat","Customer"),show="headings",height=10)
        recent_tree.heading("Cat",text="Cat")
        recent_tree.heading("Customer",text="Customer")
        recent_tree.column("Cat",anchor="center",width=180)
        recent_tree.column("Customer",anchor="center",width=220)
        recent_tree.pack(fill="both",expand=True,padx=15,pady=(0,15))

        try:
            rows = d.adoption_data_show()
            for row in rows[-1::-1]:
                recent_tree.insert("","end",values=(row[1],row[2]))
        except:
            pass

        customer_tree = ttk.Treeview(customers_frame,style="Dashboard.Treeview",columns=("Name","Phone"),show="headings",height=10)
        customer_tree.heading("Name",text="Customer")
        customer_tree.heading( "Phone", text="Phone")
        customer_tree.column("Name",anchor="center",width=200)
        customer_tree.column("Phone",anchor="center", width=180)
        customer_tree.pack(fill="both",expand=True,padx=15,pady=(0,15))

        try:
            rows = d.customer_data_show()
            for row in rows[-1::-1]:
                customer_tree.insert("","end",values=(row[1],row[2]))
        except:
            pass

        quick = tk.Frame(actions,bg="white")
        quick.pack(fill="both",expand=True,padx=20,pady=15)

        def action(text,command):
            tk.Button(quick,text=text,command=command,bg=ORANGE,fg="white",relief="flat",cursor="hand2",font=("Segoe UI",11,"bold"),height=1).pack(fill="x",pady=6)

        action("🐱  Manage Cats",lambda: bt["Cats"].invoke())
        action("👥  Customers",lambda: bt["Customers"].invoke())
        action("❤️  Adoptions",lambda: bt["Adoption"].invoke())
        action("👨‍💼  Employees",lambda: bt["Employees"].invoke())

    def destroy():
        for window in cont.winfo_children():
            window.destroy()

    def meow_cat():
        destroy()
        row = d.cat_data_show()
        c.show_data(cont,row)
        c.buttons(root,bt["Cats"],add_cat,delete_cat,search_cat,update_cat)

    def add_cat():
        import cat as c
        name,breed,age,status,health = c.add_data(root) 
        import database as d
        d.cat_data_add(name,breed,age,status,health)
        destroy()
        row = d.cat_data_show()
        c.show_data(cont,row)

    def  delete_cat():
        import cat as c
        search = tk.Toplevel(root)
        search.geometry("400x220")
        search.config(bg="#F97F05")
        search.resizable(False, False)

        header = tk.Frame(search, bg="#F97F05")
        header.pack(fill="x", pady=5)

        title = tk.Label(header,text="Delete Cat Record",font=("Arial", 20, "bold"),bg="#F97F05", fg="white")
        title.pack(pady=10)

        frame = tk.Frame(search, bg="#F97F05")
        frame.pack(fill="both", expand=True)

        tk.Label(frame,text="Cat ID :",font=("Arial", 15, "bold"),bg="#F97F05", fg="white").grid(row=0, column=0, padx=10, pady=20, sticky="e")

        id = tk.Entry(frame,width=25,relief="flat",font=("Arial", 11))
        id.grid(row=0, column=1, padx=10, pady=20)
        def remove():
            row = d.cat_data_show()
            if id.get():
                d.cat_delete_data(id.get(),root)
            destroy()
            import cat as c
            c.show_data(cont,row)
            search.destroy()
        
        tk.Button(search,text="Delete",width=20,relief="flat",bg="white",fg="#F97F05",font=("Arial", 11, "bold"),cursor="hand2",command = remove).pack(pady=15)


    def search_cat():
        import cat as c
        search = tk.Toplevel(root)
        search.geometry("400x220")
        search.config(bg="#F97F05")
        search.resizable(False, False)

        header = tk.Frame(search, bg="#F97F05")
        header.pack(fill="x", pady=5)

        title = tk.Label(header,text="Search Cat Record",font=("Arial", 20, "bold"),bg="#F97F05",fg="white")
        title.pack(pady=10)

        frame = tk.Frame(search, bg="#F97F05")
        frame.pack(fill="both", expand=True)

        tk.Label(frame,text="Cat ID :",font=("Arial", 15, "bold"),bg="#F97F05",fg="white").grid(row=0, column=0, padx=10, pady=20, sticky="e")
        id = tk.Entry(frame,width=25,relief="flat",font=("Arial", 11))
        id.grid(row=0, column=1, padx=10, pady=20)
        def remove():
            if id.get():
                r = d.cat_search_data(id.get(),root)
                row = [r]
            destroy()
            c.show_data(cont,row)
            search.destroy()
        
        tk.Button(search,text="Search",width=20,relief="flat",bg="white",fg="#F97F05",font=("Arial", 11, "bold"),cursor="hand2",command = remove).pack(pady=15)


    def update_cat():
        import cat as c
        search = tk.Toplevel(root)
        search.geometry("400x220")
        search.config(bg="#F97F05")
        search.resizable(False, False)

        header = tk.Frame(search, bg="#F97F05")
        header.pack(fill="x", pady=5)

        title = tk.Label(header,text="Search Cat Record",font=("Arial", 20, "bold"),bg="#F97F05", fg="white")
        title.pack(pady=10)

        frame = tk.Frame(search, bg="#F97F05")
        frame.pack(fill="both", expand=True)

        tk.Label(frame,text="Cat ID :",font=("Arial", 15, "bold"),bg="#F97F05",fg="white").grid(row=0, column=0, padx=10, pady=20, sticky="e")

        id = tk.Entry(frame,width=25,relief="flat",font=("Arial", 11))
        id.grid(row=0, column=1, padx=10, pady=20)
        def update():
            if id.get():
                c.update_data(id.get(),root)
            search.destroy()
            destroy()
            row = d.cat_data_show()
            c.show_data(cont,row)
        tk.Button(search,text="Search",width=20,relief="flat",bg="white",fg="#F97F05",font=("Arial", 11, "bold"),cursor="hand2",command = update).pack(pady=15)


    def meow_customer():
        destroy()
        row = d.customer_data_show()
        c.show_data(cont,row)
        c.buttons(root,bt["Customers"],add_customer,delete_customer,search_customer,update_customer)

    def add_customer():
        name,phone,email,address,total_adoption,reservation_date = c.add_data(root) 
        d.customer_data_add(name,phone,email,address,total_adoption,reservation_date)
        destroy()
        row = d.customer_data_show()
        c.show_data(cont,row)

    def delete_customer():
        search = tk.Toplevel(root)
        search.geometry("400x220")
        search.config(bg="#F97F05")
        search.resizable(False, False)

        header = tk.Frame(search, bg="#F97F05")
        header.pack(fill="x", pady=5)

        title = tk.Label(header,text="Delete Customer Record",font=("Arial", 20, "bold"),bg="#F97F05",fg="white")
        title.pack(pady=10)

        frame = tk.Frame(search, bg="#F97F05")
        frame.pack(fill="both", expand=True)

        tk.Label(frame,text="Cutomer ID :",font=("Arial", 15, "bold"),bg="#F97F05",fg="white").grid(row=0, column=0, padx=10, pady=20, sticky="e")

        id = tk.Entry(frame,width=25,relief="flat",font=("Arial", 11))
        id.grid(row=0, column=1, padx=10, pady=20)
        def remove():
            row = d.customer_data_show()
            if id.get():
                d.customer_delete_data(id.get(),root)
            destroy()
            c.show_data(cont,row)
            search.destroy()
        
        tk.Button(search,text="Delete",width=20,relief="flat",bg="white",fg="#F97F05",font=("Arial", 11, "bold"),cursor="hand2",command = remove).pack(pady=15)

    def search_customer():
        search = tk.Toplevel(root)
        search.geometry("400x220")
        search.config(bg="#F97F05")
        search.resizable(False, False)

        header = tk.Frame(search, bg="#F97F05")
        header.pack(fill="x", pady=5)

        title = tk.Label(header,text="Search Customer Record",font=("Arial", 20, "bold"),bg="#F97F05",fg="white")
        title.pack(pady=10)
        
        frame = tk.Frame(search, bg="#F97F05")
        frame.pack(fill="both", expand=True)

        tk.Label(frame,text="Customer ID :",font=("Arial", 15, "bold"),bg="#F97F05",fg="white").grid(row=0, column=0, padx=10, pady=20, sticky="e")

        id = tk.Entry(frame,width=25,relief="flat",font=("Arial", 11))
        id.grid(row=0, column=1, padx=10, pady=20)
        def remove():
            if id.get():
                r = d.customer_search_data(id.get())
                row = [r]
            destroy()
            c.show_data(cont,row)
            search.destroy()
        tk.Button(search,text="Search",width=20,relief="flat",bg="white",fg="#F97F05",font=("Arial", 11, "bold"),cursor="hand2",command = remove).pack(pady=15)

    def update_customer():
        search = tk.Toplevel(root)
        search.geometry("400x220")
        search.config(bg="#F97F05")
        search.resizable(False, False)

        header = tk.Frame(search, bg="#F97F05")
        header.pack(fill="x", pady=5)

        title = tk.Label(header,text="Search Customer Record",font=("Arial", 20, "bold"),bg="#F97F05",fg="white")
        title.pack(pady=10)

        frame = tk.Frame(search, bg="#F97F05")
        frame.pack(fill="both", expand=True)

        tk.Label(frame,text="Customer ID :",font=("Arial", 15, "bold"),bg="#F97F05",fg="white").grid(row=0, column=0, padx=10, pady=20, sticky="e")

        id = tk.Entry(frame,width=25,relief="flat",font=("Arial", 11))
        id.grid(row=0, column=1, padx=10, pady=20)
        def update():
            if id.get():
                c.update_data(id.get(),root)
                name,phone,address = d.fetch_customer_for_adoption_3(id.get())
                d.update_customer_for_adoption(id.get(),name,phone,address)
                destroy()
                row = d.customer_data_show()
                c.show_data(cont,row)
            search.destroy()
        tk.Button(search,text="Search",width=20,relief="flat",bg="white",fg="#F97F05",font=("Arial", 11, "bold"),cursor="hand2",command = update).pack(pady=15)

    def meow_adoption():
        destroy()
        row = d.adoption_data_show()
        a.show_data(cont,row)
        a.buttons(root,bt["Adoption"],add_adoption,delete_adoption,search_adoption,update_adoption)

    def add_adoption():
        customer_id,cat_id, adopter_name, phone, address, date, status = a.add_data(root)
        d.adoption_data_add(customer_id,cat_id,adopter_name,phone,address,date,status)
        d.cat_status_update(cat_id,status)
        d.update_adoption_count(customer_id,root)
        destroy()
        row = d.adoption_data_show()
        a.show_data(cont,row)

    def delete_adoption():
        search = tk.Toplevel(root)
        search.geometry("400x220")
        search.config(bg="#F97F05")
        search.resizable(False, False)

        header = tk.Frame(search, bg="#F97F05")
        header.pack(fill="x", pady=5)

        title = tk.Label(header,text="Delete Adoption Record",font=("Arial", 20, "bold"), bg="#F97F05",fg="white")
        title.pack(pady=10)

        frame = tk.Frame(search, bg="#F97F05")
        frame.pack(fill="both", expand=True)

        tk.Label(frame,text="Adoption ID :",font=("Arial", 15, "bold"),bg="#F97F05",fg="white").grid(row=0, column=0, padx=10, pady=20, sticky="e")

        id = tk.Entry(frame,width=25,relief="flat",font=("Arial", 11))
        id.grid(row=0, column=1, padx=10, pady=20)
        def remove():
            if id.get():
                d.adoption_delete_data(id.get(),root)
            search.destroy()
            destroy()
            row = d.adoption_data_show()
            a.show_data(cont,row)
        tk.Button(search,text="Delete",width=20,relief="flat",bg="white",fg="#F97F05",font=("Arial", 11, "bold"),cursor="hand2",command = remove).pack(pady=15)

    def search_adoption():
        search = tk.Toplevel(root)
        search.geometry("400x220")
        search.config(bg="#F97F05")
        search.resizable(False, False)

        header = tk.Frame(search, bg="#F97F05")
        header.pack(fill="x", pady=5)

        title = tk.Label(header,text="Search Adoption Record",font=("Arial", 20, "bold"),bg="#F97F05",fg="white")
        title.pack(pady=10)

        frame = tk.Frame(search, bg="#F97F05")
        frame.pack(fill="both", expand=True)

        tk.Label(frame,text="Adoption ID :",font=("Arial", 15, "bold"),bg="#F97F05",fg="white").grid(row=0, column=0, padx=10, pady=20, sticky="e")

        id = tk.Entry(frame,width=25,relief="flat",font=("Arial", 11))
        id.grid(row=0, column=1, padx=10, pady=20)

        def find():
            if id.get():
                r=d.adoption_search_data(id.get())
                row=[r]
                destroy()
                a.show_data(cont,row)
            search.destroy()
        tk.Button(search,text="Search",width=20,relief="flat",bg="white",fg="#F97F05",font=("Arial", 11, "bold"),cursor="hand2",command = find).pack(pady=15)

    def update_adoption():
        search = tk.Toplevel(root)
        search.geometry("400x220")
        search.config(bg="#F97F05")
        search.resizable(False, False)

        header = tk.Frame(search, bg="#F97F05")
        header.pack(fill="x", pady=5)

        title = tk.Label(header,text="Search Adoption Record",font=("Arial", 20, "bold"),bg="#F97F05",fg="white")
        title.pack(pady=10)

        frame = tk.Frame(search, bg="#F97F05")
        frame.pack(fill="both", expand=True)

        tk.Label(frame,text="Adoption ID :",font=("Arial", 15, "bold"),bg="#F97F05",fg="white").grid(row=0, column=0, padx=10, pady=20, sticky="e")

        id = tk.Entry(frame,width=25,relief="flat",font=("Arial", 11))
        id.grid(row=0, column=1, padx=10, pady=20)
        def update():
            if id.get():
                a.update_data(id.get(),root)
                destroy()
                row = d.adoption_data_show()
                a.show_data(cont,row)
            search.destroy()
        tk.Button(search,text="Search",width=20,relief="flat",bg="white",fg="#F97F05",font=("Arial", 11, "bold"),cursor="hand2",command=update).pack(pady=15)

    def meow_employee():
        destroy()
        row = d.employee_data_show()
        e.show_data(cont, row)
        e.buttons(root, bt["Employees"], add_employee, delete_employee, search_employee, update_employee)

    def add_employee():
        name, phone, email, designation, salary, joining_date = e.add_data(root)
        d.employee_data_add(name, phone, email, designation, salary, joining_date)
        destroy()
        row = d.employee_data_show()
        e.show_data(cont, row)

    def delete_employee():
        search = tk.Toplevel(root)
        search.geometry("400x220")
        search.config(bg="#F97F05")
        search.resizable(False, False)

        header = tk.Frame(search, bg="#F97F05")
        header.pack(fill="x", pady=5)

        tk.Label(header, text="Delete Employee Record", font=("Arial", 20, "bold"), bg="#F97F05", fg="white").pack(pady=10)

        frame = tk.Frame(search, bg="#F97F05")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Employee ID :", font=("Arial", 15, "bold"), bg="#F97F05", fg="white").grid(row=0, column=0, padx=10, pady=20, sticky="e")

        id = tk.Entry(frame, width=25, relief="flat", font=("Arial", 11))
        id.grid(row=0, column=1, padx=10, pady=20)

        def remove():
            if id.get():
                d.employee_delete_data(id.get(), root)
            destroy()
            row = d.employee_data_show()
            e.show_data(cont, row)
            search.destroy()

        tk.Button(search, text="Delete", width=20, relief="flat", bg="white", fg="#F97F05", font=("Arial", 11, "bold"), cursor="hand2", command=remove).pack(pady=15)

    def search_employee():
        search = tk.Toplevel(root)
        search.geometry("400x220")
        search.config(bg="#F97F05")
        search.resizable(False, False)

        header = tk.Frame(search, bg="#F97F05")
        header.pack(fill="x", pady=5)

        tk.Label(header, text="Search Employee Record", font=("Arial", 20, "bold"), bg="#F97F05", fg="white").pack(pady=10)

        frame = tk.Frame(search, bg="#F97F05")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Employee ID :", font=("Arial", 15, "bold"), bg="#F97F05", fg="white").grid(row=0, column=0, padx=10, pady=20, sticky="e")
        id = tk.Entry(frame, width=25, relief="flat", font=("Arial", 11))
        id.grid(row=0, column=1, padx=10, pady=20)

        def search_record():
            if id.get():
                r = d.employee_search_data(id.get(), root)
                if r:
                    row = [r]
                    destroy()
                    e.show_data(cont, row)
            search.destroy()

        tk.Button(search, text="Search", width=20, relief="flat", bg="white", fg="#F97F05", font=("Arial", 11, "bold"), cursor="hand2", command=search_record).pack(pady=15)

    def update_employee():
        search = tk.Toplevel(root)
        search.geometry("400x220")
        search.config(bg="#F97F05")
        search.resizable(False, False)

        header = tk.Frame(search, bg="#F97F05")
        header.pack(fill="x", pady=5)

        tk.Label(header, text="Search Employee Record", font=("Arial", 20, "bold"), bg="#F97F05", fg="white").pack(pady=10)

        frame = tk.Frame(search, bg="#F97F05")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Employee ID :", font=("Arial", 15, "bold"), bg="#F97F05", fg="white").grid(row=0, column=0, padx=10, pady=20, sticky="e")

        id = tk.Entry(frame, width=25, relief="flat", font=("Arial", 11))
        id.grid(row=0, column=1, padx=10, pady=20)

        def update():
            if id.get():
                e.update_data(id.get(), root)
            search.destroy()

        tk.Button(search, text="Search", width=20, relief="flat", bg="white", fg="#F97F05", font=("Arial", 11, "bold"), cursor="hand2", command=update).pack(pady=15)

    def meow_settings():
        s.open_settings(root)

    def logout_():
        from tkinter import messagebox
        if messagebox.askyesno("Logout", "Are you sure you want to logout?",parent=root):
            root.destroy()
            parent.destroy()

    logout = tk.Button(sidebar,text="Logout",font=("Segoe UI", 15),fg="#E53935",bg = TEXT,relief="flat",width=13)

    logout.pack(padx=5, pady=10)
    bt["Dashboard"].config(command = lambda: dash(cont))
    bt["Dashboard"].invoke()
    bt["Cats"].config(command = meow_cat)
    bt["Customers"].config(command = meow_customer)
    bt["Adoption"].config(command = meow_adoption)
    bt["Employees"].config(command = meow_employee)
    bt["Settings"].config(command=meow_settings)
    logout.config(command = logout_)
