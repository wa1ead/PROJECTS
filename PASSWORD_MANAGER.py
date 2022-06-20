master_pwd = input("WHAT IS THE MASTER PASSWORD? : ")

def add():
    name = input("ACCOUNT NAME : ")
    pwd = input("PASSWORD : ")
    with open ('PASSWORDS.txt', 'a') as f:
        f.write = (name + "|" + pwd + "\n")

def view():
    with open('PASSWORDS.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwrd = data.split("|")
            print("USER :", user, "| PASSWORD :", pwrd)

while True:
    mode = input("WOULD YOU LIKE TO ADD NEW PASSWORD OR VIEW EXISTING ONES ('ADD'/'VIEW')? OR PRESS 'Q' TO QUIT : ").upper()
    if mode == "ADD":
        add()
    elif mode == "VIEW":
        view()
    elif mode == "Q":
        break
    else:
        print("INVALID MODE.")
        continue