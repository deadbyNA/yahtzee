import tkinter as tk
import sys
import random

from PIL import ImageTk, Image
from dice import Dice
from scorecard import Scoreboard


dice = Dice()
sc = Scoreboard()

def quit():
    sys.exit()

def update_aces(aceBtn):
    if not sc.aces_used: 
        ace_score =  sc.score_aces(dice.values)
        aceLbl = tk.Label(text=ace_score, padx=49,pady=15, font=('change later',20)).grid(row=4, column=1)

        aceBtn.configure(state = "disabled")
        

def update_twos(twoBtn):
    if not sc.twos_used:
        two_score = sc.score_twos(dice.values)
        twosLbl = tk.Label(text=two_score, padx=49,pady=15, font=('change later',20)).grid(row=5, column=1)
        twoBtn.configure(state = "disabled")

def update_threes(threeBtn):
    if not sc.threes_used:
        three_score = sc.score_threes(dice.values)
        threesLbl = tk.Label(text=three_score, padx=49,pady=15, font=('change later',20)).grid(row=6, column=1)
        threeBtn.configure(state = "disabled")

def update_fours(fourBtn):
    if not sc.fours_used:
        four_score = sc.score_fours(dice.values)
        foursLbl = tk.Label(text=four_score, padx=49,pady=15, font=('change later',20)).grid(row=7, column=1)
        fourBtn.configure(state = "disabled")

def update_fives(fiveBtn):
    if not sc.fives_used:
        five_score = sc.score_fives(dice.values)
        fivesLbl = tk.Label(text=five_score, padx=49,pady=15, font=('change later',20)).grid(row=8, column=1)
        fiveBtn.configure(state = "disabled")

def update_sixes(sixBtn):
    if not sc.sixes_used:
        six_score = sc.score_sixes(dice.values)
        sixesLbl = tk.Label(text=six_score, padx=49,pady=15, font=('change later',20)).grid(row=9, column=1)
        sixBtn.configure(state = "disabled")

def update_3kind(threeKindBtn):
    if not sc.threeKind_used:
        threeKind_score = sc.score_threeKind(dice.values)
        threeKindLbl = tk.Label(text=threeKind_score, padx=49,pady=15, font=('change later',20)).grid(row=4, column=3)
        threeKindBtn.configure(state = "disabled")

def update_4kind(fourKindBtn):
    if not sc.fourKind_used:
        fourKind_score = sc.score_fourKind(dice.values)
        fourKindLbl = tk.Label(text=fourKind_score, padx=49,pady=15, font=('change later',20)).grid(row=5, column=3)
        fourKindBtn.configure(state = "disabled")

def update_full(fullHouseBtn):
    if not sc.fullHouse_used:
        full_score = sc.score_fullHouse(dice.values)
        fullHouseLbl = tk.Label(text=full_score, padx=49,pady=15, font=('change later',20)).grid(row=6, column=3)
        fullHouseBtn.configure(state = "disabled")

def update_small(smallstr8Btn):
    if not sc.score_smallStr8_used:
        small_score = sc.score_smallStr8(dice.values)
        smallstraightLbl = tk.Label(text=small_score, padx=49,pady=15, font=('change later',20)).grid(row=7, column=3)
        smallstr8Btn.configure(state = "disabled")

def update_large(largestr8Btn):
    if not sc.score_largeStr8_used:
        large_score = sc.score_largeStr8(dice.values)
        largeStraightLbl = tk.Label(text=large_score, padx=49,pady=15, font=('change later',20)).grid(row=8, column=3)
        largestr8Btn.configure(state = "disabled")

def update_yahtzee(yahtzeeBtn):
    if not sc.yahtzee_used:
        yahtzee_score = sc.score_yahtzee(dice.values)
        yahtzeeLbl = tk.Label(text=yahtzee_score, padx=49,pady=15, font=('change later',20)).grid(row=9, column=3)
        yahtzeeBtn.configure(state = "disabled")

def update_chance(chanceBtn):
    if not sc.chance_used:
        chance_score = sc.score_chance(dice.values)
        chanceLbl = tk.Label(text=chance_score, padx=49,pady=15, font=('change later',20)).grid(row=10, column=3)
        aceBtn.configure(state = "disabled")
        chanceBtn.configure(state = "disabled")
    


