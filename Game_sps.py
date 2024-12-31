import random
import time
def game():
    computer=["stone","paper","scissor"]
    player=input( "Enter stone scissor paper : ")
    while player not in computer:
        player=input( "Enter stone scissor paper : ")
    player1=random.choice(computer) 
    for x in range(3,0,-1):
        print(x) 
        time.sleep(0.2)
    print("Computer is choosing ",player1)
    print("You have choosen ",player)

    if player1==player:
        print("The Game is Draw")
        print("Good Try")
    elif  player =="stone":
        if player1 =="paper":
            print("You have lost the game!")
        elif player1=="scissor":
            print("You have won the game!")
    elif  player =="paper":
        if player1 =="stone":
            print("You have won the game!")
        elif player1=="scissor":
            print("You have lost the game!")
    elif  player =="scissor":
        if player1 =="paper":
            print("You have won the game!")
        elif player1=="stone":
            print("You have lost the game")

print("----Welcome to our game----")
while True:
    a=input("Do you want to play (y/n) :  ")
    if a=="y" or a=="Y":
        game()
    elif a=="n" or a=="N":
        print("Dhanyavaad")
        exit()
    

        
        

