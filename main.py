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


def player1Choice(player_1: player.Player, player_2: player.Player, result, double_damage, eject):
    if not eject:
        choice = input()
        pause()
        print("")

        if choice == "1" and result == "L": # Shot self with live round
            print(u"You shot yourself with a\u001b[31m\u001b[1m live round...\u001b[0m\n")
            pause()
            if double_damage == True:
                player_1.health -= 2
                print("You have lost 2 health,", player_1.health, "health remaining.\n")
            else:
                player_1.health -= 1
                print("You have lost 1 health,", player_1.health, "health remaining.\n")
            pause()

        elif choice == "1" and result == "B": # Shot self with blank round
            print("You shot yourself with a blank...\n")
            pause()

        elif choice == "2" and result == "L": # Shot player2 with live round
            print("You shot", player_2.name, u"with a\u001b[31m\u001b[1m live round...\u001b[0m\n")
            pause()
            if double_damage == True:
                player_2.health -= 2
                print(player_2.name, "has lost 2 health,", player_2.health, "health remaining.\n")
            else:
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


def player2Choice(player_1: player.Player, player_2: player.Player, result, dub_dam, eject):
    if not eject:
        choice = random.randint(1, 2)
        pause()

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
            if dub_dam == True:
                player_1.health -= 2
                print("You have lost 2 health,", player_1.health, "health remaining.\n")
            else:
                player_1.health -= 1
                print("You have lost 1 health,", player_1.health, "health remaining.\n")
            pause()

        elif choice == 1 and result == "B": # Player2 shot you with blank round
            print(player_2.name, "shot you with a blank...\n")
            pause()

        elif choice == 2 and result == "L": # Player2 shot self with live round
            print(player_2.name, u"shot themself with a\u001b[31m\u001b[1m live round...\u001b[0m\n")
            pause()
            if dub_dam == True:
                player_2.health -= 2
                print(player_2.name, "has lost 2 health,", player_2.health, "health remaining.\n")
            else:
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


def round_2(player_1: player.Player, player_2: player.Player):
    pause()
    print(u"""\u001b[33m
    +----------------+
    | ROUND 2 BEGINS |
    +----------------+
    \u001b[0m""")
    pause()
    print("LET'S MAKE THIS  A LITTLE MORE INTERESTING ...\n")
    pause()
    print("TWO ITEMS EACH.\n")
    pause()
    print("MORE ITEMS BEFORE EVERY LOAD.\n")
    select_items(player_1, player_2)
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


def select_items(player_1: player.Player, player_2: player.Player):
    items = ["Beer can", "Cigarette", "Saw", "Magnifying glass", "Handcuffs"]
    p1_len = len(player_1.inventory)
    p2_len = len(player_2.inventory)

    for _ in range(2):
        if p1_len < 8 or p2_len < 8:
            p1_item = random.randint(0, 4)
            p2_item = random.randint(0, 4)
            player_1.inventory.append(items[p1_item])
            player_2.inventory.append(items[p2_item])
        else:
            print("You can only carry 8 items", p1_len, p2_len)

    print("Your items are being chosen...")
    pause()
    print("\nItems in", player_1.name + "'s inventory: ")
    for i in player_1.inventory:
        print("- ", i)

    print("\n", player_2.name + "'s items are being chosen...")
    pause()
    print("\nItems in", player_2.name + "'s inventory: ")
    for i in player_2.inventory:
        print("- ", i)


