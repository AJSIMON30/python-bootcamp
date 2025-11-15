class InvalidAmount(ValueError):
    pass

class WithdrawAmount1Error(ValueError):
    pass

class WithdrawAmount2Error(ValueError):
    pass
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount <0:
            raise InvalidAmount("Please deposit valid amount")
        self.__balance += int(amount)

    def withdraw(self, amount):
        if amount < 0:
            raise WithdrawAmount1Error("Please withdraw valid amount")
        if amount > self.__balance:
            raise WithdrawAmount2Error("Insufficient Balance")
        self.__balance -= amount

    def balance(self):
        print(self.__balance)




bank_account = BankAccount(-1000)
bank_account.deposit(100)
bank_account.withdraw(-100)
bank_account.balance()