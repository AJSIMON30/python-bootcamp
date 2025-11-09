with open('sample.txt','r') as file:
    user = file.readlines()
    print(user)



# file = open('sample.txt', 'w')
#



# file = open('sample.txt','a')
#
# lines = [
#     'Hello',
#     'mga',
#     'mamser',
#     'mango',
#     'di po ako makakapasok'
# ]
#
# formated_lines = []
# for line in lines:
#     formated_lines.append(line + '\n')
#
# file.writelines(formated_lines)
#
# file.close()







# num = '123000123123000123'
#
# print(num.lstrip('123'))

# sample = 'hello world i am the king'
#
# words = sample.split()
# print(words)
#
# joined = " ".join(words)
# print(joined)


# sample = '123,123,123,1231,6543'
#
# is_sample = sample.replace('123','456')
# print(sample)
# print(is_sample)

# sample = "hello world! I am learning python"
# input = input("Enter value: ").strip()
# print(f"| {input} |")
#
# print(input == "rock")

# print(sample.endswith("learning python"))



# sample = "qweqwe123123 "
# print(sample)
# print(sample.isalpha())

# pw = input("Enter your password: ")
# lower_case_count = 0
# upper_case_count = 0
#
# for letter in pw:
#     if letter.islower():
#         lower_case_count += 1
#     elif letter.isupper():
#         upper_case_count += 1
#
# print(lower_case_count)
# print(upper_case_count)



# move = input("enter your move: ").islower()
# print(move)


# text = "AJ SIMON"
#
# substring = "SIMON"
# print(substring in text)

# text = "AJ SIMON"
# print(f"|{text:=^20}|")

# price = 15000132.12312312
# print(f'the price is {price:%}')



# country_codes = {
#     "PH": "Philippines",
#     "US": "United States",
#     "SK": "South Korea",
#     "NK": "North Korea",
# }



# country_codes = {
#     "PH": "Philippines",
#     "US": "United States",
#     "SK": "South Korea",
#     "NK": "North Korea",
# }
#
# if "SG" not in country_codes:
#     country_codes["SG"] = "qwerty"
#     print(country_codes["SG"])





# data = {
#     "first name": "John",
#     "last name": "Doe",
#     "age": 25,
#     "city": "New York",
# }
# print(dict(data))


# names = ['a','b','c']
# scores = [1,2,3]
# number = [9,8,7]
#
# records = zip(names,scores)
# print(dict(records))





# names = ['a','b','c']
# scores = [1,2,3]
# value = [9,8,7]
#
# records = {
#     'a':{'score':1,'number': 9},
#
# }
#
# print(records['a'])

#
# print(list(zip(names,scores)))
# print(dict(zip(names,scores)))




# records = {
#     "juan":70,
#     "maria":98,
#     "joseph":81,
#     "elise":80,
# }


# {} - set
# [] - list
# () - tuple



# sample1 = {'a','b','c','d'}
# sample2 = {'e','f','g','h','a','b'}
#
# print(sample1.symmetric_difference(sample2))
# print(sample1 ^ sample2)

# print(sample1.intersection(sample2))
# print(sample1 | sample2)

# print(sample1.union(sample2))
# print(sample1 | sample2)
#
#
#
#
# # attendees = set()
#
#
# while len(attendees) < 10:
# # for item in range(10):
#     name = input("Please enter your name: ")
#     attendees.add(name)
#
# print(attendees)
#
#


# sample = {'a','a','b','a','d','d','c',}
# print(len(sample))
# # sample.discard('123')
# # print(sample)


# sample = [1,4,5,2,3]
#
# for sam in sample:
#     print(sample)
#     sample.pop(-1)
#     print(sample)


# sample = [5,3,1,6,2,33,96]
#
# sample.insert(0,123)
# print(sample)
#


# sample = [5,3,1,6,2,33,96]
#
# # sample.remove(5)
# # print(sample)

# sample = int(input("Enter a number: "))
# sample1 = int(input("Enter a number: "))
# sample2 = int(input("Enter a number: "))
# sample3 = int(input("Enter a number: "))
# sample4 = int(input("Enter a number: "))
#
# total = sample ,sample1 ,sample2 , sample3 , sample4
# # sample = [5,3,87,1,11,4,22,44,77,553,6]
# print(sorted(total))





# example = [1,2,3,4,999,5,6,7,8,9]
# example2 = [2,7,3,5,8,22,455,22]
#
# print(example, example2)
# print(max(example),max(example2))



# food = ['ice cream','rice','spam','eggs']
# item_to_find = 'ice cream'
#
# if item_to_find not in food:
#     print(item_to_find)
# else:
#     print('not found')

# has_spam='spam' in food
# print(has_spam)


# number_cards = ['1','2','3','4','5','6','7','8','9']
# special_cards = ['+2','skip','reverse']
# super_cards = ['0','+4','color']
#
# cards = number_cards + special_cards + super_cards
# print(cards)





# for item in items:
#     for other in others:
#         print(item,other)


# queen = ('x','y','z')
#
# for item, other, queens in zip(items, others, queen):
#     print(items, others, queens)

# item_costs = (100,200,300,400,500)
#
# item_cost1,item_cost2,item_cost3,_,_ = item_costs
# print(item_cost1, item_cost2, item_cost3)