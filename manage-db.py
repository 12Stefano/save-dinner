import json
from utils.functions import update_db

list_category = list_place = [
    "     ",
]


# Read from json file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Update list with existing category key
print("Categories already added:")
for category_key in data:
    print(f"  - {category_key}")
    list_category.append(category_key)

category = input("Type new category:\n").lower()
place = input("Type restaurant's name:\n").title()
address = input("Type address:\n").title()
city = input("Type city:\n").title()
delivery = input("Delivery? [Si/No]:\n").title()
phone = input("Phone number (leave null if not presented):\n")
review_num = int(input("Rating from 1 to 5:\n"))
review = ""

if review_num < 1:
    review_num = 1
elif review_num > 5:
    review_num = 5
for _ in range(1, review_num+1):
    review += "★"

new_place = {
        category: {
            place: {
                "review": review,
                "address": address,
                "phone": phone,
                "city": city,
                "delivery": delivery
            }
        }
    }

update_db(data=data, categories=list_category, new_entry=new_place, category=category)