# Price notification template
price_notification = "The price of {} is ${}."

# TODO: Post: Latte ($3.5)
post1 = "Latte"
post2 = 3.5
for_print = price_notification.format(post1,post2)
print(for_print)

# TODO: Post: Espresso ($2.75)
post3 = "Espresso"
post4 = 2.75
for_print2 = price_notification.format(post3,post4)
print(for_print2)

# TODO: Post: Cappuccino ($4.0)
post5 = "Cappuccino"
post6 = 4.0
for_print3 = price_notification.format(post5,post6)
print(for_print3)