# QLEARN TESTING

# authors: 
# blackjackQLearn.py
#
#
#
#

# import numpy and blackjameGame modules
import numpy as np
from blackjackGame import blackjackGame

 
class QLearn:

    # Constructs a QLearn Object 
    # @ensure: alpha, gamma, and epsilon values are between 0 and 1
    def __init__(self, alpha: float, gamma: float, epsilon: float):
        
        assert alpha > 0.0 or alpha < 1.0, "alpha value must be between 0.0 and 1.0"
        assert gamma > 0.0 or gamma < 1.0, "gamma value must be between 0.0 and 1.0"
        assert epsilon > 0.0 or epsilon < 1.0, "epsilon value must be between 0.0 and 1.0"
        
        self._alpha = alpha
        self._gamma = gamma
        self._epsilon = epsilon
        
        # intialize Q table
        
        self._QTable = np.zeros((33, 12, 4)) # Number of player sets (33), number of dealer sets (12), usable ace true/false (2), action hit or stand (2)
        
    def aceIndex(self, action, usableAce):
        value = 0
        if usableAce == 0:
            
            if action == 0:
                value = 0
            else:
                value = 1
        
        elif usableAce == 1:
            
            if action == 0:
                value = 2
            else:
                value = 3
                
        return int(value)
        
    # print the Q Table
    #
    def printQTable(self):
        for i in self._QTable:
           
            print(i)
    
            
            
    # agent chooses an action
    #
    def chooseAction(self, playerSum, dealerCard, usableAce):
        
        # generate a random value between 0 and 1, if less than epsilon value, choose random action
        if np.random.uniform(0, 1) < self._epsilon:
            return np.random.choice([0, 1])
    
        else:
          
            
            # check to see if the reward value is greater for hitting (0) or staying (1), make the action that returns the highest reward
            if self._QTable[playerSum, dealerCard, (self.aceIndex(0, usableAce))] > self._QTable[playerSum, dealerCard, (self.aceIndex(1, usableAce))]: 
                return 0  
            else:
                return 1
            
    # 
    #
    # update the QTable
    #
    def update(self, playerSum, dealerCard, usableAce, action, reward, newPlayerSum, newDealerCard, newUsableAce):
                    
   
        #Get the current value from the Q table
        currentValue = self._QTable[playerSum, dealerCard, (self.aceIndex(action, usableAce))]
       
   
            
   
            
        # Update the Q table based of the value that has the largest reward
        if self._QTable[newPlayerSum, newDealerCard, self.aceIndex(0, usableAce)] >= self._QTable[newPlayerSum, newDealerCard, self.aceIndex(1, usableAce)]:
            futureValue = self._QTable[newPlayerSum, newDealerCard, self.aceIndex(0, usableAce)]
            
        else: 
            futureValue = self._QTable[newPlayerSum, newDealerCard, self.aceIndex(1, usableAce)]
            
        

        ########
        ##
        ########
        #print(currentValue + self._alpha * (reward + self._gamma * futureValue - currentValue))
        self._QTable[playerSum, dealerCard, (self.aceIndex(action, usableAce))] = currentValue + self._alpha * (reward + self._gamma * futureValue - currentValue)
    #
    #
    #
    #
    #
    
    # Check to see if the hand has a usable ace
    # returns an integer for index access, int is 1 or 0, representing true or false
    def hasUsableAce(self, hand: list)->int:
        value = 0
        ace = 0 
    
        # Loop through the hand and calculate the value of the cards
        for card in hand:
            # Check to see if card is jack, queen, or king
            if card[0] in ['J', 'Q', 'K']:
                value += 10
            # Check to see if the card is an ace
            elif card[0] == 'A':
                value += 1
                ace += 1
            else:
                value += int(card[0])
                
        # return 1(true) if usable ace, false if not
        if ace >= 1 and value + 10 <= 21:
            return 1
        else:
            return 0
            
            
    # play the game for the number of episodes 
    #       
    def train(self, episodes: int):
        
        assert episodes >= 100, "Error, must train agent with a minimum of 100 episodes"
                
        progressValue = round(episodes / 100)
    
        # play a game for episode
        for episode in range(episodes):
            game = blackjackGame()
               
            # print the progree every whole percent value   
            if episode % progressValue == 0:
                progress = (episode/episodes) * 100
                print("Training progress: %.2f" % progress)
                
      
            dealerCard = game.getDealerHand()[0][0]
       
            # calculate value of the dealer's face card
            if dealerCard in ['K', 'Q', 'J']:
                dealerCard = 10
            elif dealerCard == 'A':
                dealerCard = 11
            else:
                delaerCard = dealerCard
            
            #cast dealerCard to int type
            dealerCard = int(dealerCard)
                       
            # play the game 
            status = "continue"
            action = 0
              
            while status == "continue" and action == 0:
        
                playerSum = game.handValue(game.getPlayerHand())
                usableAce = self.hasUsableAce(game.getPlayerHand())
                
                #######
                #print("Player hand: ", game.getPlayerHand())
                #playerSum = game.handValue(game.getPlayerHand())
                #print(playerSum)
                #print()
                #######
                #print("Dealer face card: ", game.getDealerHand()[0])
                #print()
                #######                
                
                    
                action = self.chooseAction(playerSum, dealerCard, usableAce)
                status = game.playerAction(action)
                
                ########## 
                #print(action)
                #print("Player hand after action: ", game.getPlayerHand())
                
                #playerSum = game.handValue(game.getPlayerHand())
                #print(playerSum)                
                #print("full dealer hand: ", game.handValue(game.getDealerHand()))
                ###########                
                    
                newPlayerSum = game.handValue(game.getPlayerHand())
                newUsableAce = self.hasUsableAce(game.getPlayerHand())
               
    
                        
                reward = 0
                    
                # determine reward if first action results in win (blackjack), or lose (bust)
                if status == "blackjack":
                    reward = 1
                elif status == "bust":
                    reward = -1
                            
                # update reward if there is a reward          
                if reward != 0:
                    self.update(playerSum, dealerCard, usableAce, action, reward, newPlayerSum, dealerCard, newUsableAce) 
                    
                    
            game.dealerAction()      
            #print("Dealer hand after action", game.handValue(game.getDealerHand()) )
                                    
                            
                        
            # Determine the final result of the game and update the reward          
            gameResult = game.gameResult()
            if gameResult == "win":
                finalReward = 1
            elif gameResult == "lose":
                finalReward = -1
            else:
                finalReward = 0
                    
            #####      
            #print("REWARD:", finalReward)
            
            #print()
            #print()
            #print()
            #####
            self.update(playerSum, dealerCard, usableAce, action, finalReward, newPlayerSum, dealerCard, newUsableAce)
                    
                    
    def agentPlaysGame(self):
        game = blackjackGame()
        
        status = "continue"
        action = 0
        
        dealerCard = game.getDealerHand()[0][0]
        

        
   
        # calculate value of the dealer's face card
        if dealerCard in ['K', 'Q', 'J']:
            dealerCard = 10
        elif dealerCard == 'A':
            dealerCard = 11
        else:
            delaerCard = dealerCard
        
        #cast dealerCard to int type
        dealerCard = int(dealerCard)          
        
        while status == "continue" and action != 1:
          
        
            playerSum = game.handValue(game.getPlayerHand())
            usableAce = self.hasUsableAce(game.getPlayerHand())
                
                    
            action = self.chooseAction(playerSum, dealerCard, usableAce)

            
            status = game.playerAction(action)
            
        game.dealerAction()
            
        return game.gameResult()
                    
    
        
                             
            
          
            
            
    
               
        
