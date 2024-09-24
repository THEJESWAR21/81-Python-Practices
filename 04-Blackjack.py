# Todo
# [x] - Ask the input to get the bet value
# [x] - A Loop to create a deck of 52 cards
# [ ] - Return the first random 2 card hit from both player and dealer
# [ ] - Make the hit , stand and Double down option work


import random

class Blackjack:
    # Define Constants
    HEARTS = chr(9829)
    DIAMONDS = chr(9830)
    SPADES = chr(9824)
    CLUBS = chr(9827)
    BACKSIDE = 'backside'

    def __init__(self) -> None:
        self.bet = self.get_bet()
        self.deck = self.get_deck()

    def get_bet(self):
        print('How much do you bet? (1-5000, or QUIT) ')
        return int(input("> "))

    def get_deck(self):
        deck = []
        for suits in (self.HEARTS, self.DIAMONDS, self.SPADES, self.CLUBS):
            for rank in range(2,11):
                deck.append((str(suits), rank))
            for rank in ('J','Q','K','A'):
                deck.append((suits, rank))
            
        random.shuffle(deck)
        print(len(deck))
        print(deck)
        return deck
    
    def play_game(self):
        DEALER = 0
        PLAYER = 0

        
Blackjack()