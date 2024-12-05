#Casino Blackjack Classes
# Alec Shalowitz, Sam Slevin

#Use timer to delay game with update idle tasks


# Import tkinter
import tkinter as tk
#from blackjack import *
import time
from blackjackmodel import *

playerTurnOver = False

# Class that vreates a Tkinter window
class CasinoWindow:
    # Class constructor
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.title("Casino")
        self.root.resizable(False, False)
        self.root.update_idletasks()
        self.player = 1
        self.windowHeight = self.root.winfo_height()
        self.windowWidth = self.root.winfo_width()        
   
    # Return the height of the tkinter window
    # @return: height of the window
    def getWindowHeight(self):
        return self.windowHeight
   
    # Return the width of the tkinter window
    # @return: width of the window
    def getWindowWidth(self):
        return self.windowWidth
   
    # Return the root of the tkinter window
    # @return: root of the window
    def getRoot(self):
        return self.root
   
    def getPlayer(self):
        return self.player
   
    def changeTurn(self):
        if(self.player == 1):
            self.player = 2
        else:
            self.player = 1
   
# Class to create a frame
class CasinoFrame:
   
    # Class frame constructor
    # @param root: the root window
    # @param bg_color: the background color of the frame
    # @param width: the width of the frame
    # @param height: the height of the frame
    # @param x_pos: the x position to place the frame at
    # @param y_pos: the y position to place the frame at
    def __init__(self, root, bg_color, width, height, x_pos, y_pos):
        self.frame = tk.Frame(root, bg=bg_color, width=width, height=height, relief="raised", bd = 5)
        self.frame.place(x=x_pos, y=y_pos)        


global buttonResult 

def getButtonResult():
    return buttonResult

