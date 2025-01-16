import tkinter as tk
import tkinter.font as tkFont

# main window
root = tk.Tk()
root.wm_geometry("200x200")
# root.resizable(False, False)

# create empty frame (new window for components in root)
frame_login = tk.Frame(root)
frame_auth = tk.Frame(root)

# Activate the grid in our new frames
frame_login.grid(row=0, column=0, sticky="news")
frame_auth.grid(row=0, column=0, sticky="news")

# Function to switch to the auth frame
def login():
    frame_auth.tkraise()

# Widgets for frame_login
# Username label
lbl_username = tk.Label(frame_login, text='Username:', fg='purple', font=("Times", 14))
lbl_username.pack(padx=50)

# Text Box for Username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack()

# Password label
lbl_password = tk.Label(frame_login, text='Password:', fg='purple', font=("Times", 14))
lbl_password.pack(padx=50)

# Text box for password
ent_password = tk.Entry(frame_login, bd=3, show="*")  # Hide the password
ent_password.pack()

# Login Button
button_login = tk.Button(frame_login, text='Log in lil bro', command=login)
button_login.pack(pady=10)

# Widgets for frame_auth
lbl_authorized = tk.Label(frame_auth, text='Authorization Screen', font=("Times", 14))
lbl_authorized.pack(padx=50)

# Initially display the login frame
frame_login.tkraise()

# Ensure the window keeps running
root.mainloop()
