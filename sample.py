

#json
import json

data = [
    {'Name': 'Alice', 'Age': 30, 'Occupation': 'Engineer'},
    {'Name': 'Bob', 'Age': 25, 'Occupation': 'Designer'},
]

with open('people.json', 'w') as file:
    json.dump(data, file)

#
# #tkinter
import tkinter


root = tkinter.Tk()

entry_var = tkinter.StringVar(root, value="")
entry = tkinter.Entry(root, textvariable=entry_var)
entry.pack()

label_var = tkinter.StringVar(root, value="")
label = tkinter.Label(root, textvariable=label_var)
label.pack()

def show_input(event):
    given_text = entry_var.get()
    label_var.set(given_text)
    entry_var.set("")
#
#
# root.bind("<Return>", show_input)
#
# root.mainloop()


# import tkinter
#
# root = tkinter.Tk()
#
# #make a variable
# var1 = tkinter.StringVar(root, value = "Hello World")
# label = tkinter.Label(root, textvariable=var1)
# label.pack()
# root.mainloop()
#


# import tkinter
#
# root = tkinter.Tk()
#
# entry = tkinter.Entry(root)
# entry.pack()
#
# def show_input(event):
#     given_text = entry.get()
#     # print(given_entry)
#     label= tkinter.Label(root,text=given_text)
#     print( )
#
# root.bind("<Tab>", show_input)
# root.bind("<Return>", show_input)
# root.bind("<a>", show_input)
# root.mainloop()


import tkinter

root = tkinter.Tk()
label = tkinter.Label(
    root,
    text="""
    Loops within loops again
    A silent function returns
    The logic is clear
    """,
    font=("Arial", 10, "bold"),
    fg="black",
    bg="red",
    width=100,
    height=100,
    padx=10,
    pady=100
)
label.pack()
root.mainloop()


# import tkinter
# root = tkinter.Tk()
# root.title("Sample GUI Application")
# root.geometry("1200x400")
#
# message = """
# Line1
# Line2
# Line3
# """
# label = tkinter.Label(root, text = message)
# label.pack()
# root.mainloop()



# class CustomError(Exception):
#     pass
#
# raise CustomError("asd")
#
#

# class Parent:
#     def parent_method1(self):
#         print("Parent1 method")
#
#     def parent_method2(self):
#         print("Parent2 method")
#
# class Child(Parent):
#     def child_method(self):
#         print("child method")
#
# child = Child()
# child.parent_method1()
# child.parent_method2()


# class Score:
#     def __init__(self, initial_value=0):
#         self.var1 = initial_value
#
#     def __repr__(self):
#         return f"Score: {self.var1}"
#
#     def __add__(self,other):
#         total = self.var1 + other.var1
#         return Score(total)
#
# score1 = Score(10)
# score2 = Score(20)
# print(score1 + score2)