"""
 Jordan Brown
 10/28/2024
 Contains all the needed objects to model a blackjack game to be extended
 into functionality to connect different algorithms to the gui and
 controller
 
 Hit modelled as a 1, stand a 0
 Usable ace returns true if usable, false otherwise
"""

import random

testingBool = True

 # Card class that creates cards when provided an integer suit and value
 # Card Values: [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
 # Card Values in Program: [1, 2, 3, 4, 5, 8, 7, 8, 9, 10, 11, 12, 13]
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    #def __repr__(self):
        #return str(self.value) + " of " + str(self.suit)
        
     # A repr that converts integer cards into "value of suit" where
     # value consists of Ace, 2, 3, ... King and the Suits are Hearts,
     # Diamonds, Clubs, Spades
    def __repr__(self):
        returnString = ""
        if self.getValue() == 1:
            returnString += "Ace"
        elif self.getValue() == 11:
            returnString += "Jack"
        elif self.getValue() == 12:
            returnString += "Queen"
        elif self.getValue() == 13:
            returnString += "King"
        else:
            returnString += str(self.getValue())
        
        returnString += " of "
        
        if self.getSuit() == 1:
            returnString += "Hearts"
        elif self.getSuit() == 2:
            returnString += "Diamonds"
        elif self.getSuit() == 3:
            returnString += "Clubs"
        elif self.getSuit() == 4:
            returnString += "Spades"
            
        return returnString
            
    
    def getSuit(self):
        return self.suit
    
    def getValue(self):
        return self.value

 # Deck class that takes a number of decks and creates one deck that
 # incorporates all 52 cards from each requested deck. Each deck is
 # composed of cards (ace to king) of each of the four suits (hearts,
 # diamonds, clubs and spades in that numeric order) also provides
 # the functionality for shuffling the deck and giving cards from the
 # deck, popping them off the stack
class Deck:
    def __init__(self, numDecks):
         # 1 is hearts, 2 is diamonds, 3 is clubs, 4 is spades
        suits = [1, 2, 3, 4]
        value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        
        self.cards = []
        numMade = 0
        
        while numMade < numDecks:
            for suit in suits:
                for num in value:
                    self.cards.append(Card(suit,num))
            numMade += 1
        
    def getCards(self):
        return self.cards
    
    def addDecks(self, numDecks):
        deck = Deck(numDecks)
        for card in deck.cards:
            self.cards.append(card)
    
    def getSize(self):
        return len(self.cards)
        
    def __repr__(self):
        return "Deck containing " + str(len(self.cards)) + " cards."
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def giveCard(self):
        return self.cards.pop(0)
        
 # Hand class that creates an empty list in the hand ready to
 # accept cards and provides functionality for drawing cards from
 # a given deck object into the list, printing all cards in the
 # list, and counting the value  of all cards in the list
class Hand:
    def __init__(self):
        self.hand = []
        
    def __repr__(self):
        return repr(self.hand)
        
    def draw(self, deck):
        self.hand.append(deck.giveCard())
        
    def addCard(self, value, suit):
        self.hand.append(Card(suit, value))
        
        
    def countHand(self):
        totalValue = 0
        numAces = 0
        
        if testingBool == True:
            print("START OF COUNT")
            print("HAND PROVIDED HAS " + repr(self.hand))
        
        for x in self.hand:
            if x.getValue() == 1:
                numAces += 1
            elif x.getValue() >= 10:
                totalValue += 10
            else: 
                totalValue += x.getValue()
                
        if testingBool == True:
            print("In hand " + str(numAces) + " were found!")
            print()
            
        totalValue += numAces
        
        numCounted = 0
        numUsed = 0
        
        while numCounted != numAces:
            tempValue = totalValue
            if tempValue + 10 > 21:
                if testingBool == True:
                    print("Ace found but could not be used without going over 21")
                    print("Current Value: " + str(tempValue))
                    print("Value with ace: " + str(tempValue + 10))
                    print()
                    
                numCounted += 1
            else:
                if testingBool == True:
                    print("Ace could be used!")
                    print("Past Value: " + str(tempValue))
                    print("Current Value: " + str(tempValue + 10))
                    print()
                totalValue += 10
                numUsed += 1
                numCounted += 1
            
            if testingBool == True:
                print("Number of Aces is " + str(numAces) + " while we have counted " + str(numCounted) + " and used " + str(numUsed))
            
        if numUsed > 0:
            return totalValue, True
        else:
            return totalValue, False
        
 # Automatically plays a given number of games but can be expanded into 
 # modelling player, dealer, and machine hands depending on implementation
