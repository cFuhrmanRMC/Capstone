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
    
    DEBUG = False
    DEBUG2 = False
    
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
    """
    ACTION will always be stay????
     - Unless player busts, in that case hit action is stored
    """
    def train(self, numGames: int):
        
        print("Training")
        
        progress = round(numGames/100)
            
        numPlayed = 0
            
        # create a deck
        deck = Deck(6)
        deck.shuffle()
            
        usableAceCounter = 0
            
        while numPlayed < numGames:
            
            # Calculate and print the progress
            if  numPlayed % progress == 0:
                print("% " + str(round(numPlayed/numGames * 100)))
                
            
                
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
                
            
            dealerCard = dealer.hand[0].getValue()
           
                
            if dealerCard > 10:
                dealerCard = 10
            
            ##TESTCODE
            if dealerCard == 1:
                dealerCard = 11
           
        
            continueGame = True
          
            action = 2
           
            tempReward =0
            while continueGame == True and action != 0:
                
                
                playerValue, usableAce = player.countHand() 
                if usableAce == 1:
                    usableAceCounter += 1
          
                action = self.chooseAction(playerValue, dealerCard, usableAce)
                    
                #if hit, draw from the deck
                if action == 1:
                    player.draw(deck)
                    
                
                newPlayerValue, newUsableAce = player.countHand()
                    
                    
                if newPlayerValue > 21:
                    continueGame = False
                    tempReward = 0
                elif newPlayerValue == 21:
                    continueGame = False
                    tempReward = 1
                    
                if tempReward != 0:
                    self.updateQTable(playerValue, dealerCard, usableAce, action, tempReward, newPlayerValue, newUsableAce)
                                  
                    
                
                    
                
                
                
                    
                    
                    
                """
                    ####
                    hitCounter +=1
                    ####
                    player.draw(deck)
                    newPlayerValue, newUsableAce = player.countHand()
                        
                    # Player busts or hits 21, game is over
                    if newPlayerValue > 21:
                        continueGame = False
                        
                        ######TEST CODE
                        tempReward = -1
                        ######TEST CODE
                        
                        
                    elif newPlayerValue == 21:
                        standCounter += 1
                        continueGame = False
                        
                        ######TEST CODE
                        tempReward = 1
                        ######TESTCODE
                        
                    
                # player Stands, game is over         
                else:
                    continueGame = False
                    
                    #####TEST CODE
                    if playerValue == 21:
                        tempReward = 1
                    #####TESTCODE
                    
                    newPlayerValue, newUsableAce = player.countHand()
            
                
             
            
            #update for black jack or bust
                if tempReward != 0:
                    self.updateQTable(playerValue, dealerCard, usableAce, action, tempReward, newPlayerValue, newUsableAce)
              
                                
                                
            """
                
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
                if dealerValue > 21 or newPlayerValue > dealerValue:
                    reward = 1
                
                elif dealerValue > newPlayerValue:
                    reward = -1
                        
                else: 
                    reward = 0
                    
                
            if QLearn.DEBUG:
                print("Game Number: %d" % numPlayed)
                print("Dealer Card: %d" % dealerCard)
                print("Dealer Value: ", dealerValue)
                print("Player Value after action: ", newPlayerValue)
                print("Players cards: ", player)
                print("reward: %d" % reward)
                print("usable ace: %d" % usableAce)
                print("action:  %d" % action)
                print("Q Value for current action: %.3f" % self.QTable[playerValue, dealerCard, self.rewardIndex(action, usableAce)] )    
                
                
                
                
                    
            if QLearn.DEBUG2:
                if usableAce == 1:
                    
                    print("Game Number: %d" % numPlayed)
                    print("Dealer Card: %d" % dealerCard)
                    print("Dealer Value: ", dealerValue)
                    print("Player Value after action: ", newPlayerValue)
                    print("Players cards: ", player)
                    print("reward: %d" % reward)
                    print("usable ace: %d" % usableAce)
                    print("action:  %d" % action)
                    print("Q Value for current action: %.3f" % self.QTable[playerValue, dealerCard, self.rewardIndex(action, usableAce)] )                         
                        
                        
                
            numPlayed += 1
            self.updateQTable(playerValue, dealerCard, usableAce, action, reward, newPlayerValue, newUsableAce)
            
            
                
            if QLearn.DEBUG2:
                if usableAce == 1:
                    print("Q value after action: %.3f" % self.QTable[playerValue, dealerCard, self.rewardIndex(action, usableAce)] ) 
                    print()
                    
                        
            
            
            
            if QLearn.DEBUG:
                print("Q value after action: %.3f" % self.QTable[playerValue, dealerCard, self.rewardIndex(action, usableAce)] )
               # print("standCounter: %d"% standCounter)
                #print("hitCounter: %d"% hitCounter)
                print()

          
            
        print("Complete")
        print(usableAceCounter)
        
    # Agent plays the game
    def playGame(self, numGames):
        
            
        numPlayed = 0

        numWins = 0
        numLosses = 0
        numDraws = 0
            
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
                
            if dealerCard == 1:
                dealerCard = 11
                    
            continueGame = True
            while continueGame == True:
                playerValue, usableAce = player.countHand()
                    
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
                ##########playerValue, usableAce = player.countHand()
                        
            # game is over        
            if newPlayerValue > 21:
                numLosses += 1
                
                ###
                reward = -1
                ###
                    
            # dealer's turn
            else:
                    
                dealerValue, dealerUsableAce = dealer.countHand()
                    
                while dealerValue < 17:
                    dealer.draw(deck)
                    dealerValue, dealerUsableAce = dealer.countHand()
                        
                        
                # determine out comes
                if dealerValue > 21:
                    numWins += 1
                    
                    ###
                    reward = 1
                    ###
                
                
                
                elif dealerValue > newPlayerValue:
                    numLosses += 1
                    
                    ####
                    reward = -1
                    ###
                        
                elif newPlayerValue > dealerValue:
                    numWins += 1
                    
                    ###
                    reward = 1
                    ###
                        
                else: 
                    numDraws += 1
                    
                    ###
                    reward = 0
                    ###
                    
                    
                    
            numPlayed += 1
            
        print("number of wins: %d" % numWins)
        print("number of losses: %d" % numLosses)
        print("number of draws: %d" % numDraws)
        
        winRate = numWins / (numWins + numLosses) * 100
        print("win rate: %.2f" % winRate)
        
       
            
            
                
                    
                    
                            
                        
                        
            
        
        
        
            
        
        
        
def main():
    agent = QLearn(.1, .4, .1)
    agent.train(2000000)
    
    agent.printTable("test.txt")
    
    agent.playGame(10000)

main()
        
        
        
        
        
