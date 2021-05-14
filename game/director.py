from game.dealer import Dealer
from colorama import Fore, Style

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        thrower (Thrower): An instance of the class of objects known as Thrower.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Director): An instance of Director.
        """
        self.dealer.draw_card()
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        print(f"\nThe card was: {self.dealer.card}")
        choice1 = input("Higher or lower? [h/l] ")
        points = self.dealer.get_points(choice1)
        self.score += points
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.

        Args:
            self (Director): An instance of Director.
        """
        print(f"Next card was: {self.dealer.card}")
        if(self.dealer.right_v_wrong):
            print(Fore.GREEN + f"Your score is: {self.score}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Your score is: {self.score}" + Style.RESET_ALL)
        if self.dealer.can_shuffle(self.score):
            choice2 = input("Keep playing? [y/n] ")
            self.keep_playing = (choice2 == "y")
        else:
            print("Better luck next time!\n")
            self.keep_playing = False