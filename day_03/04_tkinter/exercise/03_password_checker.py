import tkinter

root = tkinter.Tk()

label_var = tkinter.StringVar(root, value="Enter your password")
label = tkinter.Label(
    root,
    textvariable=label_var,
    font=("Arial", 10, "bold"),
    fg="black"

)
label.pack()

entry_var = tkinter.StringVar(root, value="")
entry = tkinter.Entry(root, textvariable=entry_var)
entry.pack()

# TODO: Add label for instructions
# TODO: Add entry for instructions
# TODO: Add StringVar for instruction
# TODO: Add label using StringVar


def check_password(event=None):
    correct_password = "pass"
    if entry_var.get() == correct_password:
        label_var.set("Password correct! Access granted")
        label.config(highlightcolor="green")
        entry_var.set("")

    else:
        label_var.set("Incorrect password. Try again")


    # TODO: Check if entry.get() has correct value


# TODO: Add key bindings for check_password

button = tkinter.Button(root,text="Submit",command=check_password)
button.pack()

root.bind("<Return>", check_password)

root.mainloop()
