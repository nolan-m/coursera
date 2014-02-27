# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
outcome2 = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
            return "Hand contains " + " ".join(str(card) for card in self.hand)
    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        
        hand_value = 0
        
        for card in self.hand:
            hand_value += VALUES[card.get_rank()]       
            
        for card in self.hand:
            if card.get_rank() == "A":            
                if hand_value + 10 <= 21:
                    return hand_value + 10
        return hand_value

   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        pos = [pos[0], pos[1]]
        for c in self.hand:           
            c.draw(canvas, pos)
            pos[0] += CARD_SIZE[1]

            
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank))
                
    def shuffle(self):
        # shuffle the deck 
        return random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop(0)
    
    def __str__(self):
        # return a string representing the deck
        return "Deck contains " + " ".join(str(card) for card in self.deck)


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, score, outcome2
    
    if in_play == True:
        score -= 1
           
    # your code goes here
    in_play = True
    outcome2 = ""
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    outcome = "Hit or stand?"    

    

def hit():
    global in_play, player_hand, deck, outcome, score, outcome2
    # replace with your code below

    # if the hand is in play, hit the player
    if in_play == True:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())    

    # if busted, assign a message to outcome, update in_play and score
    if player_hand.get_value() > 21:        
        if in_play == True:
            score -= 1
        in_play = False
        outcome = "New deal?"
        outcome2 = "You have busted." 
        


def stand():
    global in_play, deck, player_hand, dealer_hand, outcome, score, outcome2
    # replace with your code below

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if player_hand.get_value() > 21:
        outcome2 = "You have busted."
        if in_play == True:
            score -= 1
    else:
        while dealer_hand.get_value() <= 17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            outcome2 = "Dealer busts."
            if in_play == True:
                score += 1            
        else:
            if player_hand.get_value() <= dealer_hand.get_value():
                outcome2 = "Dealer wins!"
                if in_play == True:
                    score -= 1
            else:
                outcome2 = "You win!"
                if in_play == True:
                    score += 1
                
    # assign a message to outcome, update in_play and score
    in_play = False
    outcome = "New deal?"

            
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    player_hand.draw(canvas, (50, 300))
    dealer_hand.draw(canvas, (50, 100))
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [86,150], CARD_BACK_SIZE)
    #canvas.draw_text(text, point, font_size, font_color, font_face)
    canvas.draw_text(outcome, (50,500), 35, "White", "sans-serif")
    canvas.draw_text(outcome2, (50,450), 35, "White", "sans-serif")
    canvas.draw_text("Blackjack", (175, 50), 50, "White", "sans-serif")
    canvas.draw_text("Score: " + str(score), (50, 550), 25, "White", "sans-serif")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric