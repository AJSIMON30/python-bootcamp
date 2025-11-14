# TODO: Fill in the details of the items you plan to buy
orders = ({
    "Name": "apple",
    "Info": "fruit",
    "Quantity": 10,
    "Available": True,
},
         {
    "Name": "Banana",
    "Info": "Fruit",
    "Quantity": 20,
    "Available": False,
},
         {
    "Name": "eggplant",
    "Info": "vegetable",
    "Quantity": 500,
    "Available": True,
         })

# TODO: Print the item details in the following format (for each order):
"""
Order:
	Name: item name
	Info: item info
	...
"""
def print_order(order):
    print("Order:")
    for field, details in order.items():
        print(f"\t{field}: {details}")


for order in orders:
    print_order(order)
