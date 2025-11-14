import json

def add(inventory):
    """TODO:
        Ask for item name, info, and stock
        Create a dictionary with key: name, info, stock
        Add that dictionary to inventory
    """
    name = input("Item name: ")
    info = input("Item info: ")
    stock = int(input("Item stock: "))

    item = {
        "name": name,
        "info": info,
        "stock": stock,
    }
    inventory.append(item)

def remove(inventory):
    """TODO:
        Ask for item index (int)
        Remove item in that index in inventory
    """
    index = int(input("Item index: "))
    if 0 <= index < len(inventory):
        rem_item = inventory.pop(index)
        print(f"Item Removed: {rem_item}")
    else:
        print("Invalid index! No Item Removed")

def read(inventory):
    """TODO:
        Ask for item index (int)
                Show item in that index in inventory
    """
    index = int(input("Item index: "))
    if 0 <= index < len(inventory):
        print(inventory[index])
    else:
        print("Invalid index")

def print_item(item):
    for field in item:
        print(f"{field}: {item[field]}")

def show(inventory):
    """TODO: Print items line-by-line"""
    for item in inventory:
        print_item(item)

def save(inventory):
    with open('inventory.json', 'w') as file:
        json.dump(inventory, file)

def load(inventory):
    with open('inventory.json', 'r') as file:
        return json.load(file)


def main():
    """Created to test functions"""
    running = True
    inventory=[]

    while running:
        command = input("Command: ")
        if command == "add":
            # TODO: Use add command"""
            add(inventory)
            pass
        elif command == "remove":
            #  TODO: Use remove command"""
            remove(inventory)
            pass
        elif command == "read":
            # TODO: Use read command"""
            read(inventory)
            pass
        elif command == "show":
            # TODO: Use show command"""
            show(inventory)
            pass
        elif command == "save":
            save(inventory)
            pass
        elif command == "load":
            inventory = load(inventory)
            print(f" Loaded {inventory} items")
            pass
        elif command == "exit":
            running = False



def print_order(order):
    for field, details in orders.items():
        print(f"{field}: {details}")

for order in orders:
    print_order(order)
    break

main()
