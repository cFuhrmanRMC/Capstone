#
#
#
#
#
#


import numpy as np
import random
from Cards import Card, Deck

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
    
    def chooseAction(self, playerSum: int, dealerCard: int, usableAce: int)->int:
        #Ensure usableAce is boolean
        assert usableAce == 0 or usableAce == 1, "usableAce must be equal to 0 or 1"
        
        # generate a random value between 0 and 1, if the value is less than epsilon choose a random action (return 0 or 1)
        if random.random() < self.epsilon:
            return random.randint(0, 1)
        
        else:
            #Check to see if the reward value is higher for hitting or standing and choose the action that has the highest reward
            if self.QTable[playerSum, dealerCard, (self.rewardIndex(1, usableAce))] > self.QTable[playerSum, dealerCard, (self.rewardIndex(0, usableAce))]:
                return 1
            else: 
                return 0
                
                
            
        
        
        
        
        