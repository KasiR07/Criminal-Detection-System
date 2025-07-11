
import tkinter as tk
from register import open_register_window
from facerec import open_detect_window
from surveillance import open_surveillance_window

root = tk.Tk()
root.title("Criminal Detection System")
root.geometry("600x400")

tk.Label(root, text="Criminal Detection System", font=("Arial", 24)).pack(pady=40)

tk.Button(root, text="Register Criminal", width=25, height=2, command=lambda: open_register_window(root)).pack(pady=10)
tk.Button(root, text="Detect Criminal", width=25, height=2, command=lambda: open_detect_window(root)).pack(pady=10)
tk.Button(root, text="Video Surveillance", width=25, height=2, command=lambda: open_surveillance_window(root)).pack(pady=10)

root.mainloop()
