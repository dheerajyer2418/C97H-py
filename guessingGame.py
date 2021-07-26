import random

randomNumber = random.randint(1,9)
chances = 0
print("Guess a Number between 1-9")
while chances < 5:
    num = int(input("Enter the number guess: "))
    if num == randomNumber: 
        print("Congrats, You guessed right!!")
    elif num < randomNumber: 
        print("Sorry, Number too less!!")
    else:
        print("Sorry that number was too high!!")
chances += 1
if not chances < 5:
    print("You Lost the game, the actual is: " + randomNumber)
    