import shotgun
import player
import random
import time
from colorama import Fore, Back, Style

def initialise():
    gun = shotgun.Shotgun(["L", "B", "B"], 3)
    player_1 = player.Player()
    player_2 = player.Player()
    player_1.name = input("\nEnter your name: ")
    player_2.name = "The Dealer"
    print("\n" + player_1.name , "will be playing against", player_2.name + ".\n")
    round = 1
    game(gun, player_1, player_2, round)


def check_win(player_1: player.Player, player_2: player.Player, round):
    if player_1.health == 0:
        print("-----", player_2.name, "wins round", round, "-----\n")
        if round == 3:
            quit()
    elif player_2.health == 0:
        print("-----", player_1.name, "wins round", round, "-----\n")
        if round == 3:
            quit()


def player1Choice(player_1: player.Player, player_2: player.Player, gun: shotgun.Shotgun):
    choice = input()
    pause()
    result = gun.shoot()
    print("")

    if choice == "1" and result == "L": # Shot self with live round
        print("You shot yourself with a live round...\n")
        pause()
        player_1.health -= 1
        print("You have lost 1 health, remaining health =", player_1.health, "\n")
        pause()
    elif choice == "1" and result == "B": # Shot self with blank round
        print("You shot yourself with a blank round...\n")
        pause()
    elif choice == "2" and result == "L": # Shot player2 with live round
        print("You shot", player_2.name, "with a live round...\n")
        pause()
        player_2.health -= 1
        print(player_2.name, "has lost 1 health, remaining health =", player_2.health, "\n")
        pause()
    elif choice == "2" and result == "B": # Shot player2 with blank round
        print("You shot", player_2.name, "with a blank round...\n")
        pause()
    else:
        print("--Player1 error choice/result--")
        quit()

    return player_1.health, player_2.health


def player2Choice(player_1: player.Player, player_2: player.Player, gun: shotgun.Shotgun):
    choice = random.randint(1, 2)
    pause()
    result = gun.shoot()

    if choice == 1:
        print(player_2.name, "has chosen to shoot you.\n")
        pause()
    elif choice == 2:
        print(player_2.name, "has chosen to shoot themself.\n")
        pause()
    else:
        print("--Player2 error choice--")

    if choice == 1 and result == "L": # Player2 shot you with live round
        print(player_2.name, "shot you with a live round...\n")
        pause()
        player_1.health -= 1
        print("You have lost 1 health, remaining health =", player_1.health, "\n")
        pause()
    elif choice == 1 and result == "B": # Player2 shot you with blank round
        print(player_2.name, "shot you with a blank round...\n")
        pause()
    elif choice == 2 and result == "L": # Player2 shot self with live round
        print(player_2.name, "shot themself with a live round...\n")
        pause()
        player_2.health -= 1
        print(player_2.name, "has lost 1 health, remaining health =", player_2.health, "\n")
        pause()
    elif choice == 2 and result == "B": # Player2 shot self with blank round
        print(player_2.name, "shot themself with a blank round...\n")
        pause()
    else:
        print("--Player2 error choice/result--")
        quit()

    return player_1.health, player_2.health


