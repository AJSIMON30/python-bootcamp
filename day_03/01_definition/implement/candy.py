class Candy:
    def __init__(self,flavor):
        self.var1 = flavor

    def __eq__(self, other):
        return self.var1 == other.flavor

choco1 = Candy("chocolate")
choco2 = Candy("chocolate")
milk = Candy("milk")

print(choco1 == choco2)
print(choco1 == milk)
