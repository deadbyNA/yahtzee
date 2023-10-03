import random
class Dice:
    def __init__(self):
        self.die_1 = Die()
        self.die_2 = Die()
        self.die_3 = Die()
        self.die_4 = Die()
        self.die_5 = Die()

        self.alldice = [self.die_1, self.die_2, self.die_3, self.die_4, self.die_5]
        self.values = [die.value for die in self.alldice]
        
    def roll(self):
        for die in self.alldice:
            die.roll()
        self.values = [die.value for die in self.alldice]
        print(self.values)
class Die:
    def __init__(self):
        self.value = None
        self.rolling = True
    
    def roll(self):
        if self.rolling:
            self.value = random.randint(1,6)

dice = Dice()
dice.roll()