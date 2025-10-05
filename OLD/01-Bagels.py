import random

class BagelGame:
    def __init__(self, num_digits=3, max_guesses=10):
        self.num_digits = num_digits
        self.max_guesses = max_guesses
        self.secret_number = self._generate_secret_number()
        self.guess_count = 0
        
    def _generate_secret_number(self):
        return str(random.randrange(100,1000))
    
    def display_header(self):
        print("""Bagels, a deductive logic game.
        By Al Sweigart al@inventwithpython.com
        I am thinking of a 3-digit number. Try to guess what it is.
        Here are some clues:
        When I say:    That means:
        Pico         One digit is correct but in the wrong position.
        Fermi        One digit is correct and in the right position.
        Bagels       No digit is correct.
        I have thought up a number.
        You have 10 guesses to get it.""")

    
    def get_clues(self, guess):
        if guess == self.secret_number:
            return ['You Won']
        
        clues = []
        for i in range(len(guess)):
            if guess[i] == self.secret_number[i]:
                clues.append("Fermi")
            elif guess[i] in self.secret_number:
                clues.append("Pico")

        if not clues:
            return ['Bagels']
        
        clues.sort()
        return clues
    
    def is_valid_guess(self, guess):
        return guess.isdigit() and len(guess) == self.num_digits
    
    def play_game(self):
        self.display_header()
        print("Enter Your Guesses")

        while self.guess_count < self.max_guesses:
            self.guess_count += 1
            print(f'\nGuess #{self.guess_count}')
            guess = input("> ")
            
            if not self.is_valid_guess(guess):
                print('Invalid input. Enter a 3-digit number.')
                self.guess_count -= 1
                continue

            clues = self.get_clues(guess)
            print(*clues)

            if clues == ['You Won']:
                break

        else:
            print(f"You are out of tires. The number was {self.secret_number}. Try again Later.")

if __name__ == "__main__":
    game = BagelGame()
    game.play_game()
            
    