# Class to create a button  
class CasinoButton:
   
   
    def buttonHit(self, root,width, height,statusBar, textBox, hand,deck, placement, computerTextBox, dealerTextBox, playerCurrency):
        global playerTurnOver
        if playerTurnOver == False:
            game.humanPlayerInput(1)
            playerHand = game.get_playerHand()
            score = playerHand.countHand()
            textBox.updateScore(score[0])
            statusBar.printCards(root, playerHand, placement, width, height, textBox)
            
            playerTurnOver= game.getHumanPlayerTurn()
            
        if(game.getHumanPlayerTurn() == True):
            self.updateOtherPlayers(root, statusBar,width, height, textBox, computerTextBox, dealerTextBox, playerCurrency)
            
        
    def buttonStay(self, root,width, height,statusBar, textBox, hand,deck, placement, computerTextBox, dealerTextBox, playerCurrency):
        global playerTurnOver
        if playerTurnOver == False:        
            statusBar.updatePlayerTurn()
            game.humanPlayerInput(0)
            playerTurnOver= game.getHumanPlayerTurn()
            
        if(game.getHumanPlayerTurn() == True):
            self.updateOtherPlayers(root, statusBar,width, height, textBox, computerTextBox, dealerTextBox, playerCurrency)        
        
    def buttonDoubleDown(self,playerCurrency,root, width, height, statusBar, textBox, hand, deck, placement, computerTextBox, dealerTextBox):
        global playerTurnOver
        if playerTurnOver == False:        
            bet = playerCurrency.getBet()
            bet = bet * 2
            playerCurrency.updateBet(bet)
            
            game.humanPlayerInput(2)
            playerHand = game.get_playerHand()
            score = playerHand.countHand()
            textBox.updateScore(score[0])
            statusBar.printCards(root, playerHand, placement, width, height, textBox)
            
            playerTurnOver= game.getHumanPlayerTurn()
            
        if(game.getHumanPlayerTurn() == True):
            self.updateOtherPlayers(root, statusBar,width, height, textBox, computerTextBox, dealerTextBox, playerCurrency)                         
        
    # Class button constructor
    # @param root: the root window
    # @param text: the text to display on the button
    # @param width: the width of the button
    # @param height: the height of the button
    # @param bg_color: the background color of the button
    # @param x_pos: the x position to place the button at
    # @param y_pos: the y position to place the button at
    # @param command: the command to execute when a button is pressed, default = None
   
    def __init__(self, root, text, width, height, bg_color, x_pos, y_pos, statusBar,player1TextBox,computerTextBox, dealerTextBox,hand, deck,playerCurrency,command=None):
        playerTurn = statusBar.getPlayerTurn()
        
        if(command == "hit"):
            if(playerTurn == 1):
                self.button = tk.Button(root, text=text, bg=bg_color, relief = "ridge" ,bd=5,command=lambda: self.buttonHit(root,width, height,statusBar,player1TextBox, hand, deck,1, computerTextBox, dealerTextBox, playerCurrency))
                self.button.place(x=x_pos, y=y_pos, width = width/5, height = height/8)        
            else:
                self.button = tk.Button(root, text=text, bg=bg_color,relief = "ridge",bd=5, command=lambda: self.buttonHit(root,width, height,statusBar,computerTextBox, hand, deck,2, computerTextBox, dealerTextBox, playerCurrency))
                self.button.place(x=x_pos, y=y_pos, width = width/5, height = height/8)                
        if(command == "stay"):
            self.button = tk.Button(root, text=text, bg=bg_color, relief = "ridge",bd=5,command=lambda: self.buttonStay(root,width, height,statusBar, player1TextBox, hand,deck, 1, computerTextBox, dealerTextBox, playerCurrency))
            self.button.place(x=x_pos, y=y_pos, width = width/5, height = height/8)        
        if(command == "double down"):
            self.button = tk.Button(root, text=text, bg=bg_color, relief="ridge",bd=5,command = lambda: self.buttonDoubleDown(playerCurrency, root,width, height,statusBar, player1TextBox,hand,deck,1, computerTextBox, dealerTextBox))
            self.button.place(x=x_pos, y=y_pos, width = width/5, height = height/8)

    def updateOtherPlayers(self, root, statusBar,width, height, textBox, computerTextBox, dealerTextBox, currency):
        #global dealerScore, computerScore, playerScore
        
        root.after(1000)
        computerHand = game.get_computerHand()
      
        statusBar.printCards(root, computerHand, 2, width, height, textBox)
        dealerHand = game.get_dealerHand()
        
        statusBar.printCards(root, dealerHand, 0, width, height, textBox)
        statusBar.showScores(dealerTextBox, computerTextBox, textBox)   
        self.endScreen(root, width, height, currency)
        
    def endScreen(self, root, width, height, currency):
        winnings = currency.getBet()
        results = game.calculate_winner()
        print(results)
        newFrame = CasinoFrame(root, "white", width/2.5, height/4, width/3.3, height/4)
        resultString = ""
        if results == 0:
            resultString = "House wins! You lost $" + str(winnings)
        elif results == 1:
            resultString = "You and Computer win! You won $" + str(winnings)
        elif results == 2:
            resultString = "You win! You won $" + str(winnings)
        elif results == 3:
            resultString = "You lost! You lost $" + str(winnings)
            
        newTextBox = tk.Text(root, height = 5, width = 25)
        newTextBox.config(highlightthickness = 0, borderwidth = 0)
        newTextBox.insert(1.0,resultString)
        newTextBox.place(x=210, y=200)
       
# Class to create text boxes to track the score of the dealer and players
class CasinoScore:
   
    # Class score text box constructor
    # @param root: the root window
    # @param width: the width of the text box
    # @param height: the height of the text box
    # @param x_pos: the x position to place the text box at
    # @param y_pos: the y position to place the text box at    
    # @param bg_color: the background color of the text box
    def __init__(self,root, width, height, x_pos, y_pos, bg_color):
        self._score = 0
        self.textBox = tk.Text(root, bg = bg_color, relief="raised", bd=5)
        self.textBox.insert('1.0', self._score)
        self.textBox.config(state="disabled")
        self.textBox.place(x = x_pos, y= y_pos, height = height, width = width)
              
    def getScore(self):
        return self._score
        
    def updateScore(self, score):
        self.textBox.config(state="normal")
        self.textBox.delete('1.0', tk.END)
        self.textBox.insert('1.0', score)        
        self.textBox.config(state="disabled")
    
  
class Currency:
    
    def __init__(self,root, width, height, x_pos, y_pos, bg_color):
        self._bet = 5
        self.textBox = tk.Text(root, bg = bg_color, relief="raised", bd=5)
        self.textBox.insert('1.0', "$")
        self.textBox.insert('2.0', self._bet)
        self.textBox.config(state="disabled")
        self.textBox.place(x = x_pos, y= y_pos, height = height, width = width + 25)    
        
    def getBet(self):
        return self._bet
    
    def updateBet(self, value):
        self.textBox.config(state="normal")
        self._bet = value
        self.textBox.delete('1.0', tk.END)
        self.textBox.insert('1.0', "$")
        self.textBox.insert('2.0', self._bet)
        self.textBox.config(state="disabled")
       
