def a(parent):    
    import tkinter as tk
    from tkinter import ttk
    from PIL import Image,ImageTk
    win = tk.Toplevel(parent)
    win.geometry("1000x1000")
    win.resizable(False,False)

    frame1 = tk.Frame(win,width = 500,height = 1000)
    frame1.pack(fill = 'both',side = 'left')

    img = Image.open("image.png")
    img = img.resize((500,650))
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(frame1,image = img)
    img_label.image = img
    img_label.place(x = 0,y = 0)

    frame_2 = tk.Frame(
        win,
        width=500,
        height=1000,
        bg="white"
    )
    frame_2.pack(fill="both", side="right")

    title_font = ("Segoe UI", 26, "bold")
    heading_font = ("Segoe UI", 14, "bold")
    text_font = ("Segoe UI", 11)
    entry_font = ("Segoe UI", 11)
    button_font = ("Segoe UI", 13, "bold")

    label1 = tk.Label(
        frame_2,
        text="Welcome!",
        font=title_font,
        fg="#ff5a36",
        bg="white"
    )
    label1.place(relx=0.5, rely=0.05, anchor="center")

    label2 = tk.Label(
        frame_2,
        text="Login to access your dashboard manage your ",
        font=text_font,
        fg="#666666",
        bg="white"
    )
    label2.place(relx=0.5, rely=0.1, anchor="center")

    label3 = tk.Label(
        frame_2,
        text="account and continue securely with full control",
        font=text_font,
        fg="#666666",
        bg="white"
    )
    label3.place(relx=0.5, rely=0.124, anchor="center")

    label4 = tk.Label(
        frame_2,
        text="Username",
        font=heading_font,
        fg="#333333",
        bg="white"
    )
    label4.place(relx=0.5, rely=0.160, anchor="center")

    username = tk.Entry(
        frame_2,
        font=entry_font,
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#d9d9d9",
        highlightcolor="#ff5a36"
    )
    username.place(relx=0.25, rely=0.190, width=260, height=36)

    label5 = tk.Label(
        frame_2,
        text="E-mail",
        font=heading_font,
        fg="#333333",
        bg="white"
    )
    label5.place(relx=0.5, rely=0.250, anchor="center")

    email = tk.Entry(
        frame_2,
        font=entry_font,
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#d9d9d9",
        highlightcolor="#ff5a36"
    )
    email.place(relx=0.25, rely=0.280, width=260, height=36)

    label6 = tk.Label(
        frame_2,
        text="Password",
        font=heading_font,
        fg="#333333",
        bg="white"
    )
    label6.place(relx=0.5, rely=0.340, anchor="center")

    show_password = False

    def toggle_password():
        global show_password

        if show_password:
            password.config(show="•")   
            eye_button.config(text="👁")
            show_password = False
        else:
            password.config(show="")   
            eye_button.config(text="🙈")
            show_password = True

    password = tk.Entry(
        frame_2,
        show="•",
        font=entry_font,
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#d9d9d9",
        highlightcolor="#f86b06"
    )
    password.place(relx=0.25, rely=0.370, width=260, height=36)

    eye_button = tk.Button(
        frame_2,
        text="👁",
        command=toggle_password,
        font=("Segoe UI", 10),
        bg="#ff5a36",
        relief="flat",
        bd=0,
        cursor="hand2"
    )

    eye_button.place(relx=0.71, rely=0.370, width=30, height=36)

    def l():
        if password.get() and username.get() and email.get():
            import database as d
            result = d.login(email.get(),password.get(),win)
            if result:
                import dashboard
                dashboard.dashboard_open(win)

    login = tk.Button(
        frame_2,
        text="Login",
        command=l,
        font=button_font,
        bg="#ff5a36",
        fg="white",
        activebackground="#e74c3c",
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2"
    )
    login.place(relx=0.5, rely=0.460, anchor="center", width=260, height=42)

    label7 = tk.Label(
        frame_2,
        text="Or",
        font=("Segoe UI", 11),
        fg="#777777",
        bg="white"
    )
    label7.place(relx=0.5, rely=0.495)

    def s():
        if password.get() and username.get() and ("@gmail.com" in  email.get()):
            import database as d
            d.login_signup(password.get(), username.get(), email.get(),win)
            import dashboard
            dashboard.dashboard_open(win)
        else:
            from tkinter import messagebox
            messagebox.showerror("Error","Fields are incorrect",parent = win)

    signup = tk.Button(
        frame_2,
        text="Sign Up",
        command=s,
        font=button_font,
        bg="white",
        fg="#ff5a36",
        activebackground="#fff3ef",
        activeforeground="#ff5a36",
        relief="solid",
        bd=1,
        cursor="hand2"
    )
    signup.place(relx=0.5, rely=0.560, anchor="center", width=260, height=42)


