import random
computer = random.choice([1, 2, 3])
human = input("\nYour Turn: Snake(s) Water(w) or Gun(g)...?\nEnter Your Choice: ")
dic1 = {"s": 1, "w": 2, "g": 3}
you = dic1[human]
reversedict = {1: "Snake", 2: "Water", 3: "Gun"}
print(f"\nComputer Choice {reversedict[computer]} and Your Choice {reversedict[you]}")
if computer == you:
    print("Match Draw!!")
else:
    if computer == 1 and you == 2:
        print("You lose!!")
    elif computer == 2 and you == 3:
        print("You lose!!")
    elif computer == 3 and you == 1:
        print("You lose!!")
    elif computer == 1 and you == 3:
        print("Congratulations!! You Won")
    elif computer == 2 and you == 1:
        print("Congratulations!! You Won")
    elif computer == 3 and you == 2:
        print("Congratulations!! You Won", end="")
    else:
        print("Something wrong. Try again")

    # The below logic is written on the basis of the value of you - computer
    # if you - computer == 1 or you - computer == -2:
    #   print("You lose!!")
    # else:
    #     print("Congratulations!! You Won", end="")
