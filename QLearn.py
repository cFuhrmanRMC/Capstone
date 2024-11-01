# QLearn.py
# authors: Cole Fuhrman, Jordan Brown
# Capstone Project
#
#
# This file contains the QLearn class


import numpy as np
import random
from Cards import Card, Deck, Hand

# QLearn contains methods that trains an agent to play the card game blackjack
class QLearn:
    
    # Construct a Qlearning object
    """
     alpha: Learning rate -> how quickly the agent "learns"
       - 1 rapidly updates, Q table filled with large values
       - 0 does not update, Q table values will not change
     
     gamma: Discount factor -> value of future reward 
       - 1 means future reward is just as valuable as current reward
       - 0 only immediate rewards are valued
       
     epsilon: epsilon-greedy -> how often random actions are taken
       - 1 every action taken is random
       - 0 no actions are taken at random
    """
    def __init__(self, alpha: float, gamma: float, epsilon: float):
        
        # all values must be between 0 and 1
        assert alpha >= 0.0 or alpha <= 1.0, "alpha value must be between 0.0 and 1.0"
        assert gamma >= 0.0 or gamma <= 1.0, "gamma value must be between 0.0 and 1.0"
        assert epsilon >= 0.0 or epsilon <= 1.0, "epsilon value must be between 0.0 and 1.0"
        
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        
        # intialize the Q table
        self.QTable = np.zeros((33, 12, 4))
        
    # prints the q table to a text file    
    def printTable(self, fileName: str):
        file = open(fileName, "w")
        for i in range(self.QTable.shape[0]):
            file.write("%d \n" %i)
            np.savetxt(file, self.QTable[i], fmt="%10.5f")
            file.write('\n')
            
        file.close()
        
    """
      Actions:
        - hit = 1
        - stay = 0
    """
    # Choose the correct index to store the reward value 
    #
    
    def rewardIndex(self, action: int, usableAce: int)->int:
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
    
    
    # Agent chooses an action
    #
    
    def chooseAction(self, playerValue: int, dealerCard: int, usableAce: int)->int:
        # Ensure usableAce is boolean
        assert usableAce == 0 or usableAce == 1, "usableAce must be equal to 0 or 1"
        
        # generate a random value between 0 and 1, if the value is less than epsilon choose a random action (return 0 or 1)
        if random.random() < self.epsilon:
            return random.randint(0, 1)
        
        else:
            #Check to see if the reward value is higher for hitting or standing and choose the action that has the highest reward
            if self.QTable[playerValue, dealerCard, (self.rewardIndex(1, usableAce))] > self.QTable[playerValue, dealerCard, (self.rewardIndex(0, usableAce))]:
                return 1
            else: 
                return 0
                
                
    # Update the QTable
    #
    """
      Reward could be an int or a float depending on alpha rate
    """
    def updateQTable(self, playerValue: int, dealerCard: int, usableAce: int, action: int, reward, newPlayerValue: int, newUsableAce: int):
        # Ensure usableAce is boolean
        assert usableAce == 0 or usableAce == 1, "usableAce must be equal to 0 or 1"
        
        # Ensure action is boolean
        assert action == 0 or action == 1, "action must be equal to 0 or 1"
        
        # get the current reward for the state from the Q table
        currentValue = self.QTable[playerValue, dealerCard, self.rewardIndex(action, usableAce)]
        
        # determine the maximum possible reward for the new state
        futureHitValue = self.QTable[newPlayerValue, dealerCard, self.rewardIndex(1, newUsableAce)]
        futureStayValue = self.QTable[newPlayerValue, dealerCard, self.rewardIndex(0, newUsableAce)]
        
        if futureHitValue > futureStayValue:
            futureValue = futureHitValue
        else: 
            futureValue = futureStayValue
            
        """
          temporal difference calculates reward value factoring in learning rate and discount factor
        """
        temporalDifference = currentValue + self.alpha * (reward + self.gamma * futureValue - currentValue)
        
        # Update the reward value in the Qtable 
        self.QTable[playerValue, dealerCard, self.rewardIndex(action, usableAce)] = temporalDifference
        
    # train the agent
    #
    def train(self, numGames: int):
        
        print("Training")
            
        numPlayed = 0
            
        # create a deck
        deck = Deck(6)
        deck.shuffle()
            
        while numPlayed < numGames:
                
            # Add cards if deck runs low
            if deck.getSize() <= 52:
                deck.addDecks(5)
                deck.shuffle()
                    
                
            #intialize hands
            dealer = Hand()
            player = Hand()
                
            player.draw(deck)
            dealer.draw(deck)
            player.draw(deck)
            dealer.draw(deck)
                
            dealerCard= dealer.hand[0].getValue()
            playerValue, usableAce = player.countHand()
                
            if dealerCard > 10:
                dealerCard = 10
                    
            continueGame = True
            while continueGame == True:
                    
                action = self.chooseAction(playerValue, dealerCard, usableAce)
                    
                #if hit, draw from the deck
                if action == 1:
                    player.draw(deck)
                    newPlayerValue, newUsableAce = player.countHand()
                        
                    # Player busts or hits 21, game is over
                    if newPlayerValue >= 21:
                        continueGame = False
                    
                # player Stands, game is over         
                else:
                    continueGame = False
                    
                newPlayerValue, newUsableAce = player.countHand()
                        
            # game is over        
            if newPlayerValue > 21:
                reward = -1
                    
            # dealer's turn
            else:
                    
                dealerValue, dealerUsableAce = dealer.countHand()
                    
                while dealerValue < 17:
                    dealer.draw(deck)
                    dealerValue, dealerUsableAce = dealer.countHand()
                        
                        
                # determine out comes
                if dealerValue > newPlayerValue:
                    reward = -1
                        
                elif newPlayerValue > dealerValue:
                    reward = 1
                        
                else: 
                    reward = 0
                        
            numPlayed += 1
            self.updateQTable(playerValue, dealerCard, usableAce, action, reward, newPlayerValue, newUsableAce)
            
        print("Complete")
                
                    
                    
                            
                        
                        
            
        
        
        
            
        
        
        
def main():
    agent = QLearn(.1, .9, .1)
    agent.train(5000000)
    
    agent.printTable("test.txt")

main()
        
        
        
        
        
