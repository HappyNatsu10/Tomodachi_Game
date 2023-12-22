import random, os
import tkinter
from tkinter import messagebox

path ='C:/Users/Scathach/Documents/Lightshot/'

def action():
    decision = yes_var.get()

    if decision == "yes":
        username = name_entry.get()
        if username:
            fate = random.randint(1, 2)
            if fate == 1:
                os.rmdir(path)
                tkinter.messagebox.showinfo(title='Important', message=f"A File or Folder is missing, Search for it \nYour fate is {fate}")
                tkinter.messagebox.showinfo(title='Important', message=f"It's not my fault. \n Warned ya {username} 😂😂" )
            else:
                tkinter.messagebox.showerror(title="XOXOXOXO",message="You have been hacked")
                tkinter.messagebox.showinfo(title='Important', message=f"You don't what God did for you \nYour fate is {fate} \n{username}, Lucky You")
        else:
            tkinter.messagebox.showwarning(title="Error", message="Enter Username")
    else:
        tkinter.messagebox.showwarning(title="Error", message="Accept the Terms to proceed")


window = tkinter.Tk()
window.title("Tomodachi Game")

frame = tkinter.Frame(window)
frame.pack()

info_frame = tkinter.LabelFrame(frame, text="User Info")
info_frame.grid(row=0, column=0, padx=20, pady=10)

name_label = tkinter.Label(info_frame, text="Username")
name_entry = tkinter.Entry(info_frame)
name_entry.grid(row=1, column=0)
name_label.grid(row=0, column=0)

for widget in info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


terms_frame = tkinter.LabelFrame(frame, text="Terms and Conditions")

yes_var = tkinter.StringVar(value="no")
terms_check = tkinter.Checkbutton(terms_frame, text="The Creator is not responsible for anything",
                                  variable=yes_var, onvalue="yes", offvalue="no")

terms_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)
terms_check.grid(row=0, column=0)

for widget in terms_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


button = tkinter.Button(frame, text="Start", command=action)
button.grid(row=2, column=0, sticky="news", padx=20, pady=10)


window.mainloop()