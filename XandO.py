import sys
val1, status1 = "1", "empty"
val2, status2 = "2", "empty"
val3, status3 = "3", "empty"
val4, status4 = "4", "empty"
val5, status5 = "5", "empty"
val6, status6 = "6", "empty"
val7, status7 = "7", "empty"
val8, status8 = "8", "empty"
val9, status9 = "9", "empty"
playerstatus = "player1"
winning_state = False

while True:
    welcome_screen = int(input("""Welcome to the Tic Tac Toe Game
    What do you want to do?
    [1] - Play Game
    [2] - Exit"""))

    if welcome_screen == 1:
        print("You have selected to play")
        break
    else:
        continue


def checkboard():
    print(f"{val1} | {val2} | {val3}")
    print("----------")
    print(f"{val4} | {val5} | {val6}")
    print("----------")
    print(f"{val7} | {val8} | {val9}")
    print("----------")


def winlogic():
    #Val1
    if val1 == "o" and (val2 == "o" or val4 == "o" or val5 == "o") and (val3 == "o" or val7 == "o" or val9 == "o"):
        print("Player 2 wins")
        sys.exit()
    elif val1 == "x" and (val2 == "x" or val4 == "x" or val5 == "x") and (val3 == "x" or val7 == "x" or val9 == "x"):
        print("Player 1 wins")
        sys.exit()

    #Val2
    if val2 == "o" and val5 == "o" and val8 == "o":
        print("Player 2 wins")
        sys.exit()
    elif val2 == "x" and val5 == "x" and val8 == "x":
        print("Player 1 wins")
        sys.exit()

    #Val3
    if val3 == "o" and (val5 == "o" or val6 == "o") and (val7 == "o" or val9 == "o"):
        print("Player 2 wins")
        sys.exit()
    elif val3 == "x" and (val5 == "x" or val6 == "x") and (val7 == "x" or val9 == "x"):
        print("Player 2 wins")
        sys.exit()


    #Val4
    if val4 == "o" and val5 == "o" and val6 == "o":
        print("Player 2 wins")
        sys.exit()
    elif val4 == "x" and val5 == "x" and val6 == "x":
        print("Player 1 wins")
        sys.exit()

    #Val7
    if val7 == "o" and val8 == "o" and val9 == "o":
        print("Player 2 wins")
        sys.exit()

    elif val7 == "x" and val8 == "x" and val9 == "x":
        print("Player 1 wins")
        sys.exit()


while val1 == "1" or val2 == "2" or val3 == "3" or val4 == "4" or val5 == "5" or val6 == "6" or val7 == "7" or val8 == "8" or val9 == "9":
    checkboard()
    winlogic()
    if playerstatus == "player1":
        player1 = int(input("Where do you want to place your X"))
        if player1 == 1:
            val1, status1, playerstatus = "x", "taken", "player2"
            if status1 == "taken":
                print(f"Already Taken with {val1}")
                continue
        elif player1 == 2:
            val2, status2, playerstatus = "x", "taken", "player2"
            if status2 == "taken":
                print(f"Already Taken with {val2}")
                continue
        elif player1 == 3:
            val3, status3, playerstatus = "x", "taken", "player2"
            if status3 == "taken":
                print(f"Already Taken with {val3}")
                continue
        elif player1 == 4:
            val4, status4, playerstatus = "x", "taken", "player2"
            if status4 == "taken":
                print(f"Already Taken with {val4}")
                continue
        elif player1 == 5:
            val5, status5, playerstatus = "x", "taken", "player2"
            if status5 == "taken":
                print(f"Already Taken with {val5}")
                continue
        elif player1 == 6:
            val6, status6, playerstatus = "x", "taken", "player2"
            if status6 == "taken":
                print(f"Already Taken with {val6}")
                continue
        elif player1 == 7:
            val7, status7, playerstatus = "x", "taken", "player2"
            if status7 == "taken":
                print(f"Already Taken with {val7}")
                continue
        elif player1 == 8:
            val8, status8, playerstatus = "x", "taken", "player2"
            if status8 == "taken":
                print(f"Already Taken with {val8}")
                continue
        elif player1 == 9:
            val9, status9, playerstatus = "x", "taken", "player2"
            if status9 == "taken":
                print(f"Already Taken with {val9}")
                continue

    if playerstatus == "player2":
        player2 = int(input("Where do you want to place your O"))
        if player2 == 1:
            val1, status1, playerstatus = "o", "taken", "player1"
            if status1 == "taken":
                print(f"Already Taken with {val1}")
                continue
        elif player2 == 2:
            val2, status2, playerstatus = "o", "taken", "player1"
            if status2 == "taken":
                print(f"Already Taken with {val2}")
                continue
        elif player2 == 3:
            val3, status3, playerstatus = "o", "taken", "player1"
            if status3 == "taken":
                print(f"Already Taken with {val3}")
                continue
        elif player2 == 4:
            val4, status4, playerstatus = "o", "taken", "player1"
            if status4 == "taken":
                print(f"Already Taken with {val4}")
                continue
        elif player2 == 5:
            val5, status5, playerstatus = "o", "taken", "player1"
            if status5 == "taken":
                print(f"Already Taken with {val5}")
                continue
        elif player2 == 6:
            val6, status6, playerstatus = "o", "taken", "player1"
            if status6 == "taken":
                print(f"Already Taken with {val6}")
                continue
        elif player2 == 7:
            val7, status7, playerstatus = "o", "taken", "player1"
            if status7 == "taken":
                print(f"Already Taken with {val7}")
                continue
        elif player2 == 8:
            val8, status8, playerstatus = "o", "taken", "player1"
            if status8 == "taken":
                print(f"Already Taken with {val8}")
                continue
        elif player2 == 9:
            val9, status9, playerstatus = "o", "taken", "player1"
            if status9 == "taken":
                print(f"Already Taken with {val9}")
                continue