import time
import random
pcpoint=0
firstdone=False
point=0
check4=False
check1=False
choice=""
check3=False
check2=False
choices=["1","2","3"]
print("<===================>\nWelcome to rock paper scissors")
while check4==False:
 if firstdone==True:
     x=input("Would you like to play again?[Y/N]")
     if x.lower()=="y":
       check1=False
       check3=False
       check4=False
       check2=False
     elif x.lower()=="n":
       time.sleep(1)
       print("Goodbye")
       break
     

 while check1==False:
    print("<===================>\n1-Rock\n2-Paper\n3-Scissors")
    x=(input("Please choose an option: "))
    print("<===================>")
    while check3==False:
        if x not in choices:
         x=(input("Pick a valid option from (1-3): "))
        else:
         check3=True

         match x:
            case "1": 
                choice="rock"
                print("you have chosen", choice)
                check1=True
            case "2":
             choice="paper"
             print("you have chosen", choice)
             check1=True        

            case "3":
             choice="scissors"
             print("you have chosen", choice)
             check1=True
    print("Computer is choosing...")
    time.sleep(1)
    c=random.randint(1,3)
    match c:
            case 1: 
              pcchoice="rock"
              print("Computer haschosen", pcchoice)
              
            case 2:
             pcchoice="paper"
             print("Computer has chosen", pcchoice)
      

            case 3:
             pcchoice="scissors"
             print("Computer has chosen", pcchoice)
             time.sleep(1)
    print(choice, "VS", pcchoice)
    if pcchoice==choice:
      time.sleep(1)
      print("Tie, No points given")
    elif (choice=="paper" and pcchoice=="rock") or (choice=="rock" and pcchoice=="scissors") or (choice=="scissors" and pcchoice=="paper"):
      point=point+1
      time.sleep(1)

      print("You won! +1 point (you currently have", point,"point(s))")
      time.sleep(1)
    else:
      pcpoint=pcpoint+1
      time.sleep(1)
      print("You lost! +1 to PC(", pcpoint,"points)")
      time.sleep(1)


    firstdone=True
    
    





    