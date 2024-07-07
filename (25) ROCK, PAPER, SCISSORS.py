import random
import time

while True:
    game = ['rock', 'paper', 'scissors']

    comp = random.choice(game)
    player = None       # we can also say "". It'll be same as None

    while player not in game:
        player = input("So...Rock, Paper or Scissors?: ").lower()

    if player == comp:
        print("Player: ", player)
        print("Computer: ", comp)
        print("Ahh! It's a Tie!")

    elif player == 'rock':
        if comp == 'paper':
            print("Player: ", player)
            print("Computer: ", comp)
            print("You Lose!")
            comp_win = "FUCK U NIGGA"
            for i in comp_win:
                time.sleep(0.3)
                print(i, end="")
        if comp == 'scissors':
            print("Player: ", player)
            print("Computer: ", comp)
            print("You won!")

    elif player == 'paper':
        if comp == 'rock':
            print("Player: ", player)
            print("Computer: ", comp)
            print("You Win!")
        if comp == 'scissors':
            print("Player: ", player)
            print("Computer: ", comp)
            print("You Lose!")
            comp_win = "FUCK U NIGGA"
            for i in comp_win:
                time.sleep(0.3)
                print(i, end="")

    elif player == 'scissors':
        if comp == 'rock':
            print("Player: ", player)
            print("Computer: ", comp)
            print("You Lose!")
            comp_win = "FUCK U NIGGA"
            for i in comp_win:
                time.sleep(0.3)
                print(i, end="")
        if comp == 'paper':
            print("Player: ", player)
            print("Computer: ", comp)
            print("You Win!")

    play_again = input("\nDo you want to play again?(yes/no): ")
    if play_again != 'yes':
        break

print("Byeee!!")