def main():
       
        
    # create "agent", Qlearn Object
    agent = QLearn(0.1, 0.9, 1)
        
        
    # train the agent
    # minimum of 100 episodes
    print("---")
    agent.train(2000000)
    print("---")
     
     
    testGames = 1000
    wins = 0
    loses = 0
    draws = 0 
    
    for i in range(testGames):
        result = agent.agentPlaysGame()
        if result == "win":
            wins += 1
        
        elif result == "lose":
            loses += 1
        
        else:
            draws += 1
            
    
    print("Wins: %d" % wins) 
    print("Loses: %d" % loses)
    print("Draws: %d" % draws)
    
  
    winRate = wins / (wins + loses) *100
    print("Win Rate: %.2f" % winRate)
    
    print()
        
    # print the QTable
   
    agent.printQTable()
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #control game
    ##########
    controlWin = 0
    controlLoss = 0
    controlDraw = 0
    
    

    for i in range(testGames):
       
        controlGame = blackjackGame()
        controlAction = 0
        controlStatus = "continue"
    
        # continue to play the game until the player stands or loses
        while controlStatus == "continue" and controlAction != 1:
            
            if controlGame.handValue(controlGame.getPlayerHand()) < 15:
                controlAction = 0
            else:
                controlAction = 1
    
    
            controlStatus = controlGame.playerAction(controlAction)
 
    
               
            
        controlResult = controlGame.gameResult()
    
        if controlResult == "win":
            controlWin += 1
            
        elif controlResult == "lose":
            controlLoss += 1
            
        else:
            controlDraw += 1
    print("Control Wins: %d" % controlWin) 
    print("Control Loses: %d" % controlLoss)
    print("Control Draws: %d" % controlDraw)
    
    print()
    controlWinRate = controlWin / (controlWin + controlLoss) *100
    print("Control Win Rate: %.2f" % controlWinRate)
            
    
    ##########
        
main()
