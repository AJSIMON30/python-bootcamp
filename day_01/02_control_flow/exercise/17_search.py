items = ["rice", "noodles", "toyo", "spam", "coffee"]
item_to_find = "toyo"

item_found = False

for item in items:
    print(">")
    if item == item_to_find:

        print(item)
        continue

