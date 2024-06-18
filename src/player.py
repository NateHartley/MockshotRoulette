class Player:
    def __init__(self):
        self.name = ""
        self.health = None
        self.inventory = []


    def set_health(self, round):
        if round == 1:
            self.health = 2
        elif round == 2:
            self.health = 4
        elif round == 3:
            self.health = 6
            # last two health cannot be regenerated though
        else:
            print("--set_health error--")

    
    def reset_inv(self):
        self.inventory = []

    # loose_health()
            
    # gain_health()