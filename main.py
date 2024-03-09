import shotgun
import random
import time

def initialise():
    p1name = input("\nEnter your name: ")
    p2name = "The Dealer"
    print("\n" + p1name , "will be playing against", p2name + ".\n")
    gun = shotgun.Shotgun(["L", "B", "B"], 3)
    game(p1name, p2name, gun)


def check_win(p1name, p2name, p1health, p2health):
    if p1health == 0:
        print("-----", p2name, "wins -----\n")
        exit
    elif p2health == 0:
        print("-----", p1name, "wins -----\n")
        exit


def set_health(round):
    if round == 1:
        p1health = 2
        p2health = 2
        return p1health, p2health


def player1Choice(p1name, p2name, p1health, p2health, gun):
    # i think the problem is that p1health is getting reset back to 2 here
    choice = input()
    time.sleep(1.5)
    result = gun.shoot()
    print("")

    if choice == "1" and result == "L": # Shot self with live round
        print("You shot yourself with a live round...\n")
        time.sleep(1.5)
        p1health -= 1
        print("You have lost 1 health, remaining health =", p1health, "\n")
        time.sleep(1.5)
    elif choice == "1" and result == "B": # Shot self with blank round
        print("You shot yourself with a blank round...\n")
        time.sleep(1.5)
    elif choice == "2" and result == "L": # Shot player2 with live round
        print("You shot", p2name, "with a live round...\n")
        time.sleep(1.5)
        p2health -= 1
        print(p2name, "has lost 1 health, remaining health =", p2health, "\n")
        time.sleep(1.5)
    elif choice == "2" and result == "B": # Shot player2 with blank round
        print("You shot", p2name, "with a blank round...\n")
        time.sleep(1.5)
    else:
        print("--Player1 error choice/result--")

    return p1health, p2health


def player2Choice(p1name, p2name, p1health, p2health, gun):
    choice = random.randint(1, 2)
    time.sleep(1.5)
    result = gun.shoot()

    if choice == 1:
        print(p2name, "has chosen to shoot you.\n")
        time.sleep(1.5)
    elif choice == 2:
        print(p2name, "has chosen to shoot themself.\n")
        time.sleep(1.5)
    else:
        print("--Player2 error choice--")

    if choice == 1 and result == "L": # Player2 shot you with live round
        print(p2name, "shot you with a live round...\n")
        time.sleep(1.5)
        p1health -= 1
        print("You have lost 1 health, remaining health =", p1health, "\n")
        time.sleep(1.5)
    elif choice == 1 and result == "B": # Player2 shot you with blank round
        print(p2name, "shot you with a blank round...\n")
        time.sleep(1.5)
    elif choice == 2 and result == "L": # Player2 shot self with live round
        print(p2name, "shot themself with a live round...\n")
        time.sleep(1.5)
        p2health -= 1
        print(p2name, "has lost 1 health, remaining health =", p2health, "\n")
        time.sleep(1.5)
    elif choice == 2 and result == "B": # Player2 shot self with blank round
        print(p2name, "shot themself with a blank round...\n")
        time.sleep(1.5)
    else:
        print("--Player2 error choice/result--")

    return p1health, p2health


def reload_gun(reload):
    if reload == 0:
        return shotgun.Shotgun(["L", "B", "B"], 3)
    elif reload == 1:
        return shotgun.Shotgun(["L", "L", "L", "B", "B"], 5)
    else:
        print("--Reload error--")


def game(p1name, p2name, gun):
    # put this all in a round1 function??
    time.sleep(1.5)
    print("""
    +----------------+
    | ROUND 1 BEGINS |
    +----------------+
    """)
    time.sleep(1.5)
    print("Both player's health will start at 2.")
    print("3 shots are loaded into the shotgun; 1 live, 2 blank. \n")
    time.sleep(1.5)
    turn = "p2" # set to p2 initially because it will get imediently flipped
    reload = 0

    round = 1
    p1health, p2health = set_health(round)

    while(p1health > 0 and p2health > 0):
        turn = "p2" if turn == "p1" else "p1" # Flips turn

        if gun.total_rounds > 0:

            if turn == "p1":
                print("It is your turn.\n")
                time.sleep(1.5)
                print("Shoot yourself [1] or", p2name + "? [2] \n")
                p1health, p2health = player1Choice(p1name, p2name, p1health, p2health, gun)

            if turn == "p2":
                print("It is", p2name + "'s turn.\n")
                time.sleep(1.5)
                print(p2name, "is deciding...\n")
                p1health, p2health = player2Choice(p1name, p2name, p1health, p2health, gun)
        else:
            print("The shotgun has been emptied...\n")
            reload += 1
            gun = reload_gun(reload)
            time.sleep(1.5)
            print("It now contains 5 rounds; 3 live, 2 blank.\n")
            time.sleep(1.5)
            exit
    else:
        check_win(p1name, p2name, p1health, p2health)


def main():
    play = input("\nPlay Buckshot Roulette [YES] [NO] \n")
    play = play.upper()
    if play == "Y" or play == "YES" or play == "YEA":
        initialise()
        exit
    elif play == "N" or play == "NO":
        print("Exit game")
        exit
    else:
        print("Invalid input")
        exit


if __name__ == "__main__":
    main()