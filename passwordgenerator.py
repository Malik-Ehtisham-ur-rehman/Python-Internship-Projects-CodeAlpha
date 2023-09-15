import tkinter as tk
import string
import random

def generate_password():
    username = username_entry.get()
    password_length = int(length_entry.get())

    if not username:
        password_label.config(text="Please enter a username.")
        return

    if password_length <= 0:
        password_label.config(text="Password length must be greater than 0.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))

    password_label.config(text=f"Generated password for {username}: {password}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password length label and entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Generate password button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Generated password label
password_label = tk.Label(root, text="")
password_label.pack()

# Start the Tkinter event loop
root.mainloop()