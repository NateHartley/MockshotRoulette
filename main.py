import shotgun
import player
import random
import time

def initialise():
    gun = shotgun.Shotgun(["L", "B", "B"], 3)
    player_1 = player.Player()
    player_2 = player.Player()
    player_1.name = input("\nEnter your name: ")
    player_2.name = "The Dealer"
    print("\n" + player_1.name , "will be playing against", player_2.name + ".\n")

    game(gun, player_1, player_2)


def check_win(player_1: player.Player, player_2: player.Player):
    if player_1.health == 0:
        print("-----", player_1.name, "wins -----\n")
        exit
    elif player_2.health == 0:
        print("-----", player_2.name, "wins -----\n")
        exit


def player1Choice(player_1: player.Player, player_2: player.Player, gun: shotgun.Shotgun):
    choice = input()
    time.sleep(1.5)
    result = gun.shoot()
    print("")

    if choice == "1" and result == "L": # Shot self with live round
        print("You shot yourself with a live round...\n")
        time.sleep(1.5)
        player_1.health -= 1
        print("You have lost 1 health, remaining health =", player_1.health, "\n")
        time.sleep(1.5)
    elif choice == "1" and result == "B": # Shot self with blank round
        print("You shot yourself with a blank round...\n")
        time.sleep(1.5)
    elif choice == "2" and result == "L": # Shot player2 with live round
        print("You shot", player_2.name, "with a live round...\n")
        time.sleep(1.5)
        player_2.health -= 1
        print(player_2.name, "has lost 1 health, remaining health =", player_2.health, "\n")
        time.sleep(1.5)
    elif choice == "2" and result == "B": # Shot player2 with blank round
        print("You shot", player_2.name, "with a blank round...\n")
        time.sleep(1.5)
    else:
        print("--Player1 error choice/result--")

    return player_1.health, player_2.health


def player2Choice(player_1: player.Player, player_2: player.Player, gun: shotgun.Shotgun):
    choice = random.randint(1, 2)
    time.sleep(1.5)
    result = gun.shoot()

    if choice == 1:
        print(player_2.name, "has chosen to shoot you.\n")
        time.sleep(1.5)
    elif choice == 2:
        print(player_2.name, "has chosen to shoot themself.\n")
        time.sleep(1.5)
    else:
        print("--Player2 error choice--")

    if choice == 1 and result == "L": # Player2 shot you with live round
        print(player_2.name, "shot you with a live round...\n")
        time.sleep(1.5)
        player_1.health -= 1
        print("You have lost 1 health, remaining health =", player_1.health, "\n")
        time.sleep(1.5)
    elif choice == 1 and result == "B": # Player2 shot you with blank round
        print(player_2.name, "shot you with a blank round...\n")
        time.sleep(1.5)
    elif choice == 2 and result == "L": # Player2 shot self with live round
        print(player_2.name, "shot themself with a live round...\n")
        time.sleep(1.5)
        player_2.health -= 1
        print(player_2.name, "has lost 1 health, remaining health =", player_2.health, "\n")
        time.sleep(1.5)
    elif choice == 2 and result == "B": # Player2 shot self with blank round
        print(player_2.name, "shot themself with a blank round...\n")
        time.sleep(1.5)
    else:
        print("--Player2 error choice/result--")

    return player_1.health, player_2.health


def reload_gun(reload):
    if reload == 0:
        return shotgun.Shotgun(["L", "B", "B"], 3)
    elif reload == 1:
        return shotgun.Shotgun(["L", "L", "L", "B", "B"], 5)
    else:
        print("--Reload error--")

    # put this in shotgun class as well


def round_1():
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

    round = 1
    return round


def round_2():
    time.sleep(1.5)
    print("""
    +----------------+
    | ROUND 2 BEGINS |
    +----------------+
    """)
    time.sleep(1.5)
    print("Both player's health will start at 4.\n")
    print("The shotgun has been emptied...\n")
    print("2 shots are loaded into the shotgun; 1 live, 1 blank. \n")
    time.sleep(1.5)


def game(gun: shotgun.Shotgun, player_1: player.Player, player_2: player.Player):
    turn = "p2" # set to p2 initially because it will get imediently flipped
    reload = 0
    round = round_1()
    player_1.set_health(round) # works! both set to 2 for round 1
    player_2.set_health(round)

    while(player_1.health > 0 and player_2.health > 0):
        turn = "p2" if turn == "p1" else "p1" # Flips turn

        if gun.total_rounds > 0:

            if turn == "p1":
                print("It is your turn.\n")
                time.sleep(1.5)
                print("Shoot yourself [1] or", player_2.name + "? [2] \n")
                player_1.health, player_2.health = player1Choice(player_1, player_2, gun)

            if turn == "p2":
                print("It is", player_2.name + "'s turn.\n")
                time.sleep(1.5)
                print(player_2.name, "is deciding...\n")
                player_1.health, player_2.health = player2Choice(player_1, player_2, gun)
        else:
            print("The shotgun has been emptied...\n")
            reload += 1
            gun = reload_gun(reload)
            time.sleep(1.5)
            print("It now contains 5 rounds; 3 live, 2 blank.\n")
            time.sleep(1.5)
            exit
    else:
        check_win(player_1, player_2)


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