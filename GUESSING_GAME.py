import random

top_of_range = input("TYPE A NUMBER : ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("PLEASE ENTER A NUMBER LARGER THAN '0'.")
        quit()
else:
    print("PLEASE ENTER A NUMBER.")
    quit()

random_number = random.randint(0, top_of_range)
print(random_number)

guesses = 0
while True:
    guesses += 1
    user_guess = input("GUESS THE NUMBER? ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("PLEASE ENTER A NUMBER.")
        continue

    if user_guess == random_number:
        print("YOU GOT IT!")
        break
    elif user_guess > random_number:
        print("YOU WERE ABOVE THE NUMBER")
    else:
        print("YOU WERE BELOW THE NUMBER")

print("YOU GOT IT IN", guesses, "GUESSES!")