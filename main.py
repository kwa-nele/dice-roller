#Loop
# ask: roll the dice?
#if user enters "yes", roll a dice and generate a random number between 1 and 6. If user enters "no", print "Maybe next time!" and exit the program.
#Else
#print "Invalid input,try again"

import random
while True:
    user_choice = input("Roll the dice? (yes/no): ").strip().lower()
    if user_choice == "yes":
        dice_roll1 = random.randint(1, 6)
        dice_roll2 = random.randint(1, 6)
        print(f"You rolled a {dice_roll1} and a {dice_roll2}!")
    elif user_choice == "no":
        print("Maybe next time!")
        break
    else:
        print("Invalid input, try again!")