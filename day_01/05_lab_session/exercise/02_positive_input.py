# # TODO: Ask the user for an input that should be a number
# number = str(float(int(input("Enter number: "))))


# TODO: Then try to convert this into an integer using the following:
# number_converted = int(number)

# The user could provide an invalid integer input (string)
# TODO: Handle this case
def convert(num1):
    running = True
    while running:
        command = input("Enter number: ")

        if command == "exit":
            print("Goodbye")
            running = False
            continue

        try:
            number = float(command )
        except ValueError:
            print(f"{command} is not a number")
            continue

        input_number = abs(number)

        if input_number == int(input_number):

            print(f"{input_number} is {input_number:.0f}")
        else:
            print(f"{input_number} is not a whole number")






        # if number == int(number):
        #     number_converted = abs(number)
        #     print(f"{number} is equal to {number_converted:.0f}")
        # else:
        #     print(f"{number} is not a whole number")
        # pass
        # if number == "exit":
        #     print("Farewell")
        #     running = False



        # try:
        #     number = " "
        # except ValueError:
        #     print("Try again")
        #     pass




        #     continue
        # elif number == str(input_number):
        #     number_converted = int(number)
        #     print(f"{input_number} is not a number")
        #     continue
        # elif number == float(input_number):
        #     number_converted = int(number)
        #     print(f"{input_number} is equal to {number_converted}")
        # elif number == "exit":
        #     running = False
convert(0)

# The user could give a negative number
# TODO: Handle this case

# Challenge: TODO: Give the user infinite times to retry
