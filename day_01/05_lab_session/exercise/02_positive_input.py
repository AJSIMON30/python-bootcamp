# TODO: Ask the user for an input that should be a number


# TODO: Then try to convert this into an integer using the following:
number_converted = int(number)

# The user could provide an invalid integer input (string)
# TODO: Handle this case

# The user could give a negative number
# TODO: Handle this case

# Challenge: TODO: Give the user infinite times to retry

try:
    for_convert = input("Enter number: ")
    number
    print(number)
except ValueError:
    print("Enter valid number!")
