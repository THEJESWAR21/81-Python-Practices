import random 
# Todo
# [x] - A Function to get the bet input
# [x] - A Function to create all 52 deck of cards
# [x] - Give the dealer and player two cards from the deck each 
# [x] - Hand Value Calculation
# [x] - Game loop for the player moves
# [ ] - win, loss logic
# [ ] - Display hands and cards
# [ ] - Error Handling

class Blackjack:
    #Unicode Characters for suits
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
        return int(input("> "))


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
    

    def display_hands(self):
        self.calculate_player_hand()
        dealer_display_hand = [card if card != self.BACKSIDE else '????' for card in self.DEALER_HAND]
        print("Player's hand: ", self.PlAYER_HAND)
        print("Dealer's hand:", dealer_display_hand)

        print("player's hand value:", self.PLAYER)
        if self.BACKSIDE in self.DEALER_HAND:
            print("Dealer's Hand Value: ????")
        else:
            self.calculate_dealer_hand()
            print(f"Dealer's Hand Value: {self.DEALER}")


    def calculate_player_hand(self):
        self.PLAYER = 0
        aces = 0

        for card, suit in self.PlAYER_HAND:
            if card.isdigit():
                self.PLAYER += int(card)
            elif card in ('J', 'Q', 'K'):
                self.PLAYER += 10
            elif card == 'A':
                aces += 1
                self.PLAYER += 11
        
        while self.PLAYER > 21 and aces:
            self.PLAYER -= 10
            aces -= 1
        

    def calculate_dealer_hand(self):
        self.DEALER = 0
        aces = 0 

        for card, suit in self.DEALER_HAND:
            if card == self.BACKSIDE:
                continue # Skip this card
            elif card.isdigit():
                self.DEALER += int(card)
            elif card in ('J','Q','K'):
                self.PLAYER += 10
            elif card == "A":
                aces += 1
                self.DEALER += 11
                
        while self.DEALER > 21 and aces:
            self.DEALER -= 10
            aces -= 1

    def player_turn(self):
        while True:
            print("(H)it, (S)tand, (D)ouble down")
            move = input("> ").upper()

            if move == "H":
                self.PlAYER_HAND.append(random.choice(self.DECK))
                self.display_hands()
                if self.PLAYER >= 21:
                    print("BUST! You went over 21")
                    break

            elif move == "S":
                self.dealer_turn()
                break

            elif move == "D":
                self.BET_VALUE = self.BET_VALUE * 2
                print(self.BET_VALUE)
                self.PlAYER_HAND.append(random.choice(self.DECK))
                self.display_hands()
                if self.PLAYER >= 21:
                    print("BUST! You went over 21")
                    break
                else:
                   self.dealer_turn()
                break
            else:
                print("Invalid move. Please enter 'H''S' or 'D'.")


    def dealer_turn(self):
        print("\nDealer's turn.")
        self.DEALER_HAND[0] = random.choice(self.DECK)
        self.calculate_dealer_hand()

        while self.DEALER < 17:
            self.DEALER_HAND.append(random.choice(self.DECK))
            self.DEALER_HAND()
            self.display_hands()
    
        self.check_winner()
    
    def check_winner(self):
        if self.DEALER > 21:
            print("Dealer busts! You win!")
        elif self.PLAYER > self.DEALER:
            print("You win with a hand value of", self.PLAYER)

        elif self.DEALER > self.PLAYER:
            print("Dealer wins with a hand value of", self.DEALER)
        else:
            print("It's a tie!")


    def play_game(self):
        print("Bet:",self.BET_VALUE)
        
        # Players get 2 cards at the start 
        for x in range(2):
            self.PlAYER_HAND.append(random.choice(self.DECK))
            if x == 0:
                self.DEALER_HAND.append(self.BACKSIDE)
            else:
                self.DEALER_HAND.append(random.choice(self.DECK))
        
        self.display_hands()
        self.player_turn()


Blackjack().play_game()