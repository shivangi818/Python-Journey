import random

jackpot=random.randint(1,100)

guess=int(input("guess a number"))
counter=1

while guess!=jackpot:
    #kab tak chalega
    if guess<jackpot:
        print("guess higher ")
        guess=int(input("guess a number again"))
        counter= counter+1
    else:
        print("guess lower")
        guess=int(input("guess a number again"))
        counter+1

else:
    print("conrats")
    print("no of attempts", counter)

