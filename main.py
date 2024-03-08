import shotgun
import random

def start():
    play = input("Play Buckshot Roulette [YES] [NO] \n")
    play = play.upper()
    if play == "Y" or play == "YES" or play == "YEA":
        initialise()
        exit
    elif play == "N" or play == "NO":
        print("End game")
        exit
    else:
        print("Invalid input")
        exit


def initialise():
    p1name = input("Enter your name: ")
    p2name = "The Dealer"
    p1health = 2
    p2health = 2
    game(p1name, p2name, p1health, p2health)


def check_win(p1name, p2name, p1health, p2health):
    if p1health == 0:
        print("-----", p2name, "wins -----")
        exit
    elif p2health == 0:
        print("-----", p1name, "wins -----")


def player1Choice(p1name, p2name, p1health, p2health, gun):
    choice = input()
    result = round1(gun)

    if choice == "1" and result == "l": # Shot self with live round
        print("You shot yourself with a live round...\n")
        p1health -= 1
        print("You have lost 1 health, remaining health =", p1health, "\n")
    elif choice == "1" and result == "b": # Shot self with blank round
        print("You shot yourself with a blank round...\n")
    elif choice == "2" and result == "l": # Shot player2 with live round
        print("You shot", p2name, "with a live round...\n")
        p2health -= 1
        print(p2name, "has lost 1 health, remaining health =", p2health, "\n")
    elif choice == "2" and result == "b": # Shot player2 with blank round
        print("You shot", p2name, "with a blank round...\n")
    
    print("It is now", p2name + "'s turn\n")#------------------------------------------------------------------------1

    check_win(p1name, p2name, p1health, p2health)


def player2Choice(p1name, p2name, p1health, p2health, gun):
    choice = random.randint(1, 2)
    result = round1(gun)

    if choice == 1:
        print(p2name, "has chosen to shoot you.")
    elif choice == 2:
        print(p2name, "has chosen to shoot themself.")
    else:
        print("--Player2 error choice--")

    if choice == 1 and result == "l": # Player2 shot you with live round
        print(p2name, "shot you with a live round...\n")
        p1health -= 1
        print("You have lost 1 health, remaining health =", p1health, "\n")
    elif choice == 1 and result == "b": # Player2 shot you with blank round
        print(p2name, "shot you with a blank round...\n")
    elif choice == 2 and result == "l": # Player2 shot self with live round
        print(p2name, "shot themself with a live round...\n")
        p2health -= 1
        print(p2name, "has lost 1 health, remaining health =", p2health, "\n")
    elif choice == 2 and result == "b": # Player2 shot self with blank round
        print(p2name, "shot themself with a blank round...\n")
    else:
        print("--Player2 error choice/result--")
    
    print("It is now your turn\n")

    check_win(p1name, p2name, p1health, p2health)


def round1(gun):
    return gun.shoot()


def game(p1name, p2name, p1health, p2health):
    gun = shotgun.Shotgun(["l", "b", "b"], 3)

    print(p1name , "will be playing against", p2name + ".\n")
    print("Round 1 begins...\n")
    print("Both player's health will start at 2.")
    print("3 shots are loaded into the shotgun.")
    print("1 live, and 2 blanks.\n")
    print(p1name, "goes first...\n")
    turn = "p2" # set to p2 initially because it will get imediently flipped

    while(p1health > 0 and p2health > 0):
        turn = "p2" if turn == "p1" else "p1" # Flips turn

        if gun.total_rounds > 0:

            if turn == "p1":
                print("Shoot yourself [1] or", p2name + "? [2]")
                player1Choice(p1name, p2name, p1health, p2health, gun)

            if turn == "p2":
                player2Choice(p1name, p2name, p1health, p2health, gun)
        else:
            print("No bullets right now, IMPLEMENT RELOAD FUNCTION LATER")
            exit
    else:
        check_win(p1name, p2name, p1health, p2health)


def main():
    start()


if __name__ == "__main__":
    main()