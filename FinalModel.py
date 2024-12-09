# File Name: Black Jack Model
# Author: Torryn Carey-Jarrell
#
# Model game for black jack

import random

import numpy as np

testingBool = False

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # def __repr__(self):
    # return str(self.value) + " of " + str(self.suit)

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
    #                 A  1  2  3  4  5  6  7  8  9  J  Q  K
    cardsUsed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    totalCardsInDeck = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, numDecks):
        # 1 is hearts, 2 is diamonds, 3 is clubs, 4 is spades
        suits = [1, 2, 3, 4]
        value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        self.cards = []
        numMade = 0

        while numMade < numDecks:
            for suit in suits:
                for num in value:
                    self.cards.append(Card(suit, num))
            numMade += 1
            self.incrementTotalCardsInDeck()

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
        card = self.cards.pop(0)
        self.countCards(card)
        return card

    def incrementTotalCardsInDeck(self):
        for i in range(len(self.totalCardsInDeck)):
            self.totalCardsInDeck[i] += 4

    def countCards(self, cardAdded):
        self.cardsUsed[cardAdded.getValue() - 1] += 1

    def printDeck(self):
        print("Total cards ever in Deck: " + str(sum(self.totalCardsInDeck)))
        print("Total cards found: " + str(sum(self.cardsUsed)))
        print("Total cards left: " + str(len(self.cards)))
        print("Ace - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 - J - Q - K")
        print(self.cardsUsed)

    def getNumBustCards(self, playerTotal):
        print(playerTotal)
        bustNumber = 21 - playerTotal
        print(bustNumber)

        if bustNumber > 10:
            return 0
        else:

            numBustCards = 0
            x = bustNumber + 1
            while x < len(self.totalCardsInDeck):
                print("X Value: " + str(x))
                print("Card " + str(x) + " has " + str(self.totalCardsInDeck[x]) + " total")
                print("and has been used " + str(self.cardsUsed[x]) + " times")
                numBustCards += self.totalCardsInDeck[x] - self.cardsUsed[x]
                print(self.totalCardsInDeck[x] - self.cardsUsed[x])
                x += 1

        print(numBustCards, sum(self.totalCardsInDeck))
        return numBustCards

    def resetClassVariables(self):
        Deck.cardsUsed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Deck.totalCardsInDeck = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


class Hand:
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return repr(self.cards)

    def draw(self, deck):
        self.cards.append(deck.giveCard())

    def addCard(self, value, suit):
        self.cards.append(Card(suit, value))

    def countHand(self):
        totalValue = 0
        numAces = 0

        if testingBool == True:
            print("START OF COUNT")
            print("HAND PROVIDED HAS " + repr(self.cards))

        for x in self.cards:
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
                print("Number of Aces is " + str(numAces) + " while we have counted " + str(
                    numCounted) + " and used " + str(numUsed))

        if numUsed > 0:
            return totalValue, True
        else:
            return totalValue, False
        
        
