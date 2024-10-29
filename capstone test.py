#Casino Blackjack Classes
# Alec Shalowitz Sam Slevin


# ASK NECAISE ABOUT AFTER()
# AFTER TIME ELAPSED DO THIS BUT AFTER GAME IS DISPLAYED AND NOT BEFORE


# Import tkinter
import tkinter as tk
from blackjack import *

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


# Class to create a button  
class CasinoButton:
   
   
    def buttonHit(self, root,width, height,statusBar, textBox, hand,deck, placement):
        #draw a new card
        #update score counter
        #change turn

        hand.draw(deck)
        if placement == 1:
            playerHand = hand.countHand()
           
        score = hand.hand[-1].getValue()
        textBox.updateScore(playerHand)
        statusBar.updatePlayerTurn()
        statusBar.printCards(root, hand, placement, width, height, textBox)
       #self,root,hand, placement, width, height, textBox
       
    def buttonStay(self, statusBar):
        statusBar.updatePlayerTurn()
        
    def buttonDoubleDown(self, playerCurrency):
        bet = playerCurrency.getBet()
        bet = bet * 2
        playerCurrency.updateBet(bet)
        
    # Class button constructor
    # @param root: the root window
    # @param text: the text to display on the button
    # @param width: the width of the button
    # @param height: the height of the button
    # @param bg_color: the background color of the button
    # @param x_pos: the x position to place the button at
    # @param y_pos: the y position to place the button at
    # @param command: the command to execute when a button is pressed, default = None
   
    def __init__(self, root, text, width, height, bg_color, x_pos, y_pos, statusBar,player1TextBox,computerTextBox,hand, deck,playerCurrency,command=None):
        playerTurn = statusBar.getPlayerTurn()
        
        if(command == "hit"):
            if(playerTurn == 1):
                self.button = tk.Button(root, text=text, bg=bg_color, relief = "ridge" ,bd=5,command=lambda: self.buttonHit(root,width, height,statusBar,player1TextBox, hand, deck,1))
                self.button.place(x=x_pos, y=y_pos, width = width/5, height = height/8)        
            else:
                self.button = tk.Button(root, text=text, bg=bg_color,relief = "ridge",bd=5, command=lambda: self.buttonHit(root,width, height,statusBar,computerTextBox, hand, deck,2))
                self.button.place(x=x_pos, y=y_pos, width = width/5, height = height/8)                
        if(command == "stay"):
            self.button = tk.Button(root, text=text, bg=bg_color, relief = "ridge",bd=5,command=lambda: self.buttonStay(statusBar))
            self.button.place(x=x_pos, y=y_pos, width = width/5, height = height/8)        
        if(command == "double down"):
            self.button = tk.Button(root, text=text, bg=bg_color, relief="ridge",bd=5,command = lambda: self.buttonDoubleDown(playerCurrency))
            self.button.place(x=x_pos, y=y_pos, width = width/5, height = height/8)

       
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
   
    #def updateScore(self, game, whichPlayer):
        #self.textBox.config(state="normal")
        #self.textBox.delete('1.0', tk.END)
        #if(whichPlayer) == 1:
            #self.textBox.insert('1.0', game.getPlayerHand())
        #elif(whichPlayer) == 2:
            #self.textBox.insert('1.0', game.getComputerHand())
        #elif(whichPlayer) == 0:
            #self.textBox.insert('1.0', game.getDealerHand())
        #self.textBox.config(state="disabled")
   

    
        
    def updateScore(self, score):
        self.textBox.config(state="normal")
        self.textBox.delete('1.0', tk.END)
        self.textBox.insert('1.0', score)        

    
  
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
       
    ## Update the score of the text box with the old score + new score
    ## @param score: the score to add to the old score
    #def updateScore(self, score):
        ##assert score <= 100
        #self.textBox.config(state="normal")
        #self.previousScore = int(self.textBox.get('1.0', 'end-1c'))
        #self.textBox.delete('1.0', tk.END)
        #newScore = score + self.previousScore
        #self.textBox.insert('1.0', newScore)      
        #self.textBox.config(state="disabled")
        #print("Previous Score: ",self.previousScore,"Score to be added:",score,"New Score: ",newScore)
       

