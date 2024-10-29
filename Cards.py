# Cards.py
# Authors:
#
#
#
# This file contains the Card, Deck, and Hand classes.

import random

class Card:
   
    # Create a card object
    def __init__(self, suit: int, value: int):
       
        #Check to make sure suit is valid
        assert suit in [1, 2, 3, 4], "invalid suit"
       
        #Check to make sure value is valid    
        assert value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
       
        self.suit = suit
        self.value = value
       
     
    # Return a string readable format of the card
    def __str__(self)->str:
        #Convert suit to appropriate name
        if(self.suit == 1):
            suit = "hearts"
        elif(self.suit == 2):
            suit = "diamonds"
        elif(self.suit ==3):
            suit = "clubs"
        else:
            suit = "spades"
           
       
        #Convert value to appropriate value
        if(self.value == 1):
            value = "A"
        elif(self.value == 11):
            value = "J"
        elif(self.value == 12):
            value = "Q"
        elif(self.value == 13):
            value = "K"
        else:
            value = int(value)        
        return f"{value} of {suit}"
   
   
    # Return the value of the card
    def getValue(self)->int:
        return self.value
       
       
class Deck:
   
    # Create a deck object
    def __init__(self, numDecks: int):
        # 1 is hearts, 2 is diamonds, 3 is clubs, 4 is spades
        suits = [1, 2, 3, 4]
        values = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13]
       
        self.cards = []
        numMade = 0
       
        # Create the deck
        while numMade < numDecks:
            for suit in suits:
                for value in values:
                    self.cards.append(Card(suit, value))
            numMade += 1
       
           
     
    # Return the deck of cards        
    def getCards(self)->list:
        return self.cards
       
    # Add additional decks of cards to the deck
    def addDecks(self, numDecks: int):
        deck = Deck(numDecks)
        for card in deck.cards:
            self.cards.append(card)
           
    # return the size of the decl
    def getSize(self)->int:
        return len(self.cards)
   
    # return a string that describes the deck of cards
    def __str__(self)->str:
        return "Deck containing " + str(self.getSize()) + " cards"
   
    # deal a card from the deck
    def dealCard(self)->Card:
        return self.cards.pop(0)
       
    #shuffule the deck
    def shuffle(self):
        random.shuffle(self.cards)
       
       


class Hand:
    def __init__(self):
        self.hand = []
       
    # string representation of the hand
    def __str__(self) -> str:
        handStr = ""
       
        i = 0

        while i < len(self.hand):
            handCard = self.hand[i]
            handStr += str(handCard)
            i += 1
            if i < len(self.hand):
                handStr += ", "
           
        return handStr
   
     
    # add a card to the hand        
    def addCard(self, Card):
        self.hand.append(Card)
       
    def handValue(self):
        for i in self.hand:
            if i.getValue() ==  b1:
                numAces += 1
            elif i
           
           
   

def main():
    myDeck = Deck(1)
    myDeck.shuffle()
    print(myDeck)
   
    playerHand = Hand()
    playerHand.addCard(myDeck.dealCard())
   
    playerHand.addCard(myDeck.dealCard())
   
    print(playerHand)
   
main()