class BlackjackGame:
    # Define global action buttons
    ACTION_BUTTONS = {
        "hit": 1,
        "stand": 0,
        "double down": 2
        }
    
    def __init__(self, num_decks=6, starting_balance=100, algoNum=1):
        
        self.deck = Deck(num_decks)
        self.deck.shuffle()

        self.human_hand = Hand()
        self.computer_hand = Hand()
        self.dealer_hand = Hand()

        self.balance = starting_balance
        self.bet = 0

        self.algorithm = algoNum

        self.humanPlayerWins = 0  # 1 = win, 2 = loss, 0 = undecided
        self.computerPlayerWins = 0
        self.humanPlayerTurnDone = False
        self.computerPlayerTurnDone = False

        self.QTable = np.load("blackJackQTable.npy")

    #new addition, returns deck object
    def get_deck(self):
        return self.deck
    #new addition, return human hand object
    def get_playerHand(self):
        return self.human_hand
    def get_computerHand(self):
        return self.computer_hand
    def get_dealerHand(self):
        return self.dealer_hand

    def rewardIndex(self, action: int, usableAce: int) -> int:
        # if there is no usable Ace
        index = 0
        if usableAce == 0:

            if action == 0:
                index = 0
            else:
                index = 1

        # else if there is a usable ace
        elif usableAce == 1:

            if action == 0:
                index = 2
            else:
                index = 3

        return index

    # Chooses action based on Q Values from npy file
    def chooseAction(self, playerValue: int, dealerCard: int, usableAce: int, numBustCards: int,
                     totalCards: int) -> int:
        hitValue = self.QTable[playerValue, dealerCard, (self.rewardIndex(1, usableAce))]
        standValue = self.QTable[playerValue, dealerCard, (self.rewardIndex(0, usableAce))]

        #print("Number of Bust Cards " + str(numBustCards) + " out of " + str(totalCards))
        percentBustCards = numBustCards / totalCards

        #print("Bust Cards %" + str(percentBustCards))
        #print("Hit Value: " + str(hitValue))
        #print("Stand Value: " + str(standValue))

        if percentBustCards <= .01:
            hitValue += abs(hitValue)
        elif percentBustCards <= .05:
            hitValue += abs(hitValue * .8)
        elif percentBustCards <= .1:
            hitValue += abs(hitValue * .3)
        elif percentBustCards <= .15:
            hitValue += abs(hitValue * .2)
        elif percentBustCards <= .2:
            hitValue += abs(hitValue * .1)
        elif percentBustCards >= .4:
            standValue += abs(standValue * .5)
        elif percentBustCards >= .5:
            standValue += abs(standValue * .6)
        elif percentBustCards >= .6:
            standValue += abs(standValue * .7)

        #print("Hit Value After calculation: " + str(hitValue))
        #print()

        if hitValue > standValue:
            if hitValue > 0.95:
                return 2
            else:
                return 1
        else:
            return 0

    # Chooses action based on Q Values from npy file
    def chooseActionNoCardCount(self, playerValue: int, dealerCard: int, usableAce: int) -> int:
        hitValue = self.QTable[playerValue, dealerCard, (self.rewardIndex(1, usableAce))]
        standValue = self.QTable[playerValue, dealerCard, (self.rewardIndex(0, usableAce))]

        if hitValue > standValue:
            if hitValue > 0.95:
                return 2
            else:
                return 1
        else:
            return 0
    
    def start_game(self):
        """Initialize a new game and deal initial cards."""
        print("\n--- Starting a New Game ---")
        # Add cards if deck runs low
        if self.deck.getSize() <= 52:
            self.deck.resetClassVariables()
            self.deck = Deck(6)
            # deck.addDecks(6)
            self.deck.shuffle()

        self.human_hand = Hand()
        self.computer_hand = Hand()
        self.dealer_hand = Hand()

        self.humanPlayerWins = 0  # 1 = win, 2 = loss, 0 = undecided
        self.computerPlayerWins = 0
        self.humanPlayerTurnDone = False
        self.computerPlayerTurnDone = False
        
        # Deal two cards to each player and the dealer
        self.human_hand.draw(self.deck)
        self.human_hand.draw(self.deck)
        self.computer_hand.draw(self.deck)
        self.computer_hand.draw(self.deck)
        self.dealer_hand.draw(self.deck)
        
        print(f"Player's Hand: {self.human_hand}")
        print(f"Dealer's Shown Card: {self.dealer_hand.cards[0]}")
        
        
    def humanPlayerInput(self, action):
        print("MODEL HERE: !!!")
        print(action)
        # Match action to corresponding logic
        if action == 0:  # Stand
            print("Player stands.")
            self.setHumanPlayerTurnDone(True)
            self.computerPlayerTurn()
        elif action == 1:  # Hit
            print("Player hits.")
            print(self.human_hand.draw(self.deck))
            print(self.human_hand)
            humanValue, x = self.human_hand.countHand()
            if humanValue > 21:
                print("Player busts!")
                self.setHumanPlayerWin(2)  # Player loses
                self.setHumanPlayerTurnDone(True)
                self.computerPlayerTurn()
        elif action == 2:  # Double Down
            print("Player doubles down.")
            self.human_hand.draw(self.deck)
            humanValue, _ = self.human_hand.countHand()
            self.bet *= 2  # Double the bet
            self.setHumanPlayerTurnDone(True)
            self.computerPlayerTurn()
            if humanValue > 21:
                print("Player busts!")
                self.setHumanPlayerWin(2)  # Player loses
                self.setHumanPlayerTurnDone(True)
                self.computerPlayerTurn()
        
    def computerPlayerTurn(self):
        while not self.computerPlayerTurnDone:
            computerValue, computerUsableAce = self.computer_hand.countHand()

            # Handle bust or blackjack
            if computerValue >= 21:
                if computerValue > 21:
                    print("Computer busts!")
                    self.setComputerPlayerWin(2)  # Computer loses
                    self.setComputerPlayerTurnDone(True)
                    self.dealer_turn()
                else:
                    print("Computer has blackjack!")
                    self.setComputerPlayerTurnDone(True)
                    self.dealer_turn()

            # Determine action based on algorithm
            action = self.computer_algorithm(computerValue)

            if action == 1:
                print("Computer hits.")
                self.computer_hand.draw(self.deck)
            elif action == 0:
                print("Computer stands.")
                self.setComputerPlayerTurnDone(True)
                self.dealer_turn()
            elif action == 2:
                print("Computer doubles down.")
                self.computer_hand.draw(self.deck)
                self.setComputerPlayerTurnDone(True)
                self.dealer_turn()
                

        
    def computer_algorithm(self, computerValue):
        if self.algorithm == 1:  # Easy: Random actions
            return random.choice(["hit", "stand", "double down"])
        elif self.algorithm == 2:  # Medium: Q-Learning (placeholder)
            computerValue, usableAce = self.computer_hand.countHand()

            dealerCard = self.dealer_hand.cards[0].getValue()

            if dealerCard > 10:
                dealerCard = 10

            if dealerCard == 1:
                dealerCard = 11

            action = self.chooseActionNoCardCount(computerValue, dealerCard, usableAce)

            return action
        elif self.algorithm == 3:  # Hard: Q-Learning with card counting
            numBustCards = self.deck.getNumBustCards(computerValue)
            totalCards = sum(self.deck.totalCardsInDeck)

            computerValue, usableAce = self.computer_hand.countHand()

            dealerCard = self.dealer_hand.cards[0].getValue()

            if dealerCard > 10:
                dealerCard = 10

            if dealerCard == 1:
                dealerCard = 11

            action = self.chooseAction(computerValue, dealerCard, usableAce, numBustCards, totalCards)

            return action

    def dealer_turn(self):
        self.dealer_hand.draw(self.deck)
        """Simulate dealer's turn."""
        dealerValue, dealerUsableAce = self.dealer_hand.countHand()
        
        while dealerValue < 17:
            self.dealer_hand.draw(self.deck)
            dealerValue, dealerUsableAce = self.dealer_hand.countHand()
            
        self.calculate_winner()

    # 1 = win, 2 = loss, 0 = undecided, 3 = tie
    def calculate_winner(self):
        playerValue = self.human_hand.countHand()
        computerValue = self.computer_hand.countHand()
        dealerValue = self.dealer_hand.countHand()
        playerValue = playerValue[0]
        computerValue = computerValue[0]
        dealerValue = dealerValue[0]
        
        # Player goes bust
        if playerValue > 21:
            self.setHumanPlayerWin(2)
        else:
            #Player didn't bust, check dealer values
            if dealerValue > 21:
                self.setHumanPlayerWin(1)
            elif dealerValue < playerValue:
                self.setHumanPlayerWin(1)
            elif dealerValue > playerValue:
                self.setHumanPlayerWin(2)
            else:
                self.setHumanPlayerWin(3)

                # Player goes bust
            if computerValue > 21:
                self.setComputerPlayerWin(2)
            else:
                # Player didn't bust, check dealer values
                if dealerValue > 21:
                    self.setComputerPlayerWin(1)
                elif dealerValue < computerValue:
                    self.setComputerPlayerWin(1)
                elif dealerValue > computerValue:
                    self.setComputerPlayerWin(2)
                else:
                    self.setComputerPlayerWin(3)

        if self.humanPlayerWins == 2 and self.computerPlayerWins == 2:
            print("Dealer Wins")
            # if both lose, dealer wins return 0
            return 0
        else:
            if self.humanPlayerWins == 1 and self.computerPlayerWins == 1:
                # if both win return 1
                return 1
            elif self.humanPlayerWins == 1 and self.computerPlayerWins != 1:
                # if human wins and computer loses return 2
                return 2
            elif self.humanPlayerWins != 1 and self.computerPlayerWins == 1:
                # human loses computer wins return 3
                return 3
            elif self.humanPlayerWins == 1:
                return 4
            else:
                return 3

            print("Player wins value: " + str(self.humanPlayerWins))
            print("Comptuer wins value: " + str(self.computerPlayerWins))
        
        """
        if self.dealer_hand.countHand() > 21:
            if self.human_hand.countHand() <= 21:
                self.setHumanPlayerWin(1)
            else:
                self.setHumanPlayerWin(2)
            if self.computer_hand.countHand() <= 21:
                self.computerPlayerWins(1)
            else:
                self.setHumanPlayerWin(2)
        else:
            if self.dealer_hand.countHand() > self.human_hand.countHand()
                self.setHumanPlayerWin(1)
            else:
                self.setHumanPlayerWin(2)
            
            if self.dealer_hand.countHand() > self.computer_hand.countHand():
                self.setComputerPlayerWin(1)
            else:
                self.setComputerPlayerWin(2)
                
        
            
        
        
        
        
        
        
        humanValue, _ = self.human_hand.countHand()
        computerValue, _ = self.computer_hand.countHand()
        dealerValue, _ = self.dealer_hand.countHand()    
        
        if self.humanPlayerWins != 2:
            if dealerValue < humanValue:
                self.humanPlayerWins = 1
            else:
                self.humanPlayerWins = 2
                
        if self.computerPlayerWins != 2:
            if dealerValue < computerValue:
                self.computerPlayerWins = 1
            else:
                self.computerPlayerWins = 2
                
        if self.humanPlayerWins == 2 and self.computerPlayerWins == 2:
            print("Dealer Wins")
            #if both lose, dealer wins return 0
            return 0
        
        else:
            if self.humanPlayerWins == 1 and self.computerPlayerWins == 1:
                #if both win return 1
                return 1
            elif self.humanPlayerWins == 1 and self.computerPlayerWins != 1:
                #if human wins and computer loses return 2
                return 2
            elif self.humanPlayerWins != 1 and self.computerPlayerWins == 1:
                #human loses computer wins return 3
                return 3
            
            print("Player wins value: " + str(self.humanPlayerWins))
            print("Comptuer wins value: " + str(self.computerPlayerWins))
    """
            
        
            
    def getHumanPlayerWin(self):
        return self.humanPlayerWins

    def getComputerPlayerWin(self):
        return self.computerPlayerWins

    def getHumanPlayerTurn(self):
        return self.humanPlayerTurnDone

    def getComputerPlayerTurn(self):
        return self.computerPlayerTurnDone    
        
    def setHumanPlayerWin(self, statusCode):
        self.humanPlayerWins = statusCode
        
    def setComputerPlayerWin(self, statusCode):
        self.computerPlayerWins = statusCode
        
    def setHumanPlayerTurnDone(self, boolStatus):
        self.humanPlayerTurnDone = boolStatus
        
    def setComputerPlayerTurnDone(self, boolStatus):
        self.computerPlayerTurnDone = boolStatus