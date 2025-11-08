total = 0
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        number = int(input("number: "))
        total += number
        print("total: " , total)
    if command == "sub":
        number = int(input("number: "))
        total -= number
        print("total: ", total)
    elif command == "exit":
        running = False
