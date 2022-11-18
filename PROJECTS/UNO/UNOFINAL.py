import random

welcomemsg='WELCOME TO UNO BY 798\nYOU WILL BE PLAYING AGAINST THE CPU\nThe game consists of 92 card\nThere are 3 types of special cards\ncoloured skip\ncoloured draw 2\ndraw 4\nSpecial cards do not stack'
print(welcomemsg)
maindeck=['+4','+4']
color=['r','b','g','y']
numbers=['1','2','3','4','5','6','7','8','9','+2','skip']
for a in color:
    for b in numbers:
        maindeck.append(a+b)

maindeck*=2
colors={'r':'a red ','b':'a blue ','g':'a green ','y':'a yellow ','+':'a draw '}
cpu=[]
player=[]
bgclr={'r':1,'g':2,'y':3,'b':4,'+':0}
q=input('ENTER ANY KEY TO START')

#DEALING
for i in range(5):
    random.shuffle(maindeck)
cardsperplayer=7
for i in range(2*cardsperplayer):
    if i%2==0:
        cpu.append(maindeck[0])
    else:
        player.append(maindeck[0])
    del maindeck[0]

#STARTING CARD
while 'skip' in maindeck[0] or '+' in maindeck[0]:
    random.shuffle(maindeck)
print(colors[maindeck[0][0]]+maindeck[0][1:],'is the starting card')
cardinplay=maindeck[0]
x=bgclr[cardinplay[0]]
print(u"\u001b[4",x,"m",".------.\u001b[0m\n"
      u"\u001b[4",x,"m|", cardinplay[1], ".--. |\u001b[0m\n"
      u"\u001b[4",x,"m","| :  : |\u001b[0m\n"
      u"\u001b[4",x,"m","| '--'", cardinplay[1],"|\u001b[0m\n"
      u"\u001b[4",x,"m","'______'\u001b[0m", sep='')
print(u"\u001b[0m")
maindeck.remove(cardinplay)