def reload_gun(reload):
    if reload == 0: # Start of round 1
        return shotgun.Shotgun(["L", "B", "B"], 3)
    elif reload == 1:
        print("It now contains 5 rounds; 3 live, 2 blank.\n")
        return shotgun.Shotgun(["L", "L", "L", "B", "B"], 5)
    elif reload == 2: # Start of round 2
        return shotgun.Shotgun(["L", "B"], 2)
    elif reload == 3:
        print("It now contains 4 rounds; 2 live, 2 blank.\n")
        return shotgun.Shotgun(["L", "L", "B", "B"], 4)
    elif reload == 4:
        print("It now contains 5 rounds; 3 live, 2 blank.\n")
        return shotgun.Shotgun(["L", "L", "L", "B", "B"], 5)
    elif reload == 5: # Made up (DOUBLE CHECK ON VIDEOS)
        print("It now contains 4 rounds; 2 live, 2 blank.\n")
        return shotgun.Shotgun(["L", "L", "B", "B"], 5)
    elif reload == 6: # Start of round 3
        return shotgun.Shotgun(["L", "B", "B"], 3)
    elif reload == 7:
        print("It now contains 8 rounds; 4 live, 4 blank.\n")
        return shotgun.Shotgun(["L", "L", "L", "L", "B", "B", "B", "B"], 8)
    elif reload == 8:
        print("It now contains 5 rounds; 3 live, 2 blank.\n")
        return shotgun.Shotgun(["L", "L", "L", "B", "B"], 5)
    elif reload == 9: # Made up (DOUBLE CHECK ON VIDEOS)
        print("It now contains 6 rounds; 4 live, 2 blank.\n")
        return shotgun.Shotgun(["L", "L", "L", "L", "B", "B"], 6)
    else:
        print("--Reload error--")
        quit()

    # put this in shotgun class as well


def round_1():
    pause()
    print("""
    +----------------+
    | ROUND 1 BEGINS |
    +----------------+
    """)
    pause()
    print("Both player's health will start at 2.")
    print("3 shots are loaded into the shotgun; 1 live, 2 blank. \n")
    pause()


def round_2():
    pause()
    print("""
    +----------------+
    | ROUND 2 BEGINS |
    +----------------+
    """)
    pause()
    print("Both player's health will start at 4.\n")
    print("The shotgun has been emptied...\n")
    print("2 shots are loaded into the shotgun; 1 live, 1 blank. \n")
    pause()


def round_3():
    pause()
    print("""
    +----------------+
    | ROUND 3 BEGINS |
    +----------------+
    """)
    pause()
    print("Both player's health will start at 6.\n")
    print("The shotgun has been emptied...\n")
    print("3 shots are loaded into the shotgun; 1 live, 2 blank. \n")
    pause()


def game(gun: shotgun.Shotgun, player_1: player.Player, player_2: player.Player, round):
    turn = "p2" # set to p2 initially because it will get imediently flipped

    if round == 1:
        round_1()
        player_1.set_health(round)
        player_2.set_health(round)
        reload = 0
        gun = reload_gun(reload)
    elif round == 2:
        round_2()
        player_1.set_health(round)
        player_2.set_health(round)
        reload = 2
        gun = reload_gun(reload)
    elif round == 3:
        round_3()
        player_1.set_health(round)
        player_2.set_health(round)
        reload = 6
        gun = reload_gun(reload)
    else:
        print("--Round error--")
        quit()

    while(player_1.health > 0 and player_2.health > 0):

        if gun.total_rounds > 0:
            turn = "p2" if turn == "p1" else "p1" # Flips turn

            if turn == "p1":
                print("It is your turn.\n")
                pause()
                print("Shoot yourself [1] or", player_2.name + "? [2] \n")
                player_1.health, player_2.health = player1Choice(player_1, player_2, gun)

            if turn == "p2":
                print("It is", player_2.name + "'s turn.\n")
                pause()
                print(player_2.name, "is deciding...\n")
                player_1.health, player_2.health = player2Choice(player_1, player_2, gun)
        else:
            print("The shotgun has been emptied...\n")
            if (player_1.health > 0 and player_2.health > 0): # Ensures reload doesn't + 2 when both health and rounds = 0
                reload += 1
            pause()
            gun = reload_gun(reload)
            pause()
    else:
        check_win(player_1, player_2, round)
        round += 1
        game(gun, player_1, player_2, round)


def pause():
    # Enable/disable pauses inbetween prints for faster testing
    pause = True
    if pause:
        return time.sleep(1.5)


def main():
    print(Style.RESET_ALL)
    play = input("\nPlay Buckshot Roulette [YES] [NO] \n")
    play = play.upper()
    if play == "Y" or play == "YES" or play == "YEA":
        initialise()
        quit()
    elif play == "N" or play == "NO":
        print("Exit game")
        quit()
    else:
        print("Invalid input")
        quit()


if __name__ == "__main__":
    main()