import tkinter as tk
import random as rd
import json
from utils.functions import get_random_category_place


# -------------------------- GLOBAL VARIABLES --------------------------- #
FONT = ("Arial", 12)
category = ""
place = ""
list_category = list_place = [
    "     ",
]


# Read from json file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Update list with existing category key
for category_key in data:
    list_category.append(category_key)


# -------------------------- UI ACTIONS --------------------------- #
def random_function():
    # Category and place randomly chosen
    category = rd.choice(list(data))
    place = rd.choice(list(data[category]))
    # Formatting the output message
    message = get_random_category_place(data=data, category=category, place=place)
    # Update Result view
    label_result["text"] = message


def get_category(*args):
    # Get category chosen and reset all fields
    category = variable_place_by_category.get()
    if category not in ["     ", ""]:
        variable_info_category.set(list_category[0])
        place = rd.choice(list(data[category]))
        # Formatting the output message
        message = get_random_category_place(data=data, category=category, place=place)
        # Update Result view
        label_result["text"] = message


def set_place_list(*args):
    # Get category chosen and reset fields
    category = variable_info_category.get()
    variable_place_by_category.set(list_category[0])
    label_result["text"] = ""
    if category not in ["     ", ""]:
        # Reset var and delete all old options
        variable_place.set("     ")
        info_place['menu'].delete(0, 'end')
        # Update second menu as submenu with existing place
        for place_key in data[category]:
            info_place['menu'].add_command(label=place_key, command=tk._setit(variable_place, place_key))
    else:
        variable_place.set("     ")
        info_place['menu'].delete(0, 'end')


def get_info(*args):
    # Get category chosen
    category = variable_info_category.get()
    # Get place chosen and reset all fields
    place = variable_place.get()

    if place not in ["     ", ""]:
        # Formatting the output message
        message = get_random_category_place(data=data, category=category, place=place)
        # Update Result view
        label_result["text"] = message


def reset():
    label_result["text"] = ""
    variable_place_by_category.set(list_category[0])
    variable_info_category.set(list_category[0])
    variable_place.set("     ")
    info_place['menu'].delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Where we will eat?")
window.config(padx=50, pady=50)

# Logo
canvas = tk.Canvas(width=400, height=200)
locker_img = tk.PhotoImage(file="utils/logo.png")
canvas.create_image(200, 100, image=locker_img)
canvas.grid(row=0, column=1)

# Button
button_all_random = tk.Button(text="Start", command=random_function, width=10)
button_all_random.grid(row=2, column=0)

button_reset = tk.Button(text="Reset", command=reset, width=10)
button_reset.grid(row=5, column=2)

# Label
label_place_random = tk.Label(text="Random Choice", font=FONT, width=20)
label_place_random.grid(row=1, column=0)
label_place_random.config(padx=5, pady=5)

label_place_by_categosies = tk.Label(text="Random Place", font=FONT, width=20)
label_place_by_categosies.grid(row=1, column=1)
label_place_by_categosies.config(padx=5, pady=5)

label_get_info = tk.Label(text="Get Info", font=FONT, width=10)
label_get_info.grid(row=1, column=2)
label_get_info.config(padx=5, pady=5)

label_result = tk.Label(text="", font=FONT, width = 50, height=10)
label_result.grid(row=4, column=0, columnspan=3)


# Option List
variable_place_by_category = tk.StringVar(window)
variable_place_by_category.set(list_category[0])

place_by_categosies = tk.OptionMenu(window, variable_place_by_category, *list_category)
place_by_categosies.config(width=10, font=('Helvetica', 12))
place_by_categosies.grid(row=2, column=1)

variable_place_by_category.trace("w", get_category)

variable_info_category = tk.StringVar(window)
variable_info_category.set(list_category[0])

info_category = tk.OptionMenu(window, variable_info_category, *list_category)
info_category.config(width=10, font=('Helvetica', 12))
info_category.grid(row=2, column=2)

variable_info_category.trace("w", set_place_list)

variable_place = tk.StringVar(window)
variable_place.set(list_place[0])

info_place = tk.OptionMenu(window, variable_place, *list_place)
info_place.config(width=10, font=('Helvetica', 12))
info_place.grid(row=3, column=2)

variable_place.trace("w", get_info)

window.mainloop()