# Class to create a status bar to display information        
class CasinoStatus:
       
    # Class status text box constructor
    # @param root: the root window
    # @param width: the width of the status text box
    # @param height: the height of the status text box  
    def __init__(self, root,width, height):
        self.textBox = tk.Text(root, bg = "yellow")
        self.textBox.place(x=0, y=height-20, width = width, height = height/20)
        self.textBox.insert(1.0, "Welcome to Blackjack! Player 1 will go first!")
        self.textBox.config(state="disabled")
        self.player = 1
       
        #self.textBox.after(1000, self.openingTurn())
        #root.after(100, self.openingTurn())        
       
    def openingTurn(self):
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
       
        #player = 1
        if placement == 1:
            for i in range(len(hand.hand)):
                newCard = CasinoCard(root, hand.hand[i].getSuit(), hand.hand[i].getValue(), playerPlacement[0] + (i*25), playerPlacement[1], textBox )
                
        #computer = 2
        elif placement == 2:
            for i in range(len(hand.hand)):
                newCard = CasinoCard(root, hand.hand[i].getSuit(), hand.hand[i].getValue(), computerPlacement[0] + (i*25), computerPlacement[1], textBox )
        #dealer = 0        
        elif placement == 0:
            for i in range(len(hand.hand)):
                newCard = CasinoCard(root, hand.hand[i].getSuit(), hand.hand[i].getValue(), dealerPlacement[0] + (i*75), dealerPlacement[1], textBox )      
       
# Class to create a card using a label frame and a label      
class CasinoCard:
   
    #Class card constructor
    # @param root: the root window
    # @param suit: the suit of the card, string
    # @param value: the numerical value of the card, 1-10
    # @param row: the row to place the card at
    # @param column: the column to place the card at
    # @param textBox: the text box to increment the card score in
   
    #NEED TO HANDLE ACE KING QUEEN JACK 11/1? 12 13 14
    def __init__(self, root, suit, value, row, column, textBox):
        currentScore = textBox.getScore()
       # 1 is hearts, 2 is diamonds, 3 is clubs, 4 is spades
        #if(suit == "spades"):
            #suit = chr(9824)
        #elif(suit == "clubs"):
            #suit = chr(9827)
        #elif(suit == "hearts"):
            #suit = chr(9829)
        #elif(suit == "diamonds"):
            #suit = chr(9830)
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
           
            #card_frame = tk.LabelFrame(root, text=suit, bd=0)
        card_frame = tk.Frame(root,bg="white", width = 50, height = 100)
        #card_frame.grid(row = row, column = column, padx = 20, pady=20)
        card_frame.place(x=row, y = column)
       
           
           
        cardFrameLabel = tk.Label(card_frame, text="%s         \n%s         \n%s\n       %s\n       %s"% (suit,face,chr(0x263B),face,suit))
        cardFrameLabel.config(highlightbackground="black", highlightthickness = 2)
        cardFrameLabel.pack()  
       
        #textBox.updateScore(value)

            ##card_frame = tk.LabelFrame(root, text=suit, bd=0)
            #card_frame = tk.Frame(root,bg="white", width = 50, height = 100)
            ##card_frame.grid(row = row, column = column, padx = 20, pady=20)
            #card_frame.place(x=row, y=column)
            #cardFrameLabel = tk.Label(card_frame, text="%s         \n%s         \n%s\n       %s\n       %s"% (suit,value,chr(0x263A),value,suit))
            #cardFrameLabel.config(highlightbackground="black", highlightthickness = 2)
            #cardFrameLabel.pack()
           
            #textBox.updateScore(value)
           
       
           

class CasinoDeck():
   
    def __init__(self, root,width,height):
        deck_frame = tk.Frame(root,bg="black", width = 50, height = 95, relief = "raised", bd = 5)
        deck_frame.place(x=width-width/20 -30, y = height/10)
        deck_frame.pack_propagate(False)
        deckFrameLabel = tk.Label(deck_frame, text = "%s"% (chr(0x263A)))
        deckFrameLabel.pack(pady=30)
       