def roll():
    '''command to roll the dice'''
    #randImages = ['images\\transparentdie1.png','images\\transdie2.png','images\\transdie3.png','images\\transdie4.png','images\\transdie5.png']

    if check1_var.get() == 1:
        dice.die_1.rolling = False
    else:
        dice.die_1.rolling = True
    if check2_var.get() == 1:
        dice.die_2.rolling = False
    else:
        dice.die_2.rolling = True
    if check3_var.get() == 1:
        dice.die_3.rolling = False
    else:
        dice.die_3.rolling = True
    if check4_var.get() == 1:
        dice.die_4.rolling = False
    else:
        dice.die_4.rolling = True
    if check5_var.get() == 1:
        dice.die_5.rolling = False
    else:
        dice.die_5.rolling = True
    dice.roll()
    '''
    for value in dice.values:
        print(value)
        print(dice_images[value-1])
    '''
    
    die_spot_1.configure(image=dice_images[dice.values[0]-1])
    die_spot_2.configure(image=dice_images[dice.values[1]-1])
    die_spot_3.configure(image=dice_images[dice.values[2]-1])
    die_spot_4.configure(image=dice_images[dice.values[3]-1])
    die_spot_5.configure(image=dice_images[dice.values[4]-1])

    '''command to roll the dice'''

#Window details
window = tk.Tk()
window.title('Yahtzee Baby!')
#Window details
roll_count = 0
def randice():
    roll()
    global roll_count
    #randposition = [die_spot_1, die_spot_2, die_spot_3, die_spot_4, die_spot_5]
    #print(random.randint(1,6))
    roll_count += 1
    if roll_count ==3:
        rollBtn.config(state="disabled")

#roll
rollBtn = tk.Button(text='Roll', padx=30, pady=15, font=('change later',20), command=randice )
rollBtn.place(x=1750, y=900)
#roll

def create_checkboxes():
    '''creates checkboxes to decide if user wants to keep dice or not'''
    global check1_var
    global check2_var
    global check3_var
    global check4_var
    global check5_var
    check1_var = tk.IntVar()
    check2_var = tk.IntVar()
    check3_var = tk.IntVar()
    check4_var = tk.IntVar()
    check5_var = tk.IntVar()

    check1 = tk.Checkbutton(text="Keep?", font= ('change later', 15), variable=check1_var, onvalue=1, offvalue=0).grid(row= 2, column=0)
    check2 = tk.Checkbutton(text="Keep?", font= ('change later', 15), variable=check2_var, onvalue=1, offvalue=0).grid(row= 2, column=1)
    check3 = tk.Checkbutton(text="Keep?", font= ('change later', 15), variable=check3_var, onvalue=1, offvalue=0).grid(row= 2, column=2)
    check4 = tk.Checkbutton(text="Keep?", font= ('change later', 15), variable=check4_var, onvalue=1, offvalue=0).grid(row= 2, column=3)
    check5 = tk.Checkbutton(text="Keep?", font= ('chang later', 15), variable=check5_var, onvalue=1, offvalue=0).grid(row= 2, column=4)
    '''creates checkboxes to decide if user wants to keep dice or not'''

    '''checks to see if player wants to keep dice'''

    '''checks to see if player wants to keep dice'''

