# Number Guess Game 

import random

winningnum = random.randint(1,10)
print(winningnum)

gameleft = 5

print(f"You have {gameleft} chance to guess the number between 1 to 10")

for curnumber in range(1,gameleft+1):
    try:
        guess = int(input(f"Game {curnumber}: Enter your guess number = "))

        if guess == winningnum:
            print(f"Congratulations correct number {winningnum} in {curnumber} attempts")
            break 
        elif guess < winningnum:
            print("Too low!, Try again")
        else:
            print("Too high!, Try again")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# check if user has used all chances 
    if curnumber == gameleft:
        print(f"Sorry!, you've used all your chances. Winning number is {winningnum}.")

# gmail address