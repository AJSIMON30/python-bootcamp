# Ask the cost and pax or count for three separate items
item_cost_1 = int(input())  # Let the user enter a number
item_count_1 = int(input())  # Let the user enter a number

item_cost_2 = int(input())  # Let the user enter a number
item_count_2 = int(input()) # Let the user enter a number

item_cost_3 = int(input()) # Let the user enter a number
item_count_3 = int(input())# Let the user enter a number

item_total1 = (item_cost_1 * item_count_1)
item_total2 = (item_cost_2 * item_count_2)
item_total3 = (item_cost_3 * item_count_3)

# Calculate the total
total = (item_total1 + item_total2 + item_total3)
print(f'{item_total1} + {item_total2} + {item_total3} = {total}')