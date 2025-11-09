

def spend(expenses):
    """TODO: Add a new cost in expenses"""
    expense = int(input('Enter expense value: '))
    expenses.append(expense)

def refund(expenses):
    """TODO: Remove the last cost added (if any)"""
    empty = len(expenses)
    if empty:
        expenses.pop(-1)
    else:
        print("No expense added")

def show(expenses):
    """TODO: Print the current list of expenses and total"""
    print(expenses)
    print("total: ",sum(expenses))


def save(expenses):
    with open('receipt.txt', 'w') as file:
        for expense in expenses:
            file.write(str(expense))

def load(expenses):
    with open('receipt.txt', 'r') as file:
        user = file.read().splitlines()

        for number in user:
            expenses.append(int(number))
        return expenses

def main():
    running = True
    expenses = []

    while running:
        command = input("Command: ")
        if command == "spend":
            spend(expenses)
        elif command == "refund":
            refund(expenses)
        elif command == "show":
            show(expenses)
        elif command == "save":
            save(expenses)
        elif command == "load":
            expenses = load()

main()
