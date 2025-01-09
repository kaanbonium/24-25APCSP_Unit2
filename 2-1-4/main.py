#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.resizable(False, False)

# create empty frame (new window for components in root)
frame_login = tk.Frame(root)

# Activate the grid in our new frame
frame_login.grid()

# Widgets for frame_login
lbl_username = tk.Label(frame_login, text='Username:',fg='red', font=("Times 14"))
lbl_username.pack(padx=50, pady=50)

# Text Box for Username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

root.mainloop()