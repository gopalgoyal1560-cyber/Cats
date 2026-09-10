import tkinter as tk
from PIL import Image, ImageTk

start = tk.Tk()
start.title("Cat Cafe & Adoption Management System")
start.geometry("1400x800")    

start.update()

img = Image.open("img.png")
img = img.resize((start.winfo_width(), start.winfo_height()), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)

bg = tk.Label(start, image=photo)
bg.place(x=0, y=0, relwidth=1, relheight=1)

def call():
    import login as l
    l.a(start)

button = tk.Button(
    start,
    text="🐾 Get Started",
    bg="#F97F05",
    fg="white",
    font=("Segoe UI", 18, "bold"),
    relief="flat",
    padx=30,
    pady=10,
    command=call
)

button.place(relx=0.5, rely=0.87, anchor="center")

start.mainloop()