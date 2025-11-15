class CashPayment:
    def __init__(self, amount):
        self.amount = amount

    def total(self):
        return self.amount

class CreditPayment:
    def __init__(self, amount, limit):
        """Set attributes here"""
        self.var1 = amount
        self.var2 = limit

    def total(self):
        """Raise error if amount is beyond limit"""
        if self.var1 > self.var2:
            raise ValueError("Amount is greater than the limit")

        return self.var1

class OnlinePayment:
    def __init__(self, amount, fee):
        """Set attributes here"""
        self.var3 = amount
        self.var4 = fee

    def total(self):
        """Return amount + fee"""
        return self.var3 + self.var4


class DiscountedPayment:
    def __init__(self, amount, discount):
        """Set attributes here"""
        self.var5 = amount
        self.var6 = discount

    def total(self):
        """Return amount - discount"""
        return self.var5 - self.var6


payments = [
    CashPayment(1_000),
    CashPayment(10_000),
    CreditPayment(5000, 10000),
    DiscountedPayment(5000, 1000)
]

for payment in payments:
    print(payment.total())
