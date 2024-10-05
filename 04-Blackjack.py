import random
# Todo
# [x] - A Function to get the bet input
# [x] - A Function to create all 52 deck of cards
# [x] - Give the dealer and player two cards from the deck each 
# [ ] - Hand Value Calculation
# [ ] - Game loop for the player moves
# [ ] - Display hands and cards
# [ ] - win, loss logic
# [ ] - Error Handling

class Blackjack:
    HEARTS = chr(9829)
    DIAMONDS = chr(9830)
    SPADES = chr(9824)
    CLUBS = chr(9827)
    BACKSIDE = "backside"

    def __init__(self):
        self.BET_VALUE = self.get_bet()
        self.DECK = self.create_deck()
        self.PlAYER_HAND = []
        self.DEALER_HAND = []   
        self.PLAYER = 0
        self.DEALER = 0

    def get_bet(self):
        print("How much do you bet? (1-5000, or QUIT)")
        return input("> ")

    def create_deck(self):
        """Create 52 card deck with tuples in a list"""
        deck = []
        for suits in (self.HEARTS, self.DIAMONDS, self.SPADES, self.CLUBS):
            for rank in range(2,11):
                deck.append((str(rank), suits))
            for rank in ('J','Q','K',"A"):
                deck.append((rank, suits))

        random.shuffle(deck)
        return deck
    
    def play_game(self):
        print("Bet:",self.BET_VALUE)

        # Players get 2 cards at the start 
        for x in range(2):
            self.PlAYER_HAND.append(random.choice(self.DECK))
            if x == 0:
                self.DEALER_HAND.append(self.BACKSIDE)
            else:
                self.DEALER_HAND.append(random.choice(self.DECK))
        
        self.hand_value()
        print(self.PlAYER_HAND)
        print(self.DEALER_HAND)
        print(self.PLAYER)

    def hand_value(self):
        while True:
            for x in range(len(self.PlAYER_HAND)):
                for y in range(1):
                    try:
                        i = int(self.PlAYER_HAND[x][y])
                    except ValueError:
                        self.PLAYER += 10
                    else:
                        self.PLAYER += i
                        
            break

Blackjack().play_game()