def playGame():
    oneHand = False
    
    games = 0
    wins = 0
    losses = 0
    draws = 0
    
    numGames = int(input('Enter number of games to play: '))
    numPlayed = 0
    
    deck = Deck(6)
    
    deck.shuffle()
    
    while numPlayed < numGames:
        # In futre add randomized shoe, for now its at 52
        if deck.getSize() <= 52:
            deck.addDecks(5)
            deck.shuffle()
        
        dealer = Hand()
        player = Hand()
        
        player.draw(deck)
        dealer.draw(deck)
        player.draw(deck)
        dealer.draw(deck)
        
        playerValue, playerUsableAce = player.countHand()
        dealerFaceValue = dealer.hand[0].getValue()
        
        if testingBool == True:
            print("Player: " + repr(player))
            print("Player Count: " + str(playerValue))
            print("Player Usable Ace: " + str(playerUsableAce))
        
            print("Dealer: " + repr(dealer.hand[0]))
            print("Shown Dealer Value: " + str(dealerFaceValue))
            print()
        
        result = 2
        
        if oneHand == True:
            # Soft blackjack hands if user has no usable ace
            if playerUsableAce == True:
                result = probabilityGame.softHands(playerValue, dealerFaceValue)
            elif playerUsableAce == False:
                result = probabilityGame.hardHands(playerValue, dealerFaceValue)
                
            if result == 1:
                # Algorithm chose hit!
                player.draw(deck)
                
                playerValue, playerUsableAce = player.countHand()
                
                if testingBool == True:
                    print("Result of Hit: " + str(result))
                    print("Player: " + repr(player))
                    print("Player Count: " + str(playerValue))
                    print("Player Usable Ace: " + str(playerUsableAce))
                    print()
                    
        else:
            while result != 0:
                if playerUsableAce == True:
                    result = probabilityGame.softHands(playerValue, dealerFaceValue)
                elif playerUsableAce == False:
                    result = probabilityGame.hardHands(playerValue, dealerFaceValue)
                
                if result == 1:
                    # Algorithm chose hit!
                    player.draw(deck)
                    
                    playerValue, playerUsableAce = player.countHand()
                    
                    if testingBool == True:
                        print("Result of Hit: " + str(result))
                        print("Player: " + repr(player))
                        print("Player Count: " + str(playerValue))
                        print("Player Usable Ace: " + str(playerUsableAce))
                        print()
        
        if playerValue > 21:
            if testingBool == True:
                print("Over 21! House Always Wins...")
                print("Player Value: " + str(playerValue))
                print()
                
            losses += 1
            games += 1
        else:
            dealerValue, dealerUsableAce = dealer.countHand()
            
            while dealerValue < 17:
                dealer.draw(deck)
                dealerValue, dealerUsableAce = dealer.countHand()
            
            if dealerValue > 21:
                if testingBool == True:
                    print("Dealer Over 21! You somehow won!")
                    print("Dealer Value: " + str(dealerValue))
                    print("Player Value: " + str(playerValue))
                    print()
                    
                wins += 1
                games += 1
            
            else:
                if dealerValue > playerValue:
                    if testingBool == True:
                        print("House Always Wins...")
                        print("Dealer Value " + str(dealerValue) + " versus Player Value " + str(playerValue))
                        print()
                        
                    losses += 1
                    games += 1
                    
                elif dealerValue < playerValue:
                    if testingBool == True:
                        print("You somehow won!")
                        print("Dealer Value " + str(dealerValue) + " versus Player Value " + str(playerValue))
                        print()
                    
                    wins += 1
                    games += 1
                else:
                    if testingBool == True:     
                        print("You tied...")
                        
                    games += 1
                    draws += 1
        
        numPlayed += 1
    
    if wins > losses:
        print("Overall, you won with a winrate of " + str((float(wins)/float(games)) * 100.0))
        print("Or " + str(wins) + " wins and " + str(losses) + " losses")
        print("Of those, you drew " + str(draws) + " times")
        print()
    else:
        print("Overall, you lost with a winrate of " + str((float(wins)/float(games)) * 100.0))
        print("Or " + str(wins) + " wins and " + str(losses) + " losses")
        print("Of those, you drew " + str(draws) + " times or %" + str((float(draws) / float(games) * 100.0)))
        print()
        
