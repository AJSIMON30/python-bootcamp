class Character:
    def __init__(self, health=10, defense=10):
        self.var1 = health
        self.var2 = defense

    def attack(self, other):
        damage = 2 - other.var2
        other.var1 -= damage

player = Character()
enemy = Character()

player.attack(enemy)
print(enemy.var1)