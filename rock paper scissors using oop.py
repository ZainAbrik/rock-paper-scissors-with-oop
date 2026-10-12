import math
import random
class rockpaperscissors():
    def __init__(self):
        global pcpoints
        global userpoints
        global player2points
        pcpoints=0
        userpoints=0
        player2points=0
    def userchoice(self):
        while True:
            x=input("enter choice (1-3): ")
            global userpick
            global pcpoints
            global userpoints
            match x:
                case"1":
                    userpick=int(x)
                    print("you picked rock")
                    break
                case"2":
                    userpick=int(x)
                    print("you picked paper")
                    break
                case"3":
                    userpick=int(x)
                    print("you picked scissors")
                    break
                case _:
                    print("pick something from 1-3")
    def player2(self):
        global player2pick
        while True:
            x=input("player2 enter choice (1-3): ")
            match x:
                case"1":
                    player2pick=int(x)
                    print("player2 picked rock")
                    break
                case"2":
                    player2pick=int(x)
                    print("player2 picked paper")
                    break
                case"3":
                    player2pick=int(x)
                    print("player2 picked scissors")
                    break
                case _:
                    print("pick something from 1-3")
            
    def pcchoice(self):
        global pcpick
        pcpick=random.randint(1,3)
        match pcpick:
            case 1:
                print("pc picked rock")
            case 2:
                print("pc picked paper")
            case 3:
                print("pc picked scissors")
    def pc_user_comparator(self):
        global pcpoints
        global userpoints
        if userpick==1 and pcpick==3 or userpick==2 and pcpick==1 or userpick==3 and pcpick==2:
            print("user won")
            userpoints+=1
        elif userpick==pcpick:
            print("tie")
        else:
            print("pc won")
            pcpoints+= 1
    def user_player2_comparator(self):
        global userpoints
        global player2points
        global userpick
        global player2points
        if userpick==1 and player2pick==3 or userpick==2 and player2pick==1 or userpick==3 and player2pick==2:
            print("user won")
            userpoints+=1
        elif userpick==player2pick:
            print("tie")
        else:
            print("player2 won")
            player2points+=1
        if userpoints>player2points:
            print(f"the score is {userpoints}-{player2points} to player1")
        elif userpoints<player2points:
            print(f"the score is {player2points}-{userpoints} to player2")    
        else:
            print(f"scores tied at {userpoints}-{userpoints}")    
        
    def score(self):
        if pcpoints>userpoints:
            print(f"the score is {pcpoints}-{userpoints} to PC")
        elif pcpoints==userpoints:
            print(f"its a tie score is {pcpoints}-{userpoints}")
        else:
            print(f"the score is {userpoints}-{pcpoints} to User")
system=rockpaperscissors()
while True:
    print("====RPS====")
    print("1.play with cpu")
    print("2.play 2player")
    print("3.score")
    print("4.exit")
    x=input("pick an option from 1-4: ")
    match x:
        case "1":
            system.userchoice()
            system.pcchoice()
            system.pc_user_comparator()
        case "2":
            system.userchoice()
            system.player2()
            system.user_player2_comparator()
        case "3":
            system.score()
        case "4":
            break
        case _:
            print("pick between 1-4")


