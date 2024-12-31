import random

def game():
    dice_computer = ['1', '2', '3', '4', '5', '6']
    count = 0

    while True:
        computer = int(random.choice(dice_computer))
        player = int(input("----Enter a number between 1 to 6: "))
        print("Number chosen by player:", player)
        print("Number chosen by computer:", computer)

        if player == computer:
            print("---Hurray! You guessed it correctly---")
            print("---You won the game!---")
            break
        else:
            print("---Guess again, please---")
            count += 1

    print("Number of chances taken to guess:", count)
    return count

print("----Welcome to our game of guessing the number----")

while True:
    play_again = input("Do you want to play? (y/n):\n ")
    
    if play_again.lower() == 'y':
        count = game()
        if count < 3:
            print("----Very Well Played----")
            print("----You are an expert----")
        else:
            print("----Good Game Play----")
    elif play_again.lower() == 'n':
        print("Dhanyavaad")
        break