class gameSetup():
    def __init__(self, numDecks, dealerTextBox, playerTextBox, computerTextBox):
        self._deck = Deck(numDecks)
        self._deck.shuffle()
        self._playerHand = Hand()
        self._computerHand = Hand()
        self._dealerHand = Hand()
       
        for i in range(2):
            self._dealerHand.draw(self._deck)
            dealerTextBox.updateScore(self.getDealerHandValue())
           
        for i in range(2):
            self._computerHand.draw(self._deck)
            computerTextBox.updateScore(self.getComputerHandValue())
           
        for i in range(2):
            self._playerHand.draw(self._deck)
            playerTextBox.updateScore(self.getPlayerHandValue())
           
    def getPlayerHand(self):
        return self._playerHand
   
    def getDealerHand(self):
        return self._dealerHand
   
    def getComputerHand(self):
        return self._computerHand
   
    def getDeck(self):
        return self._deck
   
    def getPlayerHandValue(self):
        return self._playerHand.countHand()
   
    def getComputerHandValue(self):
        return self._computerHand.countHand()
   
    def getDealerHandValue(self):
        return self._dealerHand.countHand()
   
def openCasinoWindow():
    casinoWindow = CasinoWindow()
   
   
    #Create reference variables
    width = casinoWindow.getWindowWidth()
    height = casinoWindow.getWindowHeight()
    root = casinoWindow.getRoot()
    player = casinoWindow.getPlayer()

   
    #def printCards(root,hand, placement, width, height, textBox):
        #dealerPlacement = (10, height /10)
        #playerPlacement = (50, height/2)
        #computerPlacement = (width *0.6, height/2)
       
        ##player = 1
        #if placement == 1:
            #for i in range(len(hand.hand)):
                #newCard = CasinoCard(root, hand.hand[i].getSuit(), hand.hand[i].getValue(), playerPlacement[0] + (i*25), playerPlacement[1], textBox )
        ##computer = 2
        #elif placement == 2:
            #for i in range(len(hand.hand)):
                #newCard = CasinoCard(root, hand.hand[i].getSuit(), hand.hand[i].getValue(), computerPlacement[0] + (i*25), computerPlacement[1], textBox )
        ##dealer = 0        
        #elif placement == 0:
            #for i in range(len(hand.hand)):
                #newCard = CasinoCard(root, hand.hand[i].getSuit(), hand.hand[i].getValue(), dealerPlacement[0] + (i*75), dealerPlacement[1], textBox )    
   
    #Create frames
    frame1 = CasinoFrame(root, "green", width, height/3, 0,0)
    frame2 = CasinoFrame(root, "green", width/2, height/2, 0, height *1/3)
    frame3 = CasinoFrame(root, "green", width/2, height/2, width/2, height  *1/3)
    frame4 = CasinoFrame(root, "saddle brown", width, height/5, 0, height * 4/5)
   
    #Create Score Boxes
    dealerScore = CasinoScore(root, 30, 30, width-width/20, 0, "white")
    computerScore = CasinoScore(root, 30, 30, width-width/20, height/3, "white")
    playerScore = CasinoScore(root, 30, 30, width/2 - width/20, height/3, "white")
    playerCurrency = Currency(root, 30, 30, width - width/11, height * 4/5, "white")
    #playerCurrency.updateCurrency(5)
   
   
    game = gameSetup(1, dealerScore, playerScore, computerScore)
    #Create status bar
    statusBar = CasinoStatus(root,width, height)  
   
    #Create buttons
  
    #button1 = CasinoButton(root, "Hit",width, height, "yellow", int(width/8), int(height * 6.7/8), statusBar,playerScore, computerScore, game.getPlayerHand(), game.getDeck(),"hit")
    button1 = CasinoButton(root, "Hit",width, height, "yellow", int(width /4) - width/10 -50, int(height * 6.7/8), statusBar,playerScore, computerScore, game.getPlayerHand(), game.getDeck(),playerCurrency,"hit")
    #button2 = CasinoButton(root, "Stay", int(width/4), int(height/8), "yellow", width * 5/8, height * 6.7/8,statusBar,playerScore, computerScore,game.getPlayerHand(), game.getDeck(),"stay")
    button2 = CasinoButton(root, "Stay", width, height, "yellow", int(width /2) - width/10, int(height * 6.7/8),statusBar,playerScore, computerScore,game.getPlayerHand(), game.getDeck(),playerCurrency,"stay")
    button3 = CasinoButton(root, "Double Down", width, height, "yellow", int(width *3/4) - width/10 + 50, int(height *6.7/8),statusBar, playerScore, computerScore, game.getPlayerHand(), game.getDeck(),playerCurrency, "double down")
                           
    #| button | button | button |
   
    ##Create cards
    #card = CasinoCard(root, 1, 11, 10, height/10, dealerScore)
    #card2 = CasinoCard(root, 2, 2, 90, height/10, dealerScore)
    #card3 = CasinoCard(root, 4, 3, 170, height/10, dealerScore)
    #card4 = CasinoCard(root, 3, 12, 250, height/10, dealerScore)
   
    #card5 = CasinoCard(root, 4, 10, 10, height/2, playerScore)
    #card6 = CasinoCard(root, 3, 2, 60, height/2, playerScore)
   
    ##card7 = CasinoCard(root, "diamonds", "jack", width/2 + 10, height/2, computerScore)
    #card7 = CasinoCard(root, 2, 1, width * 0.6, height/2, computerScore)
    #card8 = CasinoCard(root, 4, 5, width*0.6 + 25, height/2, computerScore)
    #card9 = CasinoCard(root, 3, 9, width*0.6 + 50, height/2, computerScore)
    #card10 = CasinoCard(root, 3, 8, width*0.6 + 75, height/2, computerScore)
    #card11 = CasinoCard(root, 1, 7, width*0.6 + 100, height/2, computerScore)
   
    #Create the deck
    cardDeck = CasinoDeck(root,width,height)
   
    #Create labels for dealer and players
    heading = tk.Label(root, text="Dealer", relief="ridge", bd=5,width=12, height=2, bg="orange")
    heading.pack()
   
    computer_label = tk.Label(root, text="Player 1",relief="ridge", bd=5, width=10, height=2, bg="red")
    computer_label.place(x=width / 6, y=height / 3)
   
    player_label = tk.Label(root, text="Computer",relief="ridge", bd=5, width=10, height=2, bg="blue")
    player_label.place(x=width * 7 / 10, y=height / 3)    
 
    #root.after(2000,statusBar.openingTurn())

       
    statusBar.printCards(root, game.getPlayerHand(), 1, width, height, playerScore)
    statusBar.printCards(root, game.getComputerHand(), 2, width, height, computerScore)
    statusBar.printCards(root, game.getDealerHand(), 0, width, height, dealerScore)    
   
   
    #create the main menu loop
    casinoWindow.getRoot().mainloop()  
   
   
def main():
    #create the main menu window
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Main Casino Window")
    root.configure(bg= "light goldenrod")
    root.resizable(False, False)
   
    heading = tk.Label(text = "Welcome to the Casino!", font = "Latha")
    heading.pack()
   

    # Create buttons that will open the CasinoWindow
    button1 = tk.Button(root, text="Easy", relief="raised", bd=5,command=openCasinoWindow, bg = "light green")
    button1.place(x=150, y=100, width=100, height=50)

    button2 = tk.Button(root, text="Medium",relief="raised", bd=5, command=openCasinoWindow, bg = "light blue")
    button2.place(x=150, y=170, width=100, height=50)
     
    button3 = tk.Button(root, text="Hard",relief="raised", bd=5, command=openCasinoWindow, bg = "pink")               #TO HAVE DIFFERENT COMPUTER LOGIC, ADD A PARAMETER IN openCasinoWindow for easy, medium, and hard
    button3.place(x=150, y=240, width=100, height=50)

    root.mainloop()    
   
main()