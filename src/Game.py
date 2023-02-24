

class Game():
    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        score = 0
        for i in range(0,20,2):
            score += self._rolls[i] + self._rolls[i+1]             
            if (self._rolls[i] + self._rolls[i+1] == 10):
                score += self._rolls[i+2] 
                
        return score