# Class to create a status bar to display information        
class CasinoStatus:
       
    # Class status text box constructor
    # @param root: the root window
    # @param width: the width of the status text box
    # @param height: the height of the status text box  
    def __init__(self, root,width, height):
        self.textBox = tk.Text(root, bg = "grey")
        self.textBox.place(x=0, y=height-20, width = width, height = height/20)
        self.textBox.insert(1.0, "Welcome to Blackjack! Player 1 will go first!")
        self.textBox.config(state="disabled")
        self.player = 1
       
        #self.textBox.after(1000, self.openingTurn())
        #root.after(100, self.openingTurn())        
       
    def openingTurn(self, root):
        root.after(2000)
        self.textBox.config(state="normal")
        self.textBox.delete(1.0, tk.END)        
        self.textBox.insert(1.0, "Player 1's turn.")
        self.textBox.config(state="disabled")        
       
       
    # Update which player's turn it is
    # @param player: a numerical value of which player's turn it is: 1 or 2
    def getPlayerTurn(self):
        return self.player
       
       
    def updatePlayerTurn(self):
        self.textBox.config(state="normal")
        self.textBox.delete(1.0, tk.END)
       
        if(self.getPlayerTurn() == 1):
            self.textBox.insert(1.0, "Computer's turn.")
            self.player = 2
        else:
            self.player = 1
            self.textBox.insert(1.0, "Player 1's turn.")
           
        self.textBox.config(state="disabled")        
       
    def updateGameOver(self, winner):
        self.textBox.config(state="normal")
        self.textBox.delete(1.0, tk.END)
        if(winner == 1):
            self.textBox.insert(1.0, "You won!")
        elif(winner == 2):
            self.textBox.insert(1.0, "You lost, computer won!")
        else:
            self.textBox.insert(1.0, "Dealer won!")
        self.textBox.config(state="disabled")
        
    def printCards(self,root,hand, placement, width, height, textBox):
        dealerPlacement = (10, height /10)
        playerPlacement = (50, height/2)
        computerPlacement = (width *0.6, height/2)
        
        handLength = len(hand.cards)
        print("GUI MODEL HERE : ",hand.cards)
        if(handLength > 6):
            playerPlacement = (30, height/2)
            computerPlacement = (width * 0.5, height /2)
            
        if(handLength > 9):
            playerPlacement = (10, height/2)
            computerPlacement = (width * 0.4, height/2)
       
        #player = 1
        if placement == 1:
            for i in range(len(hand.cards)):
                newCard = CasinoCard(root, hand.cards[i].getSuit(), hand.cards[i].getValue(), playerPlacement[0] + (i*25), playerPlacement[1], textBox )
                
        #computer = 2
        elif placement == 2:
            for i in range(len(hand.cards)):
                newCard = CasinoCard(root, hand.cards[i].getSuit(), hand.cards[i].getValue(), computerPlacement[0] + (i*25), computerPlacement[1], textBox )
        #dealer = 0        
        elif placement == 0:
            for i in range(len(hand.cards)):
                newCard = CasinoCard(root, hand.cards[i].getSuit(), hand.cards[i].getValue(), dealerPlacement[0] + (i*75), dealerPlacement[1], textBox )      
       
    def showScores(self, dealerTextBox, computerTextBox, playerTextBox):
        score = game.get_dealerHand().countHand()
        dealerTextBox.updateScore(score[0])

        score = game.get_computerHand().countHand()
        computerTextBox.updateScore(score[0])
        
        score = game.get_playerHand().countHand()
        playerTextBox.updateScore(score[0])       
       
       
