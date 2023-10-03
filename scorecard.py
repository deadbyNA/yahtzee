class Scoreboard:
    '''yahtzee scoreboard'''
    def __init__(self):
        self.score = 0
        self.top_score=0
        self.bottom_score =0
        self.aces_used = False
        self.twos_used = False
        self.threes_used = False
        self.fours_used = False
        self.fives_used = False
        self.sixes_used = False
        self.threeKind_used = False
        self.fourKind_used = False
        self.fullHouse_used = False
        self.score_smallStr8_used = False
        self.score_largeStr8_used = False
        self.yahtzee_used = False
        self.chance_used = False

    def score_aces(self,dice:list):
        score = 0
        for die in dice:
            if die == 1:
                score += 1

        self.aces_used = True   
        self.score += score
        self.top_score += score
        return score
    def score_twos(self,dice:list):
        score = 0
        for die in dice:
            if die == 2:
                score += 2

        self.twos_used = True   
        self.score += score
        return score
    def score_threes(self,dice:list):
        score = 0
        for die in dice:
            if die == 3:
                score += 3

        self.threes_used = True   
        self.score += score
        return score
    def score_fours(self,dice:list):
        score = 0
        for die in dice:
            if die == 4:
                score += 4

        self.fours_used = True   
        self.score += score
        return score
    def score_fives(self,dice:list):
        score = 0
        for die in dice:
            if die == 5:
                score += 5

        self.fives_used = True   
        self.score += score
        return score
    def score_sixes(self,dice:list):
        score = 0
        for die in dice:
            if die == 6:
                score += 6

        self.sixes_used = True   
        self.score += score
        return score
    def score_threeKind(self,dice:list):
        dice.sort()
        score = 0
        if dice[0] == dice[1] and dice[1] == dice[2] or dice[1] == dice[2] and dice[2] == dice[3] or dice[2] == dice[3] and dice[3] == dice[4]:
            score = sum(dice)
        if self.threeKind_used == True:
            print('Can\'t use this now.')
        else:
            self.threeKind_used = True 
            print(f'You scored {score} on 3 of a kind')
        
        
        return score
    def score_fourKind(self,dice:list):
        dice.sort()
        score = 0
        if dice[0] == dice[1] and dice[1] == dice[2] and dice[2] == dice[3] or dice[1] == dice[2] and dice[2] == dice[3] and dice[3] == dice[4]:
            score = sum(dice)
        if self.fourKind_used == True:
            print('Can\'t use this now.')
        else:
            self.fourKind_used = True
            print(f'you scared {score} on 4 of a kind')
        
        return score

    def score_smallStr8(self,dice:list):
        dice.sort()
        score = 0
        smallStr8_set = set(dice)
        dice1 = list(smallStr8_set)
        if len(dice1) == 4:
            if dice1 == [1,2,3,4] or dice1 == [2,3,4,5] or dice1 == [3,4,5,6] or dice1 == [1,3,4,5] or dice1 == [1,2,4,5] or dice1 == [1,2,3,5]:
                score = 30
        if len(dice1) == 5:
            if dice1 == [1,2,3,4,5] or dice1 == [2,3,4,5,6] or dice1 == [1,2,3,4,6] or dice1 == [1,3,4,5,6] or dice1 == [1,2,4,5,6] or dice1 == [1,2,3,5,6] or dice1 == [1,2,3,4,6]:
                score = 30
        self.score_smallStr8_used = True
        return score

    def score_largeStr8(self,dice:list):
        dice.sort()
        score = 0
        largeStr8_set = set(dice)
        dice1 = list(largeStr8_set)
        if dice1 == [1,2,3,4,5] or dice1 == [2,3,4,5,6]:
            score = 40
        self.score_largeStr8_used = True
        return score

    def score_yahtzee(self,dice:list):
        dice.sort()
        score = 0
        if dice[0] == dice[4]:
            score = 50
        self.yahtzee_used = True
            
        return score

    def score_yahtzee(self,dice:list):
        dice.sort()
        score = 0
        if dice[0] == dice[4]:
            score = 50
        self.yahtzee_used = True
            
        return score
    def score_chance(self,dice:list):
        self.chance_used = True   
        return sum(dice)

    def score_fullHouse(self,dice:list):
        dice.sort
        score = 0
        if dice[0] == dice[2] and dice[3] == dice[4] or dice[0] == dice[1] and dice[2] == dice[4]:
            score = 25
        self.fullHouse_used = True
        return score





