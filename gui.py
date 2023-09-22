import tkinter as tk
import sys
import random

from PIL import ImageTk, Image
def quit():
    sys.exit()




#Window details
window = tk.Tk()
window.geometry('1080x1920')
window.title('Yahtzee Baby!')
#Window details

def randice():
    randposition = [die_spot_1, die_spot_2, die_spot_3, die_spot_4, die_spot_5]
    print(random.randint(1,6))
#    rollBtn.config(state="disabled")

#roll
rollBtn = tk.Button(text='Roll', padx=30, pady=15, font=('change later',20), command=randice )
rollBtn.place(x=940, y=1760)
#roll

def create_checkboxes():
    '''creates checkboxes to decide if user wants to keep dice or not'''
    check1 = tk.Checkbutton(text="Keep?", font= ('change later', 15)).grid(row= 2, column=0)
    check2 = tk.Checkbutton(text="Keep?", font= ('change later', 15)).grid(row= 2, column=1)
    check3 = tk.Checkbutton(text="Keep?", font= ('change later', 15)).grid(row= 2, column=2)
    check4 = tk.Checkbutton(text="Keep?", font= ('change later', 15)).grid(row= 2, column=3)
    check5 = tk.Checkbutton(text="Keep?", font= ('change later', 15)).grid(row= 2, column=4)
    '''creates checkboxes to decide if user wants to keep dice or not'''
def create_yahtzee_btns():
    '''creates buttons for user to decide what points they want'''
    aceBtn = tk.Button(text='Aces', padx=49, pady=15, font=('change later',20 )).grid(row=4, column =0)
    twoBtn = tk.Button(text='Twos', padx=48, pady=15, font=('change later',20 )).grid(row=5, column =0)
    threeBtn = tk.Button(text='Threes', padx=38, pady=15, font=('change later',20 )).grid(row=6, column =0)
    fourBtn = tk.Button(text='Fours', padx=45, pady=15, font=('change later',20 )).grid(row=7, column =0)
    fiveBtn = tk.Button(text='Fives', padx=47, pady=15, font=('change later',20 )).grid(row=8, column =0)
    sixBtn = tk.Button(text='Sixes', padx=47, pady=15, font=('change later',20 )).grid(row=9, column =0)
    threeKindBtn = tk.Button(text='3Kind', padx=45, pady=15, font=('change later',20 )).grid(row=4, column =2)
    fourKindBtn = tk.Button(text='4Kind', padx=45, pady=15, font=('change later',20 )).grid(row=5, column =2)
    fullHouseBtn = tk.Button(text='FullHouse', padx=18, pady=15, font=('change later',20 )).grid(row=6, column =2)
    smallstr8Btn = tk.Button(text='SmallStr8', padx=20, pady=15, font=('change later',20 )).grid(row=7, column =2)
    largestr8Btn = tk.Button(text='LargeStr8', padx=19, pady=15, font=('change later',20 )).grid(row=8, column =2)
    yahtzeeBtn = tk.Button(text='Yahtzee', padx=29, pady=15, font=('change later',20 )).grid(row=9, column =2)
    chanceBtn = tk.Button(text='Chance', padx=32, pady=15, font=('change later',20 )).grid(row=10, column =2)
    '''creates buttons for user to decide what points they want'''
bonus = tk.Label(text='Bonus', padx=49, pady=15, font=('change later',20)).grid(row=10, column=0)

#creates image of dice and location
die1_image = ImageTk.PhotoImage(Image.open('images\\dice1.png'))
die2_image = ImageTk.PhotoImage(Image.open('images\\dice2.png'))
die3_image = ImageTk.PhotoImage(Image.open('images\\dice3.png'))
die4_image = ImageTk.PhotoImage(Image.open('images\\dice4.png'))
die5_image = ImageTk.PhotoImage(Image.open('images\\dice5.png'))

die_spot_1 = tk.Label(image= die1_image).grid(row=1, column=0,padx=25, pady=10)
die_spot_2 = tk.Label(image=die2_image).grid(row=1, column=1,padx=25, pady=10)
die_spot_3 = tk.Label(image=die3_image).grid(row=1, column=2,padx=25, pady=10)
die_spot_4 = tk.Label(image=die4_image).grid(row=1, column=3,padx=25, pady=10)
die_spot_5 = tk.Label(image=die5_image).grid(row=1, column=4,padx=25, pady=10)
#creates image of dice and location



line = tk.Label(text='______________________________________________________', pady=10).grid(row=3, column=0, columnspan=5)

create_yahtzee_btns()
create_checkboxes()
window.mainloop()
