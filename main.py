blank_list = ["  "] * 9


def blanks():
    print(f"{blank_list[0]}|{blank_list[1]}|{blank_list[2]}")
    print(f"{blank_list[3]}|{blank_list[4]}|{blank_list[5]}")
    print(f"{blank_list[6]}|{blank_list[7]}|{blank_list[8]}")


blanks()


def placement(x):
    if blank_list[x] != "  ":
        print("That place is occupied.Please make another choice.")
        x = int(input("Where do you wanna put? :"))
        placement(x)


def check(y):
    if blank_list[0] != "  " and blank_list[1] != "  " and blank_list[2] != "  " and blank_list[0] == blank_list[1] == \
            blank_list[2]:
        return f"{y} wins"
    elif blank_list[3] != "  " and blank_list[4] != "  " and blank_list[5] != "  " and blank_list[3] == blank_list[4] == \
            blank_list[5]:
        return f"{y} wins"
    elif blank_list[6] != "  " and blank_list[7] != "  " and blank_list[8] != "  " and blank_list[6] == blank_list[7] == \
            blank_list[8]:
        return f"{y} wins"
    elif blank_list[0] != "  " and blank_list[3] != "  " and blank_list[6] != "  " and blank_list[0] == blank_list[3] == \
            blank_list[6]:
        return f"{y} wins"
    elif blank_list[1] != "  " and blank_list[4] != "  " and blank_list[7] != "  " and blank_list[1] == blank_list[4] == \
            blank_list[7]:
        return f"{y} wins"
    elif blank_list[2] != "  " and blank_list[5] != "  " and blank_list[8] != "  " and blank_list[2] == blank_list[5] ==  \
            blank_list[8]:
        return f"{y} wins"
    elif blank_list[0] != "  " and blank_list[4] != "  " and blank_list[8] != "  " and blank_list[0] == blank_list[4] == \
            blank_list[8]:
        return f"{y} wins"
    elif blank_list[2] != "  " and blank_list[4] != "  " and blank_list[6] != "  " and blank_list[2] == blank_list[4] == \
            blank_list[6]:
        return f"{y} wins"


game_is_on = True
name1 = input("Player1 -name :")
name2 = input("Player2 -name :")
print(" 1| 2| 3")
print(" 4| 5| 6")
print(" 7| 8| 9")
while game_is_on:
    PLAYER1 = int(input(f"{name1} -Where do you wanna put? :"))
    placement(PLAYER1 - 1)
    blank_list[PLAYER1 - 1] = " X"
    blanks()
    x = check(name1)
    if x:
        print(x)
        break
    else: print("It's a tie. If you wanna continue play, type yes if not no")
    PLAYER2 = int(input(f"{name2} -Where do you wanna put? :"))
    placement(PLAYER2-1)
    blank_list[PLAYER2 - 1] = " O"
    blanks()
    z = check(name2)
    if z:
        print(z)
        break