name = (input("TYPE YOUR NAME : "))
print("WELCOME", name, "TO THE ADVENTURE GAME")
answer = input("YOU ARE ON A DIRT ROAD, IT HAS COME TO AN END AND YOU CAN GO LEFT OR RIGHT. WHICH WAY WOULD YOU LIKE TO GO? ('RIGHT'/'LEFT') : ").upper()

if answer == "RIGHT":
    answer = input("YOU COME TO A BRIDGE, IT LOOKS WOBBLY. DO YOU WANT TO CROSS IT OR HEAD BACK? ('CROSS'/'BACK') : ").upper()
    if answer == "CROSS":
        answer = input(("YOU CROSS THE BRIDGE AND MEET A STRANGER. DO YOU TALK TO THEM? ('YES'/'NO') : ")).upper()
        if answer == "YES":
            print("YOU TALK TO THE STRANGER, AND THEY GIVE YOU GOLD. YOU WIN!")
        elif answer == "NO":
            print("YOU IGNORE THE STRANGER, AND THEY ARE OFFENDED. YOU LOSE.")
        else:
            print("NOT A VALID OPTION, YOU LOSE.")

    elif answer == "BACK":
            print("YOU GO BACK AND LOSE!")
    
    else:
            print("NOT A VALID OPTION, YOU LOSE.")

elif answer == "LEFT":
    answer = input("YOU COME TO A RIVER. DO YOU WANT TO WALK AROUND IT OR SWIM ACROSS? ('WALK'/'SWIM') : ").upper()
    if answer == "WALK":
        print("YOU WALKED FOR MANY MILES, RAN OUT OF WATER. YOU LOSE.")
    elif answer == "SWIM":
        print("YOU SWIM ACROSS, AND WERE EATEN BY AN ALLIGATOR.")
    else:
        print("NOT A VALID OPTION, YOU LOSE.")

else:
    print("NOT A VALID OPTION, YOU LOSE.")