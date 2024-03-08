import random

# Each instance of Shotgun has rounds containing lives and blanks, and total rounds
class Shotgun:
    def __init__(self, rounds, total_rounds):
        self.rounds = rounds # Example: ["l", "b", "b"]
        self.total_rounds = total_rounds # Example: 3

    # Instance method
    def shoot(self):
        if len(self.rounds) > 0:
            rand = random.randint(0, self.total_rounds-1) # 1-3 is out of range, needs to be 0-2
            chosen_round = self.rounds[rand]
            self.total_rounds -= 1
            del self.rounds[rand]
            return chosen_round
        else:
            print("No more shots left")
            exit