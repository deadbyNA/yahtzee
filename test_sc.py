import unittest
from scorecard import Scoreboard


class TestNums(unittest.TestCase):
    def test_score_aces(self):
        self.scorecard = Scoreboard()
        ace_score = self.scorecard.score_aces( [1,1,1,4,5])
        self.assertEqual(ace_score, 3,'should be 3')

    def test_score_twos(self):
        self.scorecard = Scoreboard()
        twos_score = self.scorecard.score_twos([2,2,2,1,1])
        self.assertEqual(twos_score, 6, 'should be 4')

    def test_score_threes(self):
        self.scorecard = Scoreboard()
        threes_score = self.scorecard.score_threes([3,3,2,1,1])
        self.assertEqual(threes_score, 6, 'should be 6')

    def test_score_fours(self):
        self.scorecard = Scoreboard()
        fours_score = self.scorecard.score_fours([4,4,4,4,1])
        self.assertEqual(fours_score, 16, 'should be 16')

    def test_score_fives(self):
        self.scorecard = Scoreboard()
        fives_score = self.scorecard.score_fives([5,4,4,4,1])
        self.assertEqual(fives_score, 5, 'should be 5')

    def test_score_sixes(self):
        self.scorecard = Scoreboard()
        sixes_score = self.scorecard.score_sixes([6,6,4,4,1])
        self.assertEqual(sixes_score, 12, 'should be 12')

    def test_score_threekind(self):
        self.scorecard = Scoreboard()
        threeKind_score = self.scorecard.score_threeKind([6,6,6,4,1])
        self.assertEqual(threeKind_score, 23, 'should be 23')

    def test_score_fourkind(self):
        self.scorecard = Scoreboard()
        fourKind_score = self.scorecard.score_fourKind([6,6,6,6,1])
        self.assertEqual(fourKind_score, 25, 'should be 25')

    def test_score_smallStr8_1(self):
        self.scorecard = Scoreboard()
        smallStr8_score = self.scorecard.score_smallStr8([1,2,3,4,3])
        self.assertEqual(smallStr8_score, 30, 'should be 30')

    def test_score_smallStr8_2(self):
        self.scorecard = Scoreboard()
        smallStr8_score = self.scorecard.score_smallStr8([5,2,3,4,6])
        self.assertEqual(smallStr8_score, 30, 'should be 30')

    def test_score_largeStr8(self):
        self.scorecard = Scoreboard()
        largeStr8_score = self.scorecard.score_largeStr8([1,2,3,4,5])
        self.assertEqual(largeStr8_score, 40, 'should be 40')

    def test_score_largeStr8_2(self):
        self.scorecard = Scoreboard()
        largeStr8_score = self.scorecard.score_largeStr8([2,3,4,5,6])
        self.assertEqual(largeStr8_score, 40, 'should be 40')

    def test_score_yahtzee(self):
        self.scorecard = Scoreboard()
        yahtzee_score = self.scorecard.score_yahtzee([2,2,2,2,2])
        self.assertEqual(yahtzee_score, 50, 'should be 50')

    def test_score_chance(self):
        self.scorecard = Scoreboard()
        chance_score = self.scorecard.score_chance([2,2,2,2,2])
        self.assertEqual(chance_score, 10, 'should be 10')
        
    def test_score_fullHouse(self):
        self.scorecard = Scoreboard()
        fullHouse_score = self.scorecard.score_fullHouse([1,1,1,2,2])
        self.assertEqual(fullHouse_score, 25, 'should be 25')

if __name__=='__main__':
    unittest.main()
