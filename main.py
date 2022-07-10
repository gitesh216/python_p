import random


def who_win(comp, you):
    if comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "s":
            return True
        elif you == "g":
            return False
    if comp == "g":
        if you == "w":
            return True
        elif you == "s":
            return False


def start_game():
    i = 1
    c_score = 0
    p_score = 0
    while i <= 5:
        print(f"Turn {i}: \r")
        comp = ""
        temp = random.randint(1, 3)
        if temp == 1:
            comp = "s"
        elif temp == 2:
            comp = "w"
        elif temp == 3:
            comp = "g"
        print("Computer had played:)")
        print("Your turn: Snake(s), Water(w), Gun(g)\r")
        you = input()
        if comp != you:
            turn_winner = who_win(comp, you)
            if turn_winner:
                p_score = p_score + 1
            else:
                c_score = c_score + 1
        print(f"Computer chose {comp}: {c_score}")
        print(f"You chose {you}: {p_score}")
        i = i + 1
    final_scores = (c_score, p_score)
    return final_scores


print("****Welcome to my First Python console Snake, Water, Gun Game****")
print('''Instructions:
1. You will get 5 chances.
2. You will play against the computer.
3. Winner will be decided based on the final score.''')
print("Please enter T to start the game..\r")
start = input()
if start == "T" or start == "t":
    print("Started")
else:
    print("Program Exited: Please restart")
    exit()

f_score = ()
f_score = start_game()
if f_score[1] > f_score[0]:
    print("You won!!!")
elif f_score[0] > f_score[1]:
    print("You lose!")
else:
    print("Draw!!")
