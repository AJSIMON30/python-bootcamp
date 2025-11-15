class Score:
    def __init__(self, initial_value=0):
        self.var1 = initial_value

    def __repr__(self):
        return f"Score: {self.var1}"

    def __add__(self,other):
        total = self.var1 + other.var1
        return Score(total)

score1 = Score(10)
score2 = Score(20)
print(score1 + score2)