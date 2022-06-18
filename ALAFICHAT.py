import random

user_wins = 0
computer_wins = 0

selections = ["ROCK", "PAPER", "SCISSORS"]

while True:
    user_input = input("TYPE 'ROCK', 'PAPER', 'SCISSORS' OR 'Q' TO QUIT : ").upper()
    if user_input == "Q":
        break

    if user_input not in selections:
        continue
    
    selection_index = random.randint(0, 2)
    computer_selection = selections[selection_index]
    print("COMPUTER SELECT :", computer_selection)

    if user_input == "ROCK" and computer_selection == "SCISSORS":
        print ("YOU WIN!")
        user_wins += 1

    elif user_input == "PAPER" and computer_selection == "ROCK":
        print ("YOU WIN!")
        user_wins += 1

    elif user_input == "SCISSORS" and computer_selection == "PAPER":
        print ("YOU WIN!")
        user_wins += 1
    
    elif user_input == computer_selection:
        print("EQUAL!")

    else:
        print("YOU LOSE!")
        computer_wins += 1

print("YOU WON", user_wins, "TIMES.")
print("THE COMPUTER WON", computer_wins, "TIMES.")
print("GOODBYE!")