class probabilityGame:
    
     # A method that takes in a player value with no usable ace (i.e
     # a hand that cannot be reduced by 10 by an ace should the hit take
     # it over 21) and decides using generally approved blackjack strategy
     # whether the player should hit or stand
     # Link to Chart:https://www.blackjackapprenticeship.com/blackjack-strategy-charts/
     # Structed by dealer hands then player hands
    def hardHands(playerValue, dealerValue):
         # hit modelled by a 1, stand is zero
           
         # array[playerValue][dealerValue] shows what action should be taken
         # but this only shows hit and stand, double to be added later
         # Since ace is modelled as a one it is stored in the 0th index of
         # playerValue
        hardArray = [[1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,0,0,0,1,1,1,1],
                     [1,0,0,0,0,0,1,1,1,1],
                     [1,0,0,0,0,0,1,1,1,1],
                     [1,0,0,0,0,0,1,1,1,1],
                     [1,0,0,0,0,0,1,1,1,1],
                     [0,0,0,0,0,0,0,0,0,0]]
           
         # 0th index for player value is 8 as everything below 8 is the same
         # action so it is unecessary to model
         # Everything 17 and above is the same action and doesn't need to be
         # stored separately
        if playerValue < 8:
            playerValue = 8
        elif playerValue > 17:
            playerValue = 17
               
         # If dealer has a face card, adjusts value
        if dealerValue > 10:
            dealerValue = 10
            
         # Adjusts player andd dealer value, player by 8 to adjust for min
         # value stored being 8 at 0th index, and dealer by 1 as minimum value
         # dealer could show is 2 (so it would be - 2) but ace is modelled as
         # a 1 so its minus 1, with ace at 0th, 2 at 1st, 3 at 2nd, etc.
        result = hardArray[playerValue - 8][dealerValue - 1]
        
        if testingBool == True:
            print(hardArray[playerValue - 8])
            print(str((playerValue - 8)))
            print(result)
        
        return result
    
     # A method that takes a player value with a usable ace (i.e meaning
     # that if the the hit puts the player over 21 they can still fall 
     # back ten points by changing ace from 11 to 1) and a dealer value
     # before deciding whether the player should hit or stand based
     # soley on generally approved poker probability
     # Link to char used here: https://www.blackjackapprenticeship.com/blackjack-strategy-charts/
     # Structed to find dealer value first before checking player value
    def softHands(playerValue, dealerValue):
         # Hit modelled by a 1, stand is 0
        
         # array[playerValue][dealerValue], similar to hardArray but since min
         # value player can have is 13 the 0th entry is 13
        softArray = [[1,1,1,1,1,1,1,1,1,1], 
                     [1,1,1,1,1,1,1,1,1,1], 
                     [1,1,1,1,1,1,1,1,1,1], 
                     [1,1,1,1,1,1,1,1,1,1], 
                     [1,1,1,1,1,1,1,1,1,1], 
                     [1,0,0,0,0,0,0,0,1,1], 
                     [0,0,0,0,0,0,0,0,0,0], 
                     [0,0,0,0,0,0,0,0,0,0]]
        
         # Player values over 20 (21) would be the same as 20 so no need to
         # model
        if playerValue > 20:
            playerValue = 20
            
         # Jack, Queen and King are all modelled as 11,12 and 13 respectively
         # but are identical to ten so they don't have separate indicies
        if dealerValue > 10:
            dealerValue = 10
        
         # Since 13 is the starting amount you can have for a soft hand, (Ace
         # a 2) the 0th entry for player value must be subracted by 13. Dealer
         # would again be - 2 for
        result = softArray[playerValue - 13][dealerValue - 1]
        
        if testingBool == True:
            print(softArray[playerValue - 13])
            print(str((playerValue - 13)))
            print(result)
        
        return result
