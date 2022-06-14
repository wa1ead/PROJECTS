print ("WELCOME IN THE QUIZ GAME")
ENTER = input("IF YOU WANNA PLAY, TYPE 'YES' ")
if ENTER.upper() == "YES":
    print("OK, LET'S GO!")
else:
    quit()
SCORE = 0

Q1 = input("HOW MANY TIMES 'REAL MADRID' WON THE UEFA.CL ")
if Q1 == "14":
    print("CORRECT!")
    SCORE += 1
else:
    print("FALSE")

Q2 = input("WHO IS THE TOP SCORRER IN THE HISTORY OF UEFA.CL ")
if Q2.upper() == "CRISTIANO RONALDO":
    print("CORRECT!")
    SCORE += 1
else:
    print("FALSE")

Q3 = input("WHO IS THE MOST TITLED PLAYER IN THE HISTORY ")
if Q3.upper() == "DANI ALVES":
    print("CORRECT!")
    SCORE += 1
else:
    print("FALSE")

Q4 = input("WHAT IS THE BEST STADIUM IN THE WORLD ")
if Q4.upper() == "SANTIAGO BERNABEU":
    print("CORRECT!")
    SCORE += 1
else:
    print("FALSE")

Q5 = input("WHICH PLAYER HAS MORE 'BALLON D'OR' IN THE HISTORY ")
if Q5.upper() == "LIONEL MESSI":
     print("CORRECT!")
     SCORE += 1
else:
    print("FALSE")

print ("YOUR SCORE IS " , str(SCORE) + "/5")
print ("ACCURACY " , (SCORE/5) * 100 , "%")