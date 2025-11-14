# TODO: Fill in the details of the item you plan to buy
orders = {
    "item": "apple",
    "type": "fruit",
    "price_kilo": 100,
    "price_pc": 20,
    "sale": True
}

# TODO: Print the item details in the following format:
"""
Order:
	Name: item name
	Info: item info
	...
"""

def print_order(order):
    for field, details in orders.items():
        print(f"{field}: {details}")

for order in orders:
    print_order(order)
    break