def player_item(turn, player_1: player.Player, player_2: player.Player, gun: shotgun.Shotgun, round, result):
    print("P1's Inv >>> ", player_1.inventory, player_1.name)
    item = False
    if round > 1:
        if turn == "p1":
            if len(player_1.inventory) > 0: # If there are no items in inventory, skip selection step
                print("Use an item? [YES] [NO]\n")
                ans = input().upper()
                ans.upper()
                if ans == 'YES' or ans == 'YEA' or ans == 'YE' or ans == 'Y':
                    item = True
                    print("\nSelect an item from your inventory\n")
                    
                    n=1
                    for i in player_1.inventory:
                        print("["+str(n)+"]", i)
                        n+=1

                    inv_num = int(input())-1
                    item_selected = player_1.inventory[inv_num]
                    print("You have selected: ", item_selected)

                else:
                    print("No item selected")
            else:
                print("No more items in", player_1.name + "'s inventory.\n")

        if turn == 'p2':
            if len(player_2.inventory) > 0:
                inv_num = random.randint(0, len(player_2.inventory)-1)
                item_selected = player_2.inventory[inv_num]
                print(player_2.name, "has selected: ", item_selected)
                pass
            else:
                print("No more items in", player_2.name + "'s inventory.\n")
            
    check = False # check is set to true if item is selected but cant be used
    eject = False
    freeze_turn = False
    double_damage = False
    if round > 1 and item:
        match item_selected:
            
            # Beer can - eject current cartridge from chamber
            case "Beer can":
                eject = True
                if result == 'L':
                    print("A live round was ejected from the chamber.")
                else:
                    print("A blank round was ejected from the chamber.")

            # Cigarette - increase 1 health
            case "Cigarette":
                # If health is already at max, don't add more health
                if (round == 2 and player_1.health == 4) or (round == 3 and player_1.health == 6):
                    check = True
                    print("\nYour health is already maxxed. You can't use this item.\n")
                elif (round == 2 and player_2.health == 4) or (round == 3 and player_2.health == 6):
                    check = True
                    print("\n", player_2.health, "'s health is already maxxed. They can't use this item.\n")
                else:
                    if turn == 'p1':
                        player_1.health += 1
                        print("Your health has now increased to ", player_1.health)
                    else:
                        player_2.health += 1
                        print(player_2.health, "'s health has now increased to ", player_2.health)

            # Saw - double damage on next shot
            case "Saw":
                print("Your next shot will do double damage.")
                if result == 'L':
                    double_damage = True
                pass

            # Magnifying glass - see what is in chamber
            case "Magnifying glass":
                if result == 'L':
                    print("The magnifying glass shows you the next shot in the chamber is a live round.")
                else:
                    print("The magnifying glass shows you the next shot in the chamber is a blank round.")

            # Handcuffs - take two turns
            case "Handcuffs":
                freeze_turn = True
                pass
        
        if not check: # If check is True, item not removed from inventory as it can't be used
            if turn == 'p1':
                player_1.inventory.remove(item_selected)
            else:
                player_2.inventory.remove(item_selected)

    return double_damage, eject, freeze_turn


def game(gun: shotgun.Shotgun, player_1: player.Player, player_2: player.Player, round):
    turn = "p2" # set to p2 initially because it will get imediently flipped
    freeze_turn = False

    if round == 1:
        round_1()
        player_1.set_health(round)
        player_2.set_health(round)
        reload = 0
        gun.reload_gun(reload)
    elif round == 2:
        player_1.reset_inv()
        player_2.reset_inv()
        round_2(player_1, player_2)
        player_1.set_health(round)
        player_2.set_health(round)
        reload = 2
        gun.reload_gun(reload)
    elif round == 3:
        player_1.reset_inv()
        player_2.reset_inv()
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
            if not freeze_turn:
                turn = "p2" if turn == "p1" else "p1" # Flips turn
            result = gun.shoot()

            if turn == "p1":
                print("It is your turn.\n")
                pause()
                dub_dam, eject, freeze_turn = player_item(turn, player_1, player_2, gun, round, result)
                print(u"Shoot\u001b[31m\u001b[1m yourself [1]\u001b[0m or \u001b[31m\u001b[1m" + player_2.name, "[2]\u001b[0m ?\n")
                player_1.health, player_2.health = player1Choice(player_1, player_2, result, dub_dam, eject)
                
            if turn == "p2":
                print("It is", player_2.name + "'s turn.\n")
                pause()
                dub_dam, eject, freeze_turn = player_item(turn, player_1, player_2, gun, round, result)
                print(player_2.name, "is deciding...\n")
                player_1.health, player_2.health = player2Choice(player_1, player_2, result, dub_dam, eject)
                
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
    #test.gui() # This works!
    initialise()


if __name__ == "__main__":
    main()