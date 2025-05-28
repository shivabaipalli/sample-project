import tkinter as tk
from tkinter import messagebox

# Predefined username and password (for demonstration)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

def authenticate():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Login Success", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Setup the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

# Username Label and Entry
tk.Label(root, text="Username").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

# Password Label and Entry
tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Login Button
tk.Button(root, text="Login", command=authenticate).pack(pady=20)

# Run the application
root.mainloop()