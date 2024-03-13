import random
# Each instance of Shotgun has rounds containing lives and blanks, and total rounds
class Shotgun:
    def __init__(self, rounds, total_rounds):
        self.rounds = rounds             # Example: ["L", "B", "B"]
        self.total_rounds = total_rounds # Example: 3

    # Instance method
    def shoot(self):
        # TODO: Occasionally will get an out of range error with rand, need to fix
        if len(self.rounds) > 0:
            rand = random.randint(0, self.total_rounds-1) # 1-3 is out of range, needs to be 0-2
            print(">>> rand: ", rand)
            print(">>> total rounds: ", self.total_rounds)
            chosen_round = self.rounds[rand]
            print(">>> chosen round: ", chosen_round)
            self.total_rounds -= 1
            del self.rounds[rand]
            return chosen_round
        else:
            print("No more shots left")
            exit
        # Get rid of if else once above todo is done