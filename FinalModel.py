# File Name: Black Jack Model
# Author: Torryn Carey-Jarrell
#
# Model game for black jack

import random

import numpy as np

testingBool = False

# Card class that creates objects for each individual card
class Card:

    # Initializes suit and value for each card
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

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

    # Getter for suit
    # @return suit of the card
    def getSuit(self):
        return self.suit

    # Getter for the value
    # @return value of the card
    def getValue(self):
        return self.value


# Deck class that takes a number of decks and creates one deck that
# incorporates all 52 cards from each requested deck. Each deck is
# composed of cards (ace to king) of each of the four suits (hearts,
# diamonds, clubs and spades in that numeric order) also provides
# the functionality for shuffling the deck and giving cards from the
# deck, popping them off the stack
class Deck:
               # A  1  2  3  4  5  6  7  8  9  J  Q  K
    cardsUsed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    totalCardsInDeck = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Initializes all 52 cards in the deck with one value for each card of each suit
    # @param numDecks - the number of decks to be made and stored in the cards list
    def __init__(self, numDecks):
        # 1 is hearts, 2 is diamonds, 3 is clubs, 4 is spades
        suits = [1, 2, 3, 4]
        value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        self.cards = []
        numMade = 0

        # Loop to make the number of decks in the numDecks parameter
        while numMade < numDecks:
            # For all four suits in the suit list
            for suit in suits:
                # For all 13 value in the value list
                for num in value:
                    # Create and append a card for a suit and value
                    self.cards.append(Card(suit, num))
            numMade += 1

            # Increments the total cards in the deck for card counting
            self.incrementTotalCardsInDeck()

    # Getter for the cards in a deck
    # @return cards in the deck
    def getCards(self):
        return self.cards

    # Getter for the size of the deck
    # @return length of the number of cards
    def getSize(self):
        return len(self.cards)

    # Updates the cards in the deck by adding new decks
    def addDecks(self, numDecks):
        deck = Deck(numDecks)
        for card in deck.cards:
            self.cards.append(card)

    # repr that returns a string detailing the number of cards in the deck
    # @return a string saying "Deck containing x cards."
    def __repr__(self):
        return "Deck containing " + str(len(self.cards)) + " cards."

    # Function for shuffling the deck to randomize cards in it
    def shuffle(self):
        random.shuffle(self.cards)

    # Gives a specific card to the player from the deck by popping it off the
    # deck object
    # @return the card popped off the deck
    def giveCard(self):
        
        # Pops the card off the deck
        card = self.cards.pop(0)
        
        # Increments the card drawn in the card counting list
        self.countCards(card)
        
        return card

    # Increments the list of cards in the deck to add four to every value
    # and is used in the creation of new decks to ensure proper number of cards
    # are added to that list
    def incrementTotalCardsInDeck(self):
        for i in range(len(self.totalCardsInDeck)):
            self.totalCardsInDeck[i] += 4

    # After a card is popped off the deck this function is called to
    # increment that cards index in the list
    # As list is a zero count each value must be incremented at a -1 index
    def countCards(self, cardAdded):
        self.cardsUsed[cardAdded.getValue() - 1] += 1

    # Prints statistics about the deck such as total cards, cards found/used,
    # cards still left in the deck and the specific cards found/used
    def printDeck(self):
        print("Total cards ever in Deck: " + str(sum(self.totalCardsInDeck)))
        print("Total cards found: " + str(sum(self.cardsUsed)))
        print("Total cards left: " + str(len(self.cards)))
        print("Ace - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 - J - Q - K")
        print(self.cardsUsed)

    # Gets the number of cards in the deck that can make players go bust with
    # the current value of cards in their hand
    # @return number of cards in the deck that would make the player go bust
    def getNumBustCards(self, playerTotal):
        
        # The bust value is 21 so subtracting player's value from 21 gives you
        # the value of a card that would make them go bust
        bustNumber = 21 - playerTotal

        # A bust value under 10 means there are zero cards in the deck that would
        # make the player go bust, so return zero
        if bustNumber > 10:
            return 0
        else:

            numBustCards = 0
            # One over bust number is when the player would go bust
            x = bustNumber + 1
            
            # Loops through all value of cards in the deck at the bust card index and above
            while x < len(self.totalCardsInDeck):
                #print("X Value: " + str(x))
                #print("Card " + str(x) + " has " + str(self.totalCardsInDeck[x]) + " total")
                #print("and has been used " + str(self.cardsUsed[x]) + " times")
                
                # Total cards in deck versus total cards used is the number of cards at that index
                # that could make the player go bust
                numBustCards += self.totalCardsInDeck[x] - self.cardsUsed[x]
                #print(self.totalCardsInDeck[x] - self.cardsUsed[x])
                x += 1

        #print(numBustCards, sum(self.totalCardsInDeck))
        return numBustCards

    # Resets the class variables when a new deck is created
    def resetClassVariables(self):
        Deck.cardsUsed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Deck.totalCardsInDeck = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Class that stores the cards for each player and contains all methods for accessing
