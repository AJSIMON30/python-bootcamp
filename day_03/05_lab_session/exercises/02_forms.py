import json
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

age = tkinter.Label(age_frame,text="Age:    ")
entry_age = tkinter.StringVar(age_frame, value="")
entry_age1 = tkinter.Entry(age_frame, textvariable=entry_age)
age.pack(side="left")
entry_age1.pack(side="right")

theme_frame = tkinter.Frame(root)
theme_frame.pack()

theme = tkinter.Label(theme_frame, text="Preferred Theme:")
select_theme1 = tkinter.StringVar(theme_frame, value="Light")
select_theme2 = tkinter.StringVar(theme_frame, value="Dark")
choices_theme1 = tkinter.Radiobutton(theme_frame, text="Light", variable=select_theme1)
choices_theme2 = tkinter.Radiobutton(theme_frame, text="Dark", variable=select_theme2)
theme.pack(side="left")
choices_theme1.pack(side="right")
choices_theme2.pack(side="right")

subscribe_frame = tkinter.Frame(root)
subscribe_frame.pack()

subscribe = tkinter.BooleanVar()
# subscribe.set()
subscribe_checkbox = tkinter.Checkbutton(subscribe_frame, text="Subscribe to newsletter", variable=subscribe)
subscribe_checkbox.pack(side="right")
# subscribe_checkbox.select()


rate_frame = tkinter.Frame(root)
rate_frame.pack()

rate_value = tkinter.IntVar(rate_frame, value=0)
rate = tkinter.Scale(rate_frame, variable=rate_value, from_=0, to=100, orient="horizontal")
rate.pack(side="right")

class Main:
    def __init__(self):
        self.root = tkinter.Tk()

def save_data(forms):
    data = {
        "Name:" : entry_name.get(),
        "Age:" : entry_age1.get(),
        "Theme:" : select_theme1.get(),
        "Subscribe:" : subscribe.get(),
        "Rating:" : rate_value.get(),
    }
    forms.append(data)
    with open('forms.json', 'w') as file:
        json.dump(forms, file)

def form(event=None):
    if name = entry_name.get():

    age = entry_age1.get()

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


# button = tkinter.Button(root,text="Submit",command=check_password)
# button.pack()

root.mainloop()
