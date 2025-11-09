# Ask the cost and pax or count for three separate items
item_cost_1 = int(input("item1_price: "))  # Let the user enter a number
item_count_1 = int(input("item1_count: ")) # Let the user enter a number

item_cost_2 = int(input("item2_price: "))  # Let the user enter a number
item_count_2 = int(input("item2_cost: "))  # Let the user enter a number

item_cost_3 = int(input("item3_price: "))  # Let the user enter a number
item_count_3 = int(input("item3_cost: "))  # Let the user enter a number

# Calculate the total
a1 = (item_cost_1 * item_count_1)
a2 = (item_cost_2 * item_count_2)
a3 = (item_cost_3 * item_count_3)


print(a1 + a2 + a3)

# total = (item_cost_1 * item_count_1) + (item_cost_2 * item_count_2) + (item_cost_3 * item_count_3)
# print(total)