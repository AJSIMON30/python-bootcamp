import tkinter

root = tkinter.Tk()
count = tkinter.IntVar(root, value=0)
label = tkinter.Label(root, textvariable=count)
label.pack()


def increment():
    new_value = count.get() + 1
    count.set(new_value)

def decrement():
    new_value1 = count.get() - 1
    count.set(new_value1)


# TODO: Add function to decrement count
increment_button = tkinter.Button(root, text=" add ", command=increment)
increment_button.pack(side="left")

increment_button1 = tkinter.Button(root, text=" deduct ", command=decrement)
increment_button1.pack(side="right")

# TODO: Add button to decrement

root.mainloop()