# Class to create a card using a label frame and a label      
class CasinoCard:
   
    #Class card constructor
    # @param root: the root window
    # @param suit: the suit of the card, string
    # @param value: the numerical value of the card, 1-10
    # @param row: the row to place the card at
    # @param column: the column to place the card at
    # @param textBox: the text box to increment the card score in
    def __init__(self, root, suit, value, row, column, textBox):
        currentScore = textBox.getScore()
        
       # 1 is hearts, 2 is diamonds, 3 is clubs, 4 is spades
        if(suit == 1):
            suit = chr(9829)
        elif(suit == 2):
            suit = chr(9830)
        elif(suit == 3):
            suit = chr(9827)
        elif(suit == 4):
            suit = chr(9824)

        if(value) == 11:
            value = 10
            face = "J"
        elif(value) == 12:
            value = 10
            face = "Q"
        elif(value) == 13:
            value = 10
            face = "K"
        elif(value) == 1:
            if(currentScore < 10):
                value = 11
            else:
                value = 1
            face = "A"
        else:
            face = value

        card_frame = tk.Frame(root,bg="white", width = 50, height = 100)
        card_frame.place(x=row, y = column)
       
        cardFrameLabel = tk.Label(card_frame, text="%s         \n%s         \n%s\n       %s\n       %s"% (suit,face,chr(0x263B),face,suit))
        cardFrameLabel.config(highlightbackground="black", highlightthickness = 2)
        cardFrameLabel.pack()  
          

class CasinoDeck():
   
    def __init__(self, root,width,height):
        deck_frame = tk.Frame(root,bg="orange", width = 50, height = 95, relief = "raised", bd = 5)
        deck_frame.place(x=width-width/20 -30, y = height/10)
        deck_frame.pack_propagate(False)
        deckFrameLabel = tk.Label(deck_frame, text = "%s"% (chr(0x263A)))
        deckFrameLabel.pack(pady=30)
       
#class gameSetup():
    #def __init__(self, root,width, height,numDecks, dealerTextBox, playerTextBox, computerTextBox, statusBar):
        #self._deck = Deck(numDecks)
        #self._deck.shuffle()
        #self._playerHand = Hand()
        #self._computerHand = Hand()
        #self._dealerHand = Hand()
        #self._dealerTextBox = dealerTextBox
        #self._statusBar = statusBar
        
        #card_frame = tk.Frame(root,bg="orange", width = 45, height = 85, relief = "raised", bd = 2)
        #card_frame.place(x=85, y = height/10)
        #card_frame.pack_propagate(False)
        #cardFrameLabel = tk.Label(card_frame, text = "%s"% (chr(0x263A)))
        #cardFrameLabel.pack(pady=30) 
        
        #card_frame = tk.Frame(root,bg="orange", width = 45, height = 85, relief = "raised", bd = 2)
        #card_frame.place(x=10, y = height/10)
        #card_frame.pack_propagate(False)
        #cardFrameLabel = tk.Label(card_frame, text = "%s"% (chr(0x263A)))
        #cardFrameLabel.pack(pady=30)        
        
        
    #def showScores(self, dealerTextBox, computerTextBox, playerTextBox):
        #for i in range(1):
            #self._dealerHand.draw(self._deck)
            #dealerTextBox.updateScore(self.getDealerHandValue())
           
        #for i in range(2):
            #self._computerHand.draw(self._deck)
            #computerTextBox.updateScore(self.getComputerHandValue())
           
        #for i in range(2):
            #self._playerHand.draw(self._deck)
            #playerTextBox.updateScore(self.getPlayerHandValue())
            
                     

    #def flipDealerCard(self, root, hand,height, width, statusBar, dealerTextBox):
        #self._dealerHand.draw(self._deck)
        #statusBar.printCards(root, self.getDealerHand(), 0, width, height, dealerTextBox)
        #dealerTextBox.updateScore(self.getDealerHandValue())
        
    #def getPlayerHand(self):
        #return self._playerHand
   
    #def getDealerHand(self):
        #return self._dealerHand
   
    #def getComputerHand(self):
        #return self._computerHand
   
    #def getDeck(self):
        #return self._deck
   
    #def getPlayerHandValue(self):
        #return self._playerHand.countHand()
   
    #def getComputerHandValue(self):
        #return self._computerHand.countHand()
   
    #def getDealerHandValue(self):
        #return self._dealerHand.countHand()

def getAlgorithm():
    return algorithm

