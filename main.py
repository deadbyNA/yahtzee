class Scoreboard:
    '''yahtzee scoreboard'''
    def __init__(self):
        self.score = 0
        self.aces_used = False
        self.twos_used = False
        self.threes_used = False
        self.fours_used = False
        self.fives_used = False
        self.sixes_used = False

    def score_aces(self,dice:list):
        score = 0
        for die in dice:
            if die == 1:
                score += 1

        self.aces_used = True   
        self.score += score
        return score
    def score_twos(self,dice:list):
        score = 0
        for die in dice:
            if die == 2:
                score += 2

        self.aces_used = True   
        self.score += score
        return score
    

myCard = Scoreboard()
print(myCard.score_aces([4,1,1,6,1]))
