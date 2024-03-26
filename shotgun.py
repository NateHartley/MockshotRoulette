import random

class Shotgun:
    def __init__(self, rounds, total_rounds):
        self.rounds = rounds             # Example: ["L", "B", "B"]
        self.total_rounds = total_rounds # Example: 3


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
        
    
    def reload_gun(self, reload):
        if reload == 0: # Start of round 1
            self.rounds = ["L", "B", "B"]
            self.total_rounds = 3
        elif reload == 1:
            self.rounds = ["L", "L", "L", "B", "B"]
            self.total_rounds = 5
        elif reload == 2: # Start of round 2
            self.rounds = ["L", "B"]
            self.total_rounds = 2
        elif reload == 3:
            self.rounds = ["L", "L", "B", "B"]
            self.total_rounds = 4
        elif reload == 4:
            self.rounds = ["L", "L", "L", "B", "B"]
            self.total_rounds = 5
        elif reload == 5: # Made up (DOUBLE CHECK ON VIDEOS)
            self.rounds = ["L", "L", "B", "B"]
            self.total_rounds = 4
        elif reload == 6: # Start of round 3
            self.rounds = ["L", "B", "B"]
            self.total_rounds = 3
        elif reload == 7:
            self.rounds = ["L", "L", "L", "L", "B", "B", "B", "B"]
            self.total_rounds = 8
        elif reload == 8:
            self.rounds = ["L", "L", "L", "B", "B"]
            self.total_rounds = 5
        elif reload == 9: # Made up (DOUBLE CHECK ON VIDEOS)
            self.rounds = ["L", "L", "L", "L", "B", "B"]
            self.total_rounds = 6
        else:
            print("--Reload error--")
            quit()

        if reload != 0 and reload != 2 and reload != 6:
            counter_L, counter_B = 0, 0
            for i in self.rounds:
                if i == "L":
                    counter_L += 1
                if i == "B":
                    counter_B += 1
            
            print("It now contains", self.total_rounds, "rounds;", counter_L, "live,", counter_B, "blank.\n")