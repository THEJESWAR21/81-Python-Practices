import random

class Bagels:
    # Constants
    MAX_GUESSES = 10
    MAX_NUM = 3

    def __init__(self) -> None:
        """Initalizes a new game by generating a number"""
        # Runs first when the package is fully imported
        self.secretNumber = self.generate_secret_number()

        
    def generate_secret_number(self):
        """Generate a 3 digits random number"""
        return str(random.randint(100,999))

    
    def get_clues(self,guess):
        """Return clues based on the answer and the secret number"""
        clues = []
        for i in range(len(guess)):
            if guess[i] == self.secretNumber[i]:
                # One Digit is correct and in the right position
                clues.append("Fermi")
            elif guess[i] in self.secretNumber:
                # One digit is correct but in the incorrent position
                clues.append("Pico")
        
        if len(clues) == 0:
            clues.append("Bagels")
        return clues
    
    
    def is_valid_guess(self, guess):
        """Check whether the guess is a valid input or not"""
        return len(guess) == self.MAX_NUM and guess.isdigit()


    def play_game(self):
        """Contains the game loop"""
        print("""
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
I have thought up a number.
You have 10 guesses to get it.
""")
        
        for chances in range(1,self.MAX_GUESSES+1):
            print(f"Guess #{chances}")
            guess = ''
            while not self.is_valid_guess(guess):
                guess = input("> ")
                if not self.is_valid_guess(guess):
                    print("Invalid input! Please enter a 3-digit number.")
        
            clues = self.get_clues(guess)
            print(" ".join(clues))

        if guess == self.secretNumber:
            print("You Win!")
            print()
        else:
            print(f'You are out of gueeses the real answer is {self.secretNumber}.')
            print()
            
        self.play_again()


    def play_again(self):
        """End Game Option"""
        while True:
            print("Do you want to play again? (yes or no)")
            end_game = input("> ")
            if end_game == 'yes':
                self.__init__() # Restarts the game
                self.play_game()
            elif end_game == 'no':
                print("Thanks for playing")
                print()
                exit()
            else:
                print("Please enter Yes or No.")

if __name__ == "__main__":
    Bagels().play_game()
