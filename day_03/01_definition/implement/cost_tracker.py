class CostTracker:

#step1(attributes): setup variables
    def __init__(self):
        self.running = True
        self.expenses = []
        self.main_loop()
#step2(methods):
    def spend(self):
        expense = int(input('Enter expense value: '))
        self.expenses.append(expense)

    def refund(self):
        empty = len(self.expenses)
        if empty:
            self.expenses.pop(-1)
        else:
            print("No expense added")

    def show(self):
        print(self.expenses)
        print("total: ", sum(self.expenses))

#step3(main_loop):
    def main_loop(self):
        while self.running:
            command = input("Command: ")
            if command == "spend":
                self.spend()
            elif command == "refund":
                self.refund()
            elif command == "show":
                self.show()
            elif command == "exit":
                self.running = False

cost_tracker = CostTracker()
# cost_tracker.main_loop()