import json


def get_random_category_place(data, category, place):
    # Search in DB the data formatting a result message
    review = data[category][place]["review"]
    city = data[category][place]["city"]
    delivery = data[category][place]["delivery"]
    phone = data[category][place]["phone"]
    address = data[category][place]["address"]
    message = f"You will eat {category} at '{place}'. The rating is: {review}"
    if address != "":
        message += "\n" + f"{place} is in {city}, at {address}"
    if phone != "":
        if delivery == "Si":
            message += "\n" + f"It is possible to have a delivery. Phone: {phone}"
        else:
            message += "\n" + "Is not possible to have a delivery."

    return message


def update_db(data, categories, new_entry, category):

    if "hamburger" not in categories:
        data["hamburger"] = new_entry[category]

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
