import tkinter

root = tkinter.Tk()
name_frame = tkinter.Frame(root)
name_frame.pack()

name = tkinter.Label(name_frame, text="Name:")
entry_name = tkinter.StringVar(name_frame, value="")
entry_name1= tkinter.Entry(name_frame, textvariable=entry_name)
name.pack(side="left")
entry_name1.pack(side="right")

age_frame = tkinter.Frame(root)
age_frame.pack()

age = tkinter.Label(age_frame,text="Age:")
entry_age = tkinter.StringVar(age_frame, value="")
entry_age1 = tkinter.Entry(age_frame, textvariable=entry_age)
age.pack(side="left")
entry_age1.pack(side="right")


# def save_data(event=None):
#     data = {
#         "input data"
#     }
# )
# label.pack()
#
# entry_var = tkinter.StringVar(root, value="")
# entry = tkinter.Entry(root, textvariable=entry_var)
# entry.pack()

# TODO: Create StringVar for name
# TODO: Create StringVar for name

# TODO: Create StringVar for age
# TODO: Create StringVar for age

# TODO: Create StringVar for theme
# TODO: Create StringVar for theme

# TODO: Create BooleanVar for subscribe
# TODO: Create BooleanVar for subscribe

# TODO: Create IntVar for rating
# TODO: Create IntVar for rating

# TODO: Create function for saving values to JSON
# TODO: Create button for submit + save

root.mainloop()
