import tkinter
root = tkinter.Tk()
root.title("Pyhton Haiku")
root.geometry("250x100")

message = """
Loops within loops again
A silent function returns
The logic is clear
"""

label = tkinter.Label(root, text = message)
label.pack()
root.mainloop()

# TODO: Show message using a label

