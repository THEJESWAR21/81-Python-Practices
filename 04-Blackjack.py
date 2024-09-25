# Todo
# [x] - A Function to ge the bet input
# [x] - A Function to create all 52 deck of cards
# [ ] - Give the dealer and player two cards from the deck each 
# [ ] - Hand Value Calculation
# [ ] - Game loop for the player moves
# [ ] - Display hands and cards
# [ ] - win, loss logic
# [ ] - Error Handling


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
        self.PLAYER = 0
        self.DEALER = 0

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
    
    def get_cards(self):
        while True:
            DEALER_Card = random.choice(self.deck) 
            PLAYER_Card = random.choice(self.deck)
            
            match DEALER_Card[1]:
                case 'J', 'Q', 'K':
                    self.DEALER += 10
                case 'A':
                    if self.DEALER + 11 > 21:
                        self.DEALER += 1
                    else:
                        self.DEALER += 11
                case 2,3,4,5,6,7,8,9,10,11:
                    self.DEALER += int(DEALER_Card[1])
    
            match PLAYER_Card[1]:
                case 'J', 'Q', 'K':
                    self.PLAYER += 10
                    return self.PLAYER
                case 'A':
                    if self.PLAYER + 11 > 21:
                        self.PLAYER += 1
                        return self.PLAYER
                    else:
                        self.PLAYER += 11
                        return self.PLAYER
                case 2,3,4,5,6,7,8,9,10,11:
                    self.PLAYER += int(PLAYER_Card[1])
                    return self.PLAYER
                    
            break
        
    def play_game(self):
        self.get_cards()
        print(self.DEALER)
        print(self.PLAYER)

        

Blackjack().play_game()