#def create_yahtzee_btns():
'''creates buttons for user to decide what points they want'''
aceBtn = tk.Button(text='Aces', padx=49, pady=15, font=('change later',20 ), command=lambda:update_aces(aceBtn))
aceBtn.grid(row=4, column =0)
twoBtn = tk.Button(text='Twos', padx=48, pady=15, font=('change later',20 ), command=lambda:update_twos(twoBtn))
twoBtn.grid(row=5, column =0)
threeBtn = tk.Button(text='Threes', padx=38, pady=15, font=('change later',20 ), command=lambda:update_threes(threeBtn))
threeBtn.grid(row=6, column =0)
fourBtn = tk.Button(text='Fours', padx=45, pady=15, font=('change later',20 ), command= lambda:update_fours(fourBtn))
fourBtn.grid(row=7, column =0)
fiveBtn = tk.Button(text='Fives', padx=47, pady=15, font=('change later',20 ), command=lambda:update_fives(fiveBtn))
fiveBtn.grid(row=8, column =0)
sixBtn = tk.Button(text='Sixes', padx=47, pady=15, font=('change later',20 ),command=lambda:update_sixes(sixBtn))
sixBtn.grid(row=9, column =0)
threeKindBtn = tk.Button(text='3Kind', padx=45, pady=15, font=('change later',20 ),command=lambda:update_3kind(threeKindBtn))
threeKindBtn.grid(row=4, column =2)
fourKindBtn = tk.Button(text='4Kind', padx=45, pady=15, font=('change later',20 ),command=lambda:update_4kind(fourKindBtn))
fourKindBtn.grid(row=5, column =2)
fullHouseBtn = tk.Button(text='FullHouse', padx=18, pady=15, font=('change later',20 ),command=lambda:update_full(fullHouseBtn))
fullHouseBtn.grid(row=6, column =2)
smallstr8Btn = tk.Button(text='SmallStr8', padx=20, pady=15, font=('change later',20 ),command=lambda:update_small(smallstr8Btn))
smallstr8Btn.grid(row=7, column =2)
largestr8Btn = tk.Button(text='LargeStr8', padx=19, pady=15, font=('change later',20 ),command=lambda:update_large(largestr8Btn))
largestr8Btn.grid(row=8, column =2)
yahtzeeBtn = tk.Button(text='Yahtzee', padx=29, pady=15, font=('change later',20 ),command=lambda:update_yahtzee(yahtzeeBtn))
yahtzeeBtn.grid(row=9, column =2)
chanceBtn = tk.Button(text='Chance', padx=32, pady=15, font=('change later',20 ),command=lambda:update_chance(chanceBtn))
chanceBtn.grid(row=10, column =2)
'''creates buttons for user to decide what points they want'''
bonus = tk.Label(text='Bonus', padx=49, pady=15, font=('change later',20)).grid(row=10, column=0)

def create_score_labels():
    '''creates how many points are in each type of score'''
    
    bonusLbl = tk.Label(text='Change', padx=49,pady=15, font=('change later',20)).grid(row=10, column=1)

    '''creates how many points are in each type of score'''



        


upper=tk.Label(text=f'Upper Score is:{sc.top_score}',padx=49,pady=15,font=('change later',20))

upper.grid(row=4,column=4)
lower=tk.Label(text='Lower Score is:',padx=49,pady=15,font=('change later',20)).grid(row=5,column=4)
total=tk.Label(text='Total Score is:',padx=49,pady=15,font=('change later',20)).grid(row=6,column=4)

#creates image of dice and location
die1_image = ImageTk.PhotoImage(Image.open('images\\transparentdie1.png'))
die2_image = ImageTk.PhotoImage(Image.open('images\\transdie2.png'))
die3_image = ImageTk.PhotoImage(Image.open('images\\transdie3.png'))
die4_image = ImageTk.PhotoImage(Image.open('images\\transdie4.png'))
die5_image = ImageTk.PhotoImage(Image.open('images\\transdie5.png'))
die6_image = ImageTk.PhotoImage(Image.open('images\\transdie6.png'))
dice_images = [die1_image, die2_image, die3_image, die4_image, die5_image,die6_image]

die_spot_1 = tk.Label(image= die1_image)
die_spot_1.grid(row=1, column=0,padx=30, pady=10)
die_spot_2 = tk.Label(image=die2_image)
die_spot_2.grid(row=1, column=1,padx=30, pady=10)
die_spot_3 = tk.Label(image=die3_image)
die_spot_3.grid(row=1, column=2,padx=35, pady=10)
die_spot_4 = tk.Label(image=die4_image)
die_spot_4.grid(row=1, column=3,padx=35, pady=10)
die_spot_5 = tk.Label(image=die5_image)
die_spot_5.grid(row=1, column=4,padx=35, pady=10)
#creates image of dice and location



line = tk.Label(text='______________________________________________________', pady=10).grid(row=3, column=0, columnspan=5)

#create_yahtzee_btns()
#create_total_scores()
create_checkboxes()
create_score_labels()
randice()
window.mainloop()