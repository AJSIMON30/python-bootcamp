class Wallet:
    def __init__(self, initial_amount=0):
        self.var1 = initial_amount

wallet1 = Wallet(100)
wallet1.var1 /= 2
print(wallet1.var1)

wallet2 = Wallet(500)
print(wallet2.var1)