# and manipulating those cards
class Hand:
    
    # Initializes the players hand to an empty list
    def __init__(self):
        self.cards = []

    # repr to print the cards in a players hand
    def __repr__(self):
        return repr(self.cards)

    # This function draws a card from the deck and adds it to the players hand
    def draw(self, deck):
        self.cards.append(deck.giveCard())

    # This function was used for testing to add a specific card to the players hand
    # @param suit - value of 1, 2, 3 or 4 denoting suit
    # @param value - value of 1-13 used to denote the value of a specific card
    def addCard(self, value, suit):
        self.cards.append(Card(suit, value))

    # This function counts the cards in a players hand and returns the value of their
    # hand and whether they have a usable ace or not
    # @return usableAce True or False if usable ace could or could not be used
    # @return value of the hand provided
    def countHand(self):
        totalValue = 0
        numAces = 0

        if testingBool == True:
            print("START OF COUNT")
            print("HAND PROVIDED HAS " + repr(self.cards))

        # Summarizes the total value of cards in the hand, checking for aces
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

        # If all aces that were found can be used returns usable ace as true,
        # otherwise usable ace is false
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

# Blackjack game that holds all instance variables needed to play the blackjack game
# and the methods used to play it
class BlackjackGame:
    # Define global action buttons
    ACTION_BUTTONS = {
        "hit": 1,
        "stand": 0,
        "double down": 2
    }

    # Initializer for the Blackjack Game object
    def __init__(self, num_decks, starting_balance, algoNum):

        # Initializes the deck and shuffles it
        self.deck = Deck(num_decks)
        self.deck.shuffle()

        # Initializes the hands for all agents
        self.human_hand = Hand()
        self.computer_hand = Hand()
        self.dealer_hand = Hand()

        # Initialises the balance
        self.balance = starting_balance
        self.bet = 0

        # Initializes tha algorithm chosen by the player
        self.algorithm = algoNum

        # Initializes wins and turn variables for players
        self.humanPlayerWins = 0  # 1 = win, 2 = loss, 0 = undecided
        self.computerPlayerWins = 0
        self.humanPlayerTurnDone = False
        self.computerPlayerTurnDone = False

        # Loads QTable to be used in second and third algorithm
        self.QTable = np.load("blackJackQTable.npy")

    # Getter for the deck
    # @return deck
    def get_deck(self):
        return self.deck

    # Getter for the human players hand
    # @return human players hand
    def get_playerHand(self):
        return self.human_hand

    # Getter for the computer players hand
    # @return computer players hand
    def get_computerHand(self):
        return self.computer_hand

    # Getter for the dealer hand
    # @return dealers hand
    def get_dealerHand(self):
        return self.dealer_hand
    
    # Getter for the human player win value
    # @return human player win value
    def getHumanPlayerWin(self):
        return self.humanPlayerWins

    # Getter for the computer player win value
    # @return computer player win value
    def getComputerPlayerWin(self):
        return self.computerPlayerWins

    # Getter for the human player turn
    # @return Boolean for human player turn
    def getHumanPlayerTurn(self):
        return self.humanPlayerTurnDone

    # Getter for the computer player turn
    # @return Boolean for the computer player turn
    def getComputerPlayerTurn(self):
        return self.computerPlayerTurnDone

    # Setter for the human player win
    # @param statusCode - value of human player win
    def setHumanPlayerWin(self, statusCode):
        self.humanPlayerWins = statusCode

    # Setter for the computer player win
    # @param statusCode - value of the computer player win
    def setComputerPlayerWin(self, statusCode):
        self.computerPlayerWins = statusCode

    # Setter for the human player turn done
    # @param boolStatus - status code for human player turn done
    def setHumanPlayerTurnDone(self, boolStatus):
        self.humanPlayerTurnDone = boolStatus

    # Setter for the computer player turn done
    # @param boolStatus - status code for computer player turn done
    def setComputerPlayerTurnDone(self, boolStatus):
        self.computerPlayerTurnDone = boolStatus

    # Accesses the proper index in the QTable based on action and usable ace
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
    # @return action - 0 denotes a stand, 1 denotes hit and 2 denotes double down
    def chooseAction(self, playerValue: int, dealerCard: int, usableAce: int, numBustCards: int,
                     totalCards: int) -> int:
        hitValue = self.QTable[playerValue, dealerCard, (self.rewardIndex(1, usableAce))]
        standValue = self.QTable[playerValue, dealerCard, (self.rewardIndex(0, usableAce))]

        percentBustCards = numBustCards / totalCards

        # This if statement block functions as card counting for the QLearn algorithm
        # it changes the hit and stand values depending on how great a chance there is
        # for the player to go bust
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

        # Most values where the player should double down have a 0.95 and above
        # hit value, especially after card counting is executed
        if hitValue > standValue:
            if hitValue > 0.95:
                return 2
            else:
                return 1
        else:
            return 0

    # Chooses action based on Q Values from npy file without card counting
    # @return action - 0 denotes a stand, 1 denotes hit and 2 denotes double down
    def chooseActionNoCardCount(self, playerValue: int, dealerCard: int, usableAce: int) -> int:

        # Gets the hit and stand values from the QTable
        hitValue = self.QTable[playerValue, dealerCard, (self.rewardIndex(1, usableAce))]
        standValue = self.QTable[playerValue, dealerCard, (self.rewardIndex(0, usableAce))]

        if hitValue > standValue:
            # Most values where the player should double down have a 0.95 and above
            # hit value
            if hitValue > 0.95:
                return 2
            else:
                return 1
        else:
            return 0

    # Every game is initialized by emptying the players hands, resetting the
    # deck if it has too few cards, and providing all agents with the appropriate
    # number of cards
    def start_game(self):
        """Initialize a new game and deal initial cards."""
        print("\n--- Starting a New Game ---")
        # Add cards if deck runs low
        if self.deck.getSize() <= 52:
            self.deck.resetClassVariables()
            self.deck = Deck(6)
            # deck.addDecks(6)
            self.deck.shuffle()

        # Empties agent hands for new game
        self.human_hand = Hand()
        self.computer_hand = Hand()
        self.dealer_hand = Hand()

        # Resets player losses and turns their turn completion flag back to false
        self.humanPlayerWins = 0  # 1 = win, 2 = loss, 0 = undecided
        self.computerPlayerWins = 0
        self.humanPlayerTurnDone = False
        self.computerPlayerTurnDone = False

        # Deal two cards to each player and one to the dealer
        self.human_hand.draw(self.deck)
        self.human_hand.draw(self.deck)
        self.computer_hand.draw(self.deck)
        self.computer_hand.draw(self.deck)
        self.dealer_hand.draw(self.deck)

        print(f"Player's Hand: {self.human_hand}")
        print(f"Dealer's Shown Card: {self.dealer_hand.cards[0]}")

    # This function takes an action from the controller and uses it to update the
    # players hand to reflect the result of that action
    # @param action - a value of 0 for stand, 1 for hit or 2 for double down
    def humanPlayerInput(self, action):

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

    # This function executes the computer players turn according to the
    # algorithm number selected by the player
    def computerPlayerTurn(self):

        # Loops until the player finishes their turn
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

    # This function calls the appropriate actions depending on the difficulty selected
    # when the player selects one of the three options in the controller
    # Easy is denoted by 1 and is a random selection between hit, stand or double down
    # Medium is denoted by 2 and uses the algorithm developed by QLearn to decide
    # whether the computer player hits, stands or doubles down
    # Hard is denoted by a 3 and uses the same algorithm as medium but with card
    # counting implemented to give the computer an extra leg up
    def computer_algorithm(self, computerValue):
        if self.algorithm == 1:  # Easy: Random actions
            return random.choice(["hit", "stand", "double down"])
        elif self.algorithm == 2:  # Medium: Q-Learning
            computerValue, usableAce = self.computer_hand.countHand()

            dealerCard = self.dealer_hand.cards[0].getValue()

            # When turning the cards from chars to integers it was easier to denote
            # ace as a 1 and Jack, Queen and King as 11, 12 and 13 respectively
            # QLearn however, functions better with ace as an 11 and Jack, Queen
            # and King as 10 which i what this ensures
            if dealerCard > 10:
                dealerCard = 10

            if dealerCard == 1:
                dealerCard = 11

            # Calls the functions to determine the computers actions
            action = self.chooseActionNoCardCount(computerValue, dealerCard, usableAce)

            return action

        elif self.algorithm == 3:  # Hard: Q-Learning with card counting

            # Hard uses card counting so the values must be gathered first
            numBustCards = self.deck.getNumBustCards(computerValue)
            totalCards = sum(self.deck.totalCardsInDeck)

            computerValue, usableAce = self.computer_hand.countHand()

            dealerCard = self.dealer_hand.cards[0].getValue()

            # When turning the cards from chars to integers it was easier to denote
            # ace as a 1 and Jack, Queen and King as 11, 12 and 13 respectively
            # QLearn however, functions better with ace as an 11 and Jack, Queen
            # and King as 10 which i what this ensures
            if dealerCard > 10:
                dealerCard = 10

            if dealerCard == 1:
                dealerCard = 11

            # Calls the
            action = self.chooseAction(computerValue, dealerCard, usableAce, numBustCards, totalCards)

            return action

    # This function gets the dealers whole hand and plays their turn hitting
    # until they reach a value of 17 or higher
    def dealer_turn(self):
        self.dealer_hand.draw(self.deck)
        dealerValue, dealerUsableAce = self.dealer_hand.countHand()

        while dealerValue < 17:
            self.dealer_hand.draw(self.deck)
            dealerValue, dealerUsableAce = self.dealer_hand.countHand()

        # Dealer is the last agent to go, calls calculate win after turn completes
        self.calculate_winner()

    # This function provides the ability to calculate who won the game between the
    # house, human player and computer player
    # 0 is undecided 1 is a win, 2 is a loss, 3 is a tie
    # @return 0 if house won, 1 if human player and computer player won
    #   2 if human player wins and computer loses, 3 if human and/or
    #   computer loses, and 4 if just the player wins
    def calculate_winner(self):

        # Gets the value and usable ace of all parties
        playerValue = self.human_hand.countHand()
        computerValue = self.computer_hand.countHand()
        dealerValue = self.dealer_hand.countHand()

        # Gets just the value of each party
        playerValue = playerValue[0]
        computerValue = computerValue[0]
        dealerValue = dealerValue[0]

        # Player went bust so they lose
        if playerValue > 21:
            self.setHumanPlayerWin(2)
        else:
            # Player didn't bust, check dealer values
            if dealerValue > 21:
                # Dealer went bust so player won
                self.setHumanPlayerWin(1)
            elif dealerValue < playerValue:
                # Dealer had a lower number than player so player wins
                self.setHumanPlayerWin(1)
            elif dealerValue > playerValue:
                # Dealer had higher number than player so dealer won
                self.setHumanPlayerWin(2)
            else:
                # Both parties had same number so they tied
                self.setHumanPlayerWin(3)

            # Computer went bust so they lose
            if computerValue > 21:
                self.setComputerPlayerWin(2)
            else:
                # Computer didn't bust, check dealer values
                if dealerValue > 21:
                    # Dealer went bust so computer won
                    self.setComputerPlayerWin(1)
                elif dealerValue < computerValue:
                    # Dealer had lower number than computer so computer won
                    self.setComputerPlayerWin(1)
                elif dealerValue > computerValue:
                    # Dealer had higher value than computer so computer won
                    self.setComputerPlayerWin(2)
                else:
                    # Both computer and dealer had same value so they tied
                    self.setComputerPlayerWin(3)

        # Returns correct value to be used by controller to display win/loss message
        if self.humanPlayerWins == 2 and self.computerPlayerWins == 2:
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
                # Human player won but computer didn't, return 4
                return 4
            else:
                # Human lost but computer won, return same loss value of 3
                return 3

            print("Player wins value: " + str(self.humanPlayerWins))
            print("Comptuer wins value: " + str(self.computerPlayerWins))
