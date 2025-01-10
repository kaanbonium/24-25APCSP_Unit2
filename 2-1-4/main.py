#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
import tkinter.font as tkFont

# main window
root = tk.Tk()
root.wm_geometry("200x200")
#root.resizable(False, False)

# create empty frame (new window for components in root)
frame_login = tk.Frame(root)
frame_auth = tk.Frame(root)



# Activate the grid in our new frame
frame_login.grid(row="0", column="1", sticky="news")
frame_auth.grid(row="0", column="0", sticky="news")

def login():
    frame_auth.tkraise()
# Widgets for frame_login

# Username label
lbl_username = tk.Label(frame_login, text='Username:',fg='purple', font=("Times 14"))
lbl_username.pack(padx=50)

# Text Box for Username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack()

# Password label
lbl_username = tk.Label(frame_login, text='Password:',fg='purple', font=("Times 14"))
lbl_username.pack(padx=50)

# Text box for password
ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack()

# Login Button
button_login = tk.Button(frame_login, text='Log in lil bro', command=login)
button_login.pack(pady=10)


# Auth Frame Label
lbl_authorized = tk.Label(frame_auth, text='Authorization Screen', font=("Times 14"))
lbl_authorized.pack(padx=50)


frame_login.tkraise()
root.mainloop()