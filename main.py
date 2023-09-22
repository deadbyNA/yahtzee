from scorecard import Scoreboard
myCard = Scoreboard()
'''ones'''
print('the below is the ones.')
print(myCard.score_aces([1,2,3,4,5,]))
print(myCard.score_aces([1,1,3,4,5,]))
print(myCard.score_aces([1,1,1,4,5,]))
print(myCard.score_aces([1,1,1,1,5,]))
print(myCard.score_aces([1,1,1,1,1,]))
print('the above is the ones.')

'''ones'''

'''twos'''
print('the below is the twos.')

print(myCard.score_twos([1,2,3,4,5,]))
print(myCard.score_twos([2,2,3,4,5,]))
print(myCard.score_twos([2,2,2,4,5,]))
print(myCard.score_twos([2,2,2,2,5,]))
print(myCard.score_twos([2,2,2,2,2,]))
print('the above is the ones.')

'''twos'''

'''threes'''
print('the below is the threes.')

print(myCard.score_threes([1,2,3,4,5,]))
print(myCard.score_threes([3,2,3,4,5,]))
print(myCard.score_threes([3,3,3,4,5,]))
print(myCard.score_threes([3,3,3,3,5,]))
print(myCard.score_threes([3,3,3,3,3,]))
print('the above is the threes.')

'''threes'''

'''fours'''
print('the below is the fours.')

print(myCard.score_fours([1,2,3,4,5,]))
print(myCard.score_fours([4,2,3,4,5,]))
print(myCard.score_fours([4,4,3,4,5,]))
print(myCard.score_fours([4,4,4,4,5,]))
print(myCard.score_fours([4,4,4,4,4,]))
print('the above is the fours.')

'''fours'''

'''fives'''
print('the below is the fives.')

print(myCard.score_fives([1,2,3,4,5,]))
print(myCard.score_fives([5,2,3,4,5,]))
print(myCard.score_fives([5,5,3,4,5,]))
print(myCard.score_fives([5,5,5,4,5,]))
print(myCard.score_fives([5,5,5,5,5,]))
print('the above is the fives.')

'''fives'''

'''sixes'''
print('the below is the sixes.')

print(myCard.score_sixes([6,2,3,4,5,]))
print(myCard.score_sixes([6,6,3,4,5,]))
print(myCard.score_sixes([6,6,6,4,5,]))
print(myCard.score_sixes([6,6,6,6,5,]))
print(myCard.score_sixes([6,6,6,6,6,]))
print('the above is the sixes.')

'''sixes'''

'''threeKind'''
print('the below checks for three of a kind')
print(myCard.score_threeKind([1,2,3,4,5,]))
print(myCard.score_threeKind([5,2,3,4,5,]))
print(myCard.score_threeKind([5,5,3,4,5,]))
print(myCard.score_threeKind([5,5,5,4,5,]))
print('the above checks for three of a kind')

'''threeKind'''

'''fourKind'''
print('the below checks four of a kind')
print(myCard.score_fourKind([1,2,3,4,5,]))
print(myCard.score_fourKind([5,2,3,4,5,]))
print(myCard.score_fourKind([5,5,3,4,5,]))
print(myCard.score_fourKind([5,5,5,4,5,]))
print(myCard.score_fourKind([5,5,5,5,1,]))
print('the above checks four of a kind')
'''fourKind'''