def openCasinoWindow(algorithmDifficulty):
    global algorithm 
    algorithm = algorithmDifficulty
    
    casinoWindow = CasinoWindow()
   
    #Create reference variables
    width = casinoWindow.getWindowWidth()
    height = casinoWindow.getWindowHeight()
    root = casinoWindow.getRoot()
    player = casinoWindow.getPlayer()  
   
    #Create frames
    frame1 = CasinoFrame(root, "green", width, height/3, 0,0)
    frame2 = CasinoFrame(root, "green", width/2, height/2, 0, height *1/3)
    frame3 = CasinoFrame(root, "green", width/2, height/2, width/2, height  *1/3)
    frame4 = CasinoFrame(root, "saddle brown", width, height/5, 0, height * 4/5)
   
    #Create Score Boxes

    
    dealerScore = CasinoScore(root, 30, 30, width-width/20, 0, "white")
    computerScore = CasinoScore(root, 30, 30, width-width/20, height/3, "white")
    playerScore = CasinoScore(root, 30, 30, 0, height/3, "white")
    playerCurrency = Currency(root, 30, 30, width - width/11, height * 4/5, "white")
    
    #Create the status bar
    statusBar = CasinoStatus(root,width, height) 
    
    #Set the game up
    #game = gameSetup(root,width,height,5, dealerScore, playerScore, computerScore, statusBar)
    global game 
    game = BlackjackGame(6,100, getAlgorithm())
    
    #Create buttons
    button1 = CasinoButton(root, "Hit",width, height, "grey", int(width /4) - width/10 -50, int(height * 6.7/8), statusBar,playerScore, computerScore, dealerScore,game.get_playerHand(), game.get_deck(),playerCurrency,"hit")
    button2 = CasinoButton(root, "Stay", width, height, "grey", int(width /2) - width/10, int(height * 6.7/8),statusBar,playerScore, computerScore,dealerScore,game.get_playerHand(), game.get_deck(),playerCurrency,"stay")
    button3 = CasinoButton(root, "Double Down", width, height, "grey", int(width *3/4) - width/10 + 50, int(height *6.7/8),statusBar, playerScore, computerScore, dealerScore,game.get_playerHand(), game.get_playerHand(),playerCurrency, "double down")

    #Create the deck
    cardDeck = CasinoDeck(root,width,height)
   
    #Create labels for dealer and players
    heading = tk.Label(root, text="Dealer", relief="ridge", bd=5,width=12, height=2, bg="orange")
    heading.pack()
   
    computer_label = tk.Label(root, text="Player 1",relief="ridge", bd=5, width=10, height=2, bg="red")
    computer_label.place(x=width / 6, y=height / 3)
   
    player_label = tk.Label(root, text="Computer",relief="ridge", bd=5, width=10, height=2, bg="cyan")
    player_label.place(x=width * 7 / 10, y=height / 3)    
    
    root.update_idletasks()
    
    statusBar.openingTurn(root)
    
    game.start_game()
    
    #game.showScores(dealerScore, computerScore, playerScore)
    statusBar.printCards(root, game.get_playerHand(), 1, width, height, playerScore)
    statusBar.printCards(root, game.get_computerHand(), 2, width, height, computerScore)
    statusBar.printCards(root, game.get_dealerHand(), 0, width, height, dealerScore)    
    
    statusBar.showScores(dealerScore, computerScore, playerScore)
    
    #UNCOMMENT THIS TO FLIP DEALERS SECOND CARD
    #game.flipDealerCard(root, game.getDealerHand(), height, width, statusBar, dealerScore)
    root.mainloop()  
   
   
def selectDifficulty():
    #create the main menu window
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Main Casino Window")
    root.configure(bg= "light goldenrod")
    root.resizable(False, False)
   
    heading = tk.Label(text = "Welcome to the Casino!", font = "Latha", bg = "light goldenrod")
    heading.pack(pady=20)
   

    # Create buttons that will open the CasinoWindow
    button1 = tk.Button(root, text="Easy", relief="raised", bd=5,command=lambda: openCasinoWindow(1), bg = "light green")
    button1.place(x=150, y=100, width=100, height=50)
    
    button2 = tk.Button(root, text="Medium",relief="raised", bd=5, command=lambda:openCasinoWindow(2), bg = "light blue")
    button2.place(x=150, y=170, width=100, height=50)
     
    button3 = tk.Button(root, text="Hard",relief="raised", bd=5, command=lambda:openCasinoWindow(3), bg = "pink")               #TO HAVE DIFFERENT COMPUTER LOGIC, ADD A PARAMETER IN openCasinoWindow for easy, medium, and hard
    button3.place(x=150, y=240, width=100, height=50)

    root.mainloop()    
    
def main():
    selectDifficulty()
    
main()