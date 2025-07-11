
import tkinter as tk
from tkinter import filedialog, messagebox

def open_register_window(root):
    def submit():
        if not entry_name.get() or not entry_crime.get():
            messagebox.showerror("Missing Data", "Name and Crime fields are required.")
            return
        messagebox.showinfo("Success", "Criminal Registered (Dummy Functionality)")

    window = tk.Toplevel(root)
    window.title("Register Criminal")
    tk.Label(window, text="Name").pack()
    entry_name = tk.Entry(window)
    entry_name.pack()
    tk.Label(window, text="Crime").pack()
    entry_crime = tk.Entry(window)
    entry_crime.pack()
    tk.Button(window, text="Register", command=submit).pack(pady=10)