#START AND DRAWING CARDS
turn=0
game=True
while game:
    if turn%2==0:
        invalidcards=True
        while invalidcards:
            for card in player:
                if card[0]==cardinplay[0] or card[1:]==cardinplay[1:] or card[0]=='+' or cardinplay[0]=='+':
                    invalidcards=False

            if invalidcards==True:
                player.append(maindeck[0])
                print("Since you don't have a card which can be played, you have drawn" ,colors[maindeck[0][0]]+maindeck[0][1:])
                del maindeck[0]
        print('Your cards are')#PRINTING THE CARDS
        number = 1
        for a in player:
            print(number, '.', colors[a[0]] + a[1:])
            number += 1
    else:
        invalidcards=True
        while invalidcards:
            for card in cpu:
                if card[0] == cardinplay[0] or card[1:] == cardinplay[1:] or card[0] == '+' or cardinplay[0]=='+':
                    invalidcards = False

            if invalidcards == True:
                cpu.append(maindeck[0])
                print('The CPU has drawn a card')
                del maindeck[0]

    #PLAYING A CARD
    if turn%2==0:
        logic1=True
        while logic1:
            if cardinplay[1:]=='skip':
                print('You have played a skip.',end=' ')
            userinput=int(input('Enter the number of the card you want to play'))
            if userinput>len(player) or userinput<=0:
                print('invalid input')
            elif player[userinput-1][0]==cardinplay[0] or player[userinput-1][1:]==cardinplay[1:] or player[userinput-1][0]=='+' or cardinplay[0]=='+':
                cardinplay=player[userinput-1]
                x=bgclr[cardinplay[0]]
                if '+2' in cardinplay:
                    print(u"\u001b[4",x,"m",".------.\u001b[0m\n"
                          u"\u001b[4",x,"m|", cardinplay[2],".--. |\u001b[0m\n"
                          u"\u001b[4",x,"m| :++: |\u001b[0m\n"
                          u"\u001b[4",x,"m| '--'", cardinplay[2], "|\u001b[0m\n"
                          u"\u001b[4",x,"m'______'\u001b[0m", sep='')
                elif '+4' in cardinplay:
                    print(u"\u001b[4",x,"m",".------.\u001b[0m\n"
                          u"\u001b[4",x,"m|", cardinplay[1],".--. |\u001b[0m\n"
                          u"\u001b[4",x,"m| :++: |\u001b[0m\n"
                          u"\u001b[4",x,"m| '--'", cardinplay[1], "|\u001b[0m\n"
                          u"\u001b[4",x,"m'______'\u001b[0m", sep='')
                elif 'skip' in cardinplay:
                    print(u"\u001b[4",x,"m",".------.\u001b[0m\n"
                          u"\u001b[4",x,"m|", 's',".--. |\u001b[0m\n"
                          u"\u001b[4",x,"m| :ki: |\u001b[0m\n"
                          u"\u001b[4",x,"m| '--'", 'p', "|\u001b[0m\n"
                          u"\u001b[4",x,"m'______'\u001b[0m", sep='')
                else:
                    print(u"\u001b[4",x,"m",".------.\u001b[0m\n"
                          u"\u001b[4",x,"m|", cardinplay[1], ".--. |\u001b[0m\n"
                          u"\u001b[4",x,"m","| :  : |\u001b[0m\n"
                          u"\u001b[4",x,"m","| '--'", cardinplay[1],"|\u001b[0m\n"
                          u"\u001b[4",x,"m","'______'\u001b[0m", sep='')
                print(u"\u001b[0m")

                maindeck.append(cardinplay)
                del player[userinput-1]
                logic1=False
                turn+=1
            else:
                print('invalid input')
    else:
        logic2=True
        while logic2:
            index=0
            while index<len(cpu):
                if cpu[index][0] == cardinplay[0] or cpu[index][1:] == cardinplay[1:] or cpu[index][0] == '+' or cardinplay[0]=='+':
                    cardinplay=cpu[index]
                    print('The CPU has played ',colors[cardinplay[0]]+cardinplay[1:])
                    x=bgclr[cardinplay[0]]
                    if '+2' in cardinplay:
                        print(u"\u001b[4",x,"m",".------.\u001b[0m\n"
                              u"\u001b[4",x,"m|", cardinplay[2],".--. |\u001b[0m\n"
                              u"\u001b[4",x,"m| :++: |\u001b[0m\n"
                              u"\u001b[4",x,"m| '--'", cardinplay[2], "|\u001b[0m\n"
                              u"\u001b[4",x,"m'______'\u001b[0m", sep='')
                    elif '+4' in cardinplay:
                        print(u"\u001b[4",x,"m",".------.\u001b[0m\n"
                              u"\u001b[4",x,"m|", cardinplay[1],".--. |\u001b[0m\n"
                              u"\u001b[4",x,"m| :++: |\u001b[0m\n"
                              u"\u001b[4",x,"m| '--'", cardinplay[1], "|\u001b[0m\n"
                              u"\u001b[4",x,"m'______'\u001b[0m", sep='')
                    elif 'skip' in cardinplay:
                        print(u"\u001b[4",x,"m",".------.\u001b[0m\n"
                              u"\u001b[4",x,"m|", 's',".--. |\u001b[0m\n"
                              u"\u001b[4",x,"m| :ki: |\u001b[0m\n"
                              u"\u001b[4",x,"m| '--'", 'p', "|\u001b[0m\n"
                              u"\u001b[4",x,"m'______'\u001b[0m", sep='')
                    else:
                        print(u"\u001b[4",x,"m",".------.\u001b[0m\n"
                              u"\u001b[4",x,"m|", cardinplay[1], ".--. |\u001b[0m\n"
                              u"\u001b[4",x,"m","| :  : |\u001b[0m\n"
                              u"\u001b[4",x,"m","| '--'", cardinplay[1],"|\u001b[0m\n"
                              u"\u001b[4",x,"m","'______'\u001b[0m", sep='')
                    print(u"\u001b[0m")

                    maindeck.append(cardinplay)
                    del cpu[index]
                    logic2=False
                    index=len(cpu)+1
                    turn+=1
                    print('The CPU has',len(cpu),'cards left')
                else:
                    index+=1

    #SPECIAL CARDS
    if '+' in cardinplay:
        if cardinplay[1]=='+':
            for times in range(2):
                if turn%2==0:
                    player.append(maindeck[0])
                    del maindeck[0]
                else:
                    cpu.append(maindeck[0])
                    del maindeck[0]
        else:
            for times in range(4):
                if turn%2==0:
                    player.append(maindeck[0])
                    del maindeck[0]
                else:
                    cpu.append(maindeck[0])
                    del maindeck[0]
    if 'skip' in cardinplay:
        turn+=1
        if turn%2==0:
            number = 1

    #WINNING THE GAME
    if len(player)==0:
        print('YOU WIN')
        game=False
    if len(cpu)==0:
        print('YOU LOSE')
        game=False