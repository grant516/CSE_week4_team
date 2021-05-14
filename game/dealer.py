import random

# TODO: Define the Thrower class here.
class Dealer:
    """Where the dice is thrown"""

    def __init__(self):
        self.card = 0
        self.right_v_wrong = True

    def draw_card(self):
        """chooses a random card"""

        self.card = random.randint(1, 14)

    def get_points(self, guess="h"):
        """get the points"""
        first_card = self.card
        points = 0
        while(first_card == self.card):
            self.draw_card()
        if(guess.lower() == "h"):
            if(first_card < self.card):
                points += 100
                self.right_v_wrong = True
            else:
                points += -75
                self.right_v_wrong = False
        elif(guess.lower()== "l"):
            if(first_card > self.card):
                points += 100
                self.right_v_wrong = True
            else:
                points += -75
                self.right_v_wrong = False

        return(points)
        #determine if the player's choice was higher or lower and if they were right

    def can_shuffle(self, score):
        """Checks to see if the dealer needs to shuffle again"""
        if(score > 0):
            return(True)
        elif(score <= 0):
            return(False)

        #Check if there were any 1s or 5s rolled that round (this function returns a boolean)