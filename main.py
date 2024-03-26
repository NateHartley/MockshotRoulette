import shotgun
import player
import random
import time
import test

def initialise():
    gun = shotgun.Shotgun(["L", "B", "B"], 3)
    player_1 = player.Player()
    player_2 = player.Player()
    slow_print('\n"Please sign the waiver."\n')
    test.print_markdown_text()
    player_1.name = input("\nEnter name: ")
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
        print(u"You shot yourself with a\u001b[31m\u001b[1m live round...\u001b[0m\n")
        pause()
        player_1.health -= 1
        print("You have lost 1 health,", player_1.health, "health remaining.\n")
        pause()
    elif choice == "1" and result == "B": # Shot self with blank round
        print("You shot yourself with a blank...\n")
        pause()
    elif choice == "2" and result == "L": # Shot player2 with live round
        print("You shot", player_2.name, u"with a\u001b[31m\u001b[1m live round...\u001b[0m\n")
        pause()
        player_2.health -= 1
        print(player_2.name, "has lost 1 health,", player_2.health, "health remaining.\n")
        pause()
    elif choice == "2" and result == "B": # Shot player2 with blank round
        print("You shot", player_2.name, "with a blank...\n")
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
        print(player_2.name, u"shot you with a\u001b[31m\u001b[1m live round...\u001b[0m\n")
        pause()
        player_1.health -= 1
        print("You have lost 1 health,", player_1.health, "health remaining.\n")
        pause()
    elif choice == 1 and result == "B": # Player2 shot you with blank round
        print(player_2.name, "shot you with a blank...\n")
        pause()
    elif choice == 2 and result == "L": # Player2 shot self with live round
        print(player_2.name, u"shot themself with a\u001b[31m\u001b[1m live round...\u001b[0m\n")
        pause()
        player_2.health -= 1
        print(player_2.name, "has lost 1 health,", player_2.health, "health remaining.\n")
        pause()
    elif choice == 2 and result == "B": # Player2 shot self with blank round
        print(player_2.name, "shot themself with a blank...\n")
        pause()
    else:
        print("--Player2 error choice/result--")
        quit()

    return player_1.health, player_2.health


def round_1():
    pause()
    print(u"""\u001b[33m
    +----------------+
    | ROUND 1 BEGINS |
    +----------------+
    \u001b[0m""")
    pause()
    print("Both player's health will start at 2.\n")
    print("3 shots are loaded into the shotgun; 1 live, 2 blank. \n")
    pause()


def round_2():
    pause()
    print(u"""\u001b[33m
    +----------------+
    | ROUND 2 BEGINS |
    +----------------+
    \u001b[0m""")
    pause()
    print("Both player's health will start at 4.\n")
    print("The shotgun has been emptied...\n")
    print("2 shots are loaded into the shotgun; 1 live, 1 blank. \n")
    pause()


def round_3():
    pause()
    print(u"""\u001b[33m
    +----------------+
    | ROUND 3 BEGINS |
    +----------------+
    \u001b[0m""")
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
        gun.reload_gun(reload)
    elif round == 2:
        round_2()
        player_1.set_health(round)
        player_2.set_health(round)
        reload = 2
        gun.reload_gun(reload)
    elif round == 3:
        round_3()
        player_1.set_health(round)
        player_2.set_health(round)
        reload = 7
        gun.reload_gun(reload)
    else:
        print("--Round error--")
        quit()

    while(player_1.health > 0 and player_2.health > 0):

        if gun.total_rounds > 0:
            turn = "p2" if turn == "p1" else "p1" # Flips turn

            if turn == "p1":
                print("It is your turn.\n")
                pause()
                print(u"Shoot\u001b[31m\u001b[1m yourself [1]\u001b[0m or \u001b[31m\u001b[1m" + player_2.name, "[2]\u001b[0m ?\n")
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
            gun.reload_gun(reload)
            pause()
    else:
        check_win(player_1, player_2, round)
        round += 1
        game(gun, player_1, player_2, round)


def pause():
    # Enable/disable pauses inbetween prints for faster testing
    pause = False
    if pause:
        return time.sleep(1.5)


def slow_print(msg):
    for i in msg:
        print(i, end="", flush=True)
        time.sleep(0.05)


def main():
    #test.coloured_text()
    initialise()


if __name__ == "__main__":
    main()