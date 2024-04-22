import shotgun
import player

class Items:

    def select_item(item_selected):
        pass
    
    # Beer can - eject current cartridge from chamber
    def beer_can(cartridge_shot, gun):
        #gun.rounds.remove(cartridge_shot)
        print(">>>> beer can called", cartridge_shot, " plus gun ", gun.rounds)

    #Cigarette - increase 1 health
    def cigarette():
        pass

    # Saw - double damage on next shot
    def saw():
        pass

    # Magnifying glass - see what is in chamber
    def mag_glass():
        pass

    # Handcuffs - take two turns
    def handcuffs():
        pass