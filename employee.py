def buttons(root,btn,f1,f2,f3,f4):
    import tkinter as tk
    menu=tk.Menu(root,tearoff=0)
    menu.add_command(label="Add",command=f1)
    menu.add_command(label="Update",command=f4)
    menu.add_command(label="Delete",command=f2)
    menu.add_command(label="Search",command=f3)

    x=btn.winfo_rootx()+btn.winfo_width()
    y=btn.winfo_rooty()
    menu.tk_popup(x,y)


def add_data(root):
    import tkinter as tk

    emp=tk.Toplevel(root)
    emp.geometry("400x450")
    emp.config(bg="#F97F05")
    emp.resizable(False,False)

    header=tk.Frame(emp,bg="#F97F05")
    header.pack(fill="x",pady=5)

    tk.Label(header,text="Add Employee Details",font=("Arial",20,"bold"),bg="#F97F05",fg="white").pack(pady=10)

    frame=tk.Frame(emp,bg="#F97F05")
    frame.pack(fill="both",expand=True)

    tk.Label(frame,text="Name :",bg="#F97F05",fg="white",font=("Arial",15,"bold")).grid(row=0,column=0,padx=10,pady=8,sticky="e")
    name=tk.Entry(frame,width=30,relief="flat")
    name.grid(row=0,column=1,padx=10,pady=8)

    tk.Label(frame,text="Phone :",bg="#F97F05",fg="white",font=("Arial",15,"bold")).grid(row=1,column=0,padx=10,pady=8,sticky="e")
    phone=tk.Entry(frame,width=30,relief="flat")
    phone.grid(row=1,column=1,padx=10,pady=8)

    tk.Label(frame,text="Email :",bg="#F97F05",fg="white",font=("Arial",15,"bold")).grid(row=2,column=0,padx=10,pady=8,sticky="e")
    email=tk.Entry(frame,width=30,relief="flat")
    email.grid(row=2,column=1,padx=10,pady=8)

    tk.Label(frame,text="Designation :",bg="#F97F05",fg="white",font=("Arial",15,"bold")).grid(row=3,column=0,padx=10,pady=8,sticky="e")
    designation=tk.Entry(frame,width=30,relief="flat")
    designation.grid(row=3,column=1,padx=10,pady=8)

    tk.Label(frame,text="Salary :",bg="#F97F05",fg="white",font=("Arial",15,"bold")).grid(row=4,column=0,padx=10,pady=8,sticky="e")
    salary=tk.Entry(frame,width=30,relief="flat")
    salary.grid(row=4,column=1,padx=10,pady=8)

    tk.Label(frame,text="Joining Date :",bg="#F97F05",fg="white",font=("Arial",15,"bold")).grid(row=5,column=0,padx=10,pady=8,sticky="e")
    joining_date=tk.Entry(frame,width=30,relief="flat")
    joining_date.grid(row=5,column=1,padx=10,pady=8)

    value=None

    def submit():
        nonlocal value
        value=(name.get(),phone.get(),email.get(),designation.get(),salary.get(),joining_date.get())
        emp.destroy()

    tk.Button(emp,text="Add",command=submit,width=20,relief="flat").pack(pady=10)

    root.wait_window(emp)
    return value


def show_data(cont,rows):
    import tkinter as tk
    from tkinter import ttk

    columns=("id","name","phone","email","designation","salary","joining_date")
    tree=ttk.Treeview(cont,columns=columns,show="headings")

    style=ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",background="white",foreground="#333333",rowheight=25,fieldbackground="white",borderwidth=0,relief="flat",font=("Segoe UI",10))
    style.configure("Treeview.Heading",background="#ff7f00",foreground="white",relief="flat",font=("Segoe UI",10,"bold"),padding=8)
    style.map("Treeview",background=[("selected","#ffb347")],foreground=[("selected","black")])
    style.map("Treeview.Heading",background=[("active","#ff9500")])

    scroll=ttk.Scrollbar(cont,orient="vertical",command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right",fill="y")
    tree.pack(fill="both",expand=True,padx=20,pady=20)

    for col in columns:
        tree.heading(col,text=col.upper())

    tree.column("id",width=70,anchor="center")
    tree.column("name",width=170,anchor="center")
    tree.column("phone",width=120,anchor="center")
    tree.column("email",width=220,anchor="center")
    tree.column("designation",width=140,anchor="center")
    tree.column("salary",width=100,anchor="center")
    tree.column("joining_date",width=130,anchor="center")

    for item in tree.get_children():
        tree.delete(item)

    for row in rows:
        tree.insert("",tk.END,values=row)


def update_data(id,root):
    import database as d
    import tkinter as tk

    value=d.employee_search_data(id,root)

    emp=tk.Toplevel(root)
    emp.geometry("400x450")
    emp.config(bg="#F97F05")
    emp.resizable(False,False)

    if value is not None:

        header=tk.Frame(emp,bg="#F97F05")
        header.pack(fill="x",pady=5)

        tk.Label(header,text="Update Employee Details",font=("Arial",20,"bold"),bg="#F97F05",fg="white").pack(pady=10)

        frame=tk.Frame(emp,bg="#F97F05")
        frame.pack(fill="both",expand=True)

        tk.Label(frame,text="Name :",bg="#F97F05",fg="white",font=("Arial",15,"bold")).grid(row=0,column=0,padx=10,pady=8,sticky="e")
        name=tk.Entry(frame,width=30,relief="flat")
        name.grid(row=0,column=1,padx=10,pady=8)
        name.insert(0,value[1])

        tk.Label(frame,text="Phone :",bg="#F97F05",fg="white",font=("Arial",15,"bold")).grid(row=1,column=0,padx=10,pady=8,sticky="e")
        phone=tk.Entry(frame,width=30,relief="flat")
        phone.grid(row=1,column=1,padx=10,pady=8)
        phone.insert(0,value[2])

        tk.Label(frame,text="Email :",bg="#F97F05",fg="white",font=("Arial",15,"bold")).grid(row=2,column=0,padx=10,pady=8,sticky="e")
        email=tk.Entry(frame,width=30,relief="flat")
        email.grid(row=2,column=1,padx=10,pady=8)
        email.insert(0,value[3])

        tk.Label(frame,text="Designation :",bg="#F97F05",fg="white",font=("Arial",15,"bold")).grid(row=3,column=0,padx=10,pady=8,sticky="e")
        designation=tk.Entry(frame,width=30,relief="flat")
        designation.grid(row=3,column=1,padx=10,pady=8)
        designation.insert(0,value[4])

        tk.Label(frame,text="Salary :",bg="#F97F05",fg="white",font=("Arial",15,"bold")).grid(row=4,column=0,padx=10,pady=8,sticky="e")
        salary=tk.Entry(frame,width=30,relief="flat")
        salary.grid(row=4,column=1,padx=10,pady=8)
        salary.insert(0,value[5])

        tk.Label(frame,text="Joining Date :",bg="#F97F05",fg="white",font=("Arial",15,"bold")).grid(row=5,column=0,padx=10,pady=8,sticky="e")
        joining_date=tk.Entry(frame,width=30,relief="flat")
        joining_date.grid(row=5,column=1,padx=10,pady=8)
        joining_date.insert(0,value[6])

        updated_value=None

        def submit():
            nonlocal updated_value
            updated_value=(name.get(),phone.get(),email.get(),designation.get(),salary.get(),joining_date.get())
            emp.destroy()

        tk.Button(emp,text="Update",command=submit,width=20,relief="flat").pack(pady=10)

        root.wait_window(emp)
        d.employee_update_data(id,updated_value,root)