
import pygame, random
from RRPSgameLogic import *
from RRPSmusicImagesFonts import *
from RRPSguiLogic import *
pygame.init()

class Game:
    music = Music()  
    def __init__(self):
        self.click_time = 0
        self.playcomputer = False
    
    def createIntroButtons(self):
        self.playLocalButton = Button(rect=(380,390,70,98), imageSurface=Images.PaperImageintro, fontLocation=Fonts.amaticBoldfont,
                        words='      Local', wordsSize=26, color=Colors.brightGreen, command=self.transition
                        )
        self.playcomputerButton = Button(rect=(510,390,70,98), imageSurface=Images.RockImageintro, fontLocation=Fonts.amaticBoldfont,
                        words='  Computer', wordsSize=26, color=Colors.brightRed, command=self.playComputer
                        )
        self.introButtonList = [self.playLocalButton, self.playcomputerButton]
        
    def createInputLoopButtons(self):
        self.rockButton = Button(rect=(180,330,140,194), imageSurface=Images.RockCardImage, command=self.rocktrue)
        self.paperButton = Button(rect=(410,330,140,195), imageSurface=Images.PaperCardImage, command=self.papertrue)
        self.scissorsButton = Button(rect=(640,330,140,195), imageSurface=Images.ScissorsCardImage, command=self.scissorstrue)
        self.backButton = Button(fontLocation=Fonts.amaticBoldfont, words='BACK', wordsSize=35, color=Colors.red,
                         bgColor=Colors.white, rect=(5,5,45,40), command=self.backtomenu
                         )
        self.mainloopButtons = [self.rockButton,self.paperButton,self.scissorsButton,self.backButton]
        
    def createIntroText(self):
        self.Title1 = Text(color=Colors.brightRed,fontLocation=Fonts.karmaticArcadefont, wordsSize=50,
                words='R  E  S  T  R  I  C  T  E  D', x=(GameGUI.display_width/2), y=(GameGUI.display_height/2)-220
                )
        self.Title2 = Text(color=Colors.pink,fontLocation=Fonts.karmaticArcadefont, wordsSize=30,
                words='R o c k', x=(GameGUI.display_width/2), y=(GameGUI.display_height/2)-120
                )
        self.Title3 = Text(color=Colors.brightBlue,fontLocation=Fonts.karmaticArcadefont, wordsSize=30,
                words='P a p e r', x=(GameGUI.display_width/2), y=(GameGUI.display_height/2)-50
                )
        self.Title4 = Text(color=Colors.yellow,fontLocation=Fonts.karmaticArcadefont, wordsSize=30,
                words='S c i s s o r s', x=(GameGUI.display_width/2), y=(GameGUI.display_height/2)+20
                )
        self.TitleList = [self.Title1, self.Title2, self.Title3, self.Title4]
        for t in self.TitleList:
            t.final()

    def createTransitionText(self):
        linecolor1= Colors.red
        linecolor2=Colors.white
        
        self.line1 = Text(color=linecolor1,fontLocation=Fonts.amaticBoldfont,wordsSize=50,
                words="Show me what you're worth, kouzu.", x=250, y=100
                )
        self.line2 = Text(color=linecolor1,fontLocation=Fonts.amaticBoldfont, wordsSize=50,
                words='Only one of you can be free...', x=250, y=180
                )
        self.line3 = Text(color=linecolor1,fontLocation=Fonts.amaticBoldfont, wordsSize=100,
                words="Heh HEH heh", x=250, y=260
                )
        self.line4 = Text(color=linecolor2,fontLocation=Fonts.amaticBoldfont,wordsSize=40,
                words='What the hell is this...', x=(GameGUI.display_width/2), y=(GameGUI.display_height-25)
                )
        
        self.instructions1 = Text(color=linecolor2,fontLocation=Fonts.amaticBoldfont,wordsSize=50,
                words="You are handed 12 cards, and start with 3 points", x=(GameGUI.display_width/2), y=100
                )
        self.instructions2 = Text(color=linecolor2,fontLocation=Fonts.amaticBoldfont, wordsSize=50,
                words='Your deck is split evenly between rock, paper, and scissors', x=(GameGUI.display_width/2), y=200
                )
        self.instructions3 = Text(color=linecolor2,fontLocation=Fonts.amaticBoldfont, wordsSize=50,
                words="The only way to win is to get to 6 points", x=(GameGUI.display_width/2), y=300
                )
        self.clicktocontinue = Text(color=linecolor1,fontLocation=Fonts.amaticBoldfont, wordsSize=40,
                words="Click to continue", x=(GameGUI.display_width/2), y=450
                )
        
        self.transitionwords = [self.line1, self.line2, self.line3, self.line4, self.instructions1,
                 self.instructions2, self.instructions3, self.clicktocontinue]
        ly = 20
        
        for l in self.transitionwords:
            if l != self.line4 and l != self.instructions1 and l != self.instructions2 and l != self.instructions3 and l != self.clicktocontinue:
                l.x = 300
                l.y = ly+80
                ly = l.y
            l.final()
        
    def createSelectText(self):
        self.selectTextrock = Text(color=Colors.brightGreen,fontLocation=Fonts.amaticBoldfont,wordsSize=40,
        words="Select", x=250, y=300)
        self.selectTextpaper = Text(color=Colors.brightGreen,fontLocation=Fonts.amaticBoldfont,wordsSize=40,
        words="Select", x=480, y=300)
        self.selectTextscissors = Text(color=Colors.brightGreen,fontLocation=Fonts.amaticBoldfont,wordsSize=40,
        words="Select", x=710, y=300)
        selectTextlist = [self.selectTextrock,self.selectTextpaper,self.selectTextscissors]
        for i in selectTextlist:
            i.final()
        
    def createScoreText(self):
        self.p1score = Text(color=Colors.yellow,fontLocation=Fonts.amaticBoldfont,wordsSize=50,
                        words=f'P1: {self.player1.score}', x=50, y=100
                        )
        self.p2score = Text(color=Colors.brightRed,fontLocation=Fonts.amaticBoldfont,wordsSize=50,
                        words=f'P2: {self.player2.score}', x=900, y=100
                        )
        self.scoreTextlist = [self.p1score,self.p2score]
        for i in self.scoreTextlist:
            i.final()
            
    def createPlayerTurnText(self):
        self.player1turn = Text(color=Colors.yellow, fontLocation=Fonts.amaticBoldfont,wordsSize=50,
                            words=f'Player 1', x=((GameGUI.display_width)-50), y=25
                            )
        self.player2turn = Text(color=Colors.brightRed, fontLocation=Fonts.amaticBoldfont,wordsSize=50,
                            words=f'Player 2', x=((GameGUI.display_width)-50), y=25
                            )
    
    def createCardTotalsText(self):
        p1color= Colors.yellow
        p2color=Colors.brightRed
        
        self.p1rocks = Text(color=p1color,fontLocation=Fonts.karmaticArcadefont,wordsSize=30,
                        words=self.player1.cardtotals['Rock total'], x=150, y=450
                        )
        self.p2rocks = Text(color=p2color,fontLocation=Fonts.karmaticArcadefont,wordsSize=30,
                        words=self.player2.cardtotals['Rock total'], x=150, y=450
                        )  
        self.p1papers = Text(color=p1color,fontLocation=Fonts.karmaticArcadefont,wordsSize=30,
                        words=self.player1.cardtotals['Paper total'], x=380, y=450
                        )
        self.p2papers = Text(color=p2color,fontLocation=Fonts.karmaticArcadefont,wordsSize=30,
                        words=self.player2.cardtotals['Paper total'], x=380, y=450
                        )
        self.p1scissors = Text(color=p1color,fontLocation=Fonts.karmaticArcadefont,wordsSize=30,
                            words=self.player1.cardtotals['Scissors total'], x=610, y=450
                            )
        self.p2scissors = Text(color=p2color,fontLocation=Fonts.karmaticArcadefont,wordsSize=30,
                            words=self.player2.cardtotals['Scissors total'], x=610, y=450
                            )
        
        self.p1cardtotalslist = [self.p1rocks, self.p1papers, self.p1scissors]
        self.p2cardtotalslist = [self.p2rocks, self.p2papers, self.p2scissors]
        
    def createWinnerText(self):       
        self.p1winsRoundtext = Text(color=Colors.red,fontLocation=Fonts.karmaticArcadefont,wordsSize=40,
                                words="Player 1 Wins", x=(GameGUI.display_width/2), y=(40)
                                )
        self.p2winsRoundtext = Text(color=Colors.red,fontLocation=Fonts.karmaticArcadefont,wordsSize=40,
                                words="Player 2 Wins", x=(GameGUI.display_width/2), y=(40)
                                )
        self.nowinnerRoundtext = Text(color=Colors.red,fontLocation=Fonts.karmaticArcadefont,wordsSize=40,
                                words="T I E", x=(GameGUI.display_width/2), y=(40)
                                )
        
        movingText = MovingText()
        self.p1winstextmultiline = movingText.linetextcomplete(
            string='Player 1 is free and Player 2 will toil for the company indefinitely', multOrSing=movingText.multilinetext, wsize=25
            )
        self.p2winstextmultiline = movingText.linetextcomplete(
            string='Player 2 is free and Player 1 will toil for the company indefinitely', multOrSing=movingText.multilinetext, wsize=25
            )
        self.nowinnersingleline = movingText.linetextcomplete(
            string='Both players failed to impress the company ... the opportunity is lost', multOrSing=movingText.multilinetext, wsize=25
            )
        self.indefinitely = movingText.linetextcomplete(string='Indefinitely', multOrSing=movingText.singlelinetext, wsize=20)

        self.winnertextlist = [self.p1winsRoundtext, self.p2winsRoundtext, self.nowinnerRoundtext]
        for i in self.winnertextlist:
            i.final()   
     

         
    def run(self):
        self.music.playmusic()
        
        self.createIntroText()
        
        self.createIntroButtons()
        
        self.intro = True
        while(self.intro):
            
            for event in pygame.event.get():
#                 print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_time = pygame.time.get_ticks()
                self.playcomputerButton.get_event(event)
                self.playLocalButton.get_event(event)
                
            GameGUI.gameDisplay.fill(Colors.black)
            GameGUI.gameDisplay.blit((Images.AkagiVsKaiji), (0, 0))
            
            for t in self.TitleList:    
                t.displayText()
            for b in self.introButtonList:
                b.renderImgText(GameGUI.gameDisplay)

            pygame.display.update()
            GameGUI.clock.tick(15)
      


    def transition(self):
        self.intro = False
        GameGUI.gameDisplay.fill(Colors.black)
        GameGUI.gameDisplay.blit((Images.ChairmanHappy), (((GameGUI.display_width-400)), ((GameGUI.display_height-622)/2)))
        
        self.createTransitionText()
        
        skipTransition = False
        passed_time = 0
        self.transitionScene = True
        while(self.transitionScene):
            for event in pygame.event.get():
#                 print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    skipTransition = True
                    
            #timer starts after playLocalButton click in intro loop    
            if self.click_time != 0:  # If timer has been started.
            # Calculate the passed time since the click.
                passed_time = (pygame.time.get_ticks()-self.click_time) / 1000

            if skipTransition == False:
                if passed_time >= 1:
                    self.line1.displayText()
                if passed_time >= 3:
                    self.line2.displayText()
                if passed_time >= 5:
                    GameGUI.gameDisplay.fill(Colors.black)
                    GameGUI.gameDisplay.blit((Images.ChairmanHappy), (((GameGUI.display_width-400)), ((GameGUI.display_height-622)/2)))
                    self.line3.displayText()
                if passed_time >= 7:
                    GameGUI.gameDisplay.fill(Colors.black)
                if passed_time >=10:
                    GameGUI.gameDisplay.blit((Images.cardsPicTransition), (0,0))
                    self.line4.displayText()
                if passed_time >=14:
                    GameGUI.gameDisplay.fill(Colors.black)
                if passed_time >=15:
                    self.instructions1.displayText()
                    self.instructions2.displayText()
                    self.instructions3.displayText()
                if passed_time >=17:
                    self.clicktocontinue.displayText()

            else: 
                self.transitionScene = False
                self.mainLoop()
            pygame.display.update()
            GameGUI.clock.tick(15)
        

    
    def backtomenu(self):
        self.playcomputer = False
        self.run()
    
    def playComputer(self):
        self.playcomputer = True
        self.transition()
    
    # create game logic objects
    def createCardTypes(self):
        self.rock = Card(CardName.ROCK.name)
        self.paper = Card(CardName.PAPER.name)
        self.scissors = Card(CardName.SCISSORS.name)

    def createDeck(self):
        self.createCardTypes()
        deck = Deck([])
        for i in range(4):
            deck.addCard(self.rock)
            deck.addCard(self.paper)
            deck.addCard(self.scissors)
        deck.cards = sorted(deck.cards)
        return deck

    def getNewPlayer(self, score, computerplayer=False):
        player = Player(score, computerplayer)
        deck = self.createDeck()
        player.addDeck(deck)
        # self.player.cardTotals() was here but didnt do anything because it returned into nothing
        # self.player.cardTotals()
        return player
    
    def getPlayerCardDicts(self):
        self.allcardtotals = {'p1':0,'p2':0}
        self.allPlayersCardDicts = []
        self.allPlayersCardDicts.append(self.player1.cardTotals())
        self.allPlayersCardDicts.append(self.player2.cardTotals())
        for i, j in zip(self.allPlayersCardDicts[0].values(), self.allPlayersCardDicts[1].values()):
            self.allcardtotals['p1'] += int(i)
            self.allcardtotals['p2'] += int(j)
            
    def createPlayers(self, score=3):
        self.player1 = self.getNewPlayer(score)
        if self.playcomputer==True:
            self.player2 = self.getNewPlayer(score, self.playComputer)
        else: self.player2 = self.getNewPlayer(score)
        self.getPlayerCardDicts()
           
    def rocktrue(self):
        self.rockClick = True
    def papertrue(self):
        self.paperClick = True
    def scissorstrue(self):
        self.scissorsClick = True
        
    def computerCardChoice(self):
        randomcard = random.randint(0,2)
        if randomcard == 0:
            self.rocktrue()
        if randomcard == 1:
            self.papertrue()
        if randomcard == 2:
            self.scissorstrue()
            
    def runInputLoop(self):
        waitforclick.true()
        self.inputLoop()
            


    def cardInput(self):
    
        handPlayed = 0
        cardName = '' 
        self.currentPlayerImage=0
        self.showcardwin0 = ''
        self.showcardwin1 = ''
        self.showcardwin2 = ''
        
        while(handPlayed < 2):
            
            if self.player2.computerplayer:
                if handPlayed==1:
                    self.computerCardChoice()
                else:self.runInputLoop()
                    
            else:self.runInputLoop()

            try:
                if self.rockClick:
                    cardName = CardName.ROCK.name
                    if handPlayed == 0:
                        self.showcardwin1 = 'R'
                    if handPlayed == 1:
                        self.showcardwin2 = 'R'
                    self.rockClick = False
                    
                elif self.paperClick:
                    cardName = CardName.PAPER.name
                    if handPlayed == 0:
                        self.showcardwin1 = 'P'
                    if handPlayed == 1:
                        self.showcardwin2 = 'P'
                    self.paperClick = False
                        
                elif self.scissorsClick:
                    cardName = CardName.SCISSORS.name
                    if handPlayed == 0:
                        self.showcardwin1 = 'S'
                    if handPlayed == 1:
                        self.showcardwin2 = 'S'
                    self.scissorsClick = False

                cardPlayed = Card(cardName)
                if(handPlayed % 2 == 0):
                    self.player1.chosenAndRemoveCard(cardPlayed)
                    self.currentPlayerImage=1  
                else:
                    self.player2.chosenAndRemoveCard(cardPlayed)
                    waitforclick.false()
                handPlayed += 1
            except:
                print('check if you have the card left')  
        
    def RockWinner(self):
        return True if(self.player1.card == self.rock and self.player2.card == self.scissors) else False 

    def PaperWinner(self):
        return True if(self.player1.card == self.paper and self.player2.card == self.rock) else False 

    def ScissorsWinner(self):
        return True if(self.player1.card == self.scissors and self.player2.card == self.paper) else False
    
    def tie(self):
        if((self.player1.card == self.rock and self.player2.card == self.rock) or 
                (self.player1.card == self.paper and self.player2.card == self.paper) or 
                (self.player1.card == self.scissors and self.player2.card == self.scissors)
                ):
            return True
        else: return False
        
    def distributePoint(self):
        if self.tie():
            self.showWinnerCardscene(self.nowinnerRoundtext, self.showcardwin0)
            
        elif self.RockWinner() or self.PaperWinner() or self.ScissorsWinner():
            self.player1.addPoint()
            # self.player2.removePoint()
            self.showWinnerCardscene(self.p1winsRoundtext, self.showcardwin1)
        else:
            self.player2.addPoint()
            # self.player1.removePoint()
            self.showWinnerCardscene(self.p2winsRoundtext, self.showcardwin2)
        
    def getWinner(self):
#         print(self.allcardtotals)
        if(int(self.player1.score) == 8) or ((self.allcardtotals['p1']+self.allcardtotals['p2']==0) and 
                int(self.player1.score) > int(self.player2.score)
                ):
            self.winScene(self.p1winstextmultiline)

        elif(int(self.player2.score) == 8) or ((self.allcardtotals['p1']+self.allcardtotals['p2']==0) and 
                int(self.player2.score) > int(self.player1.score)
                ):
            self.winScene(self.p2winstextmultiline)
            
        elif((self.allcardtotals['p1']+self.allcardtotals['p2']==0) and 
                int(self.player1.score) == int(self.player2.score)
                ):
            self.winScene(self.nowinnersingleline)

        else: return False
        
        
    def inputLoop(self):
        self.createSelectText()
        self.player1turn.final()
        self.player2turn.final()
        while waitforclick.wait==True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_time = pygame.time.get_ticks()
                    
                for i in self.mainloopButtons:
                    i.get_event(event)

            if self.currentPlayerImage == 0:
                GameGUI.gameDisplay.fill(Colors.black)
                GameGUI.gameDisplay.blit(Images.kaijiupset,(110,0))
                self.player1turn.displayText()
                self.p1rocks.words = self.player1.cardtotals['Rock total']
                self.p1papers.words = self.player1.cardtotals['Paper total']
                self.p1scissors.words = self.player1.cardtotals['Scissors total']
                for i in self.p1cardtotalslist:
                    i.final()
                    i.displayText()
                for i in self.scoreTextlist:
                    i.final()
                    i.displayText()
                    
            if self.currentPlayerImage == 1:
                GameGUI.gameDisplay.fill(Colors.black)
                GameGUI.gameDisplay.blit(Images.akaginormal,(110,0)) 
                self.player2turn.displayText()
                self.p2rocks.words = self.player2.cardtotals['Rock total']
                self.p2papers.words = self.player2.cardtotals['Paper total']
                self.p2scissors.words = self.player2.cardtotals['Scissors total']
                
                for i in self.p2cardtotalslist:
                    i.final()
                    i.displayText()
                for i in self.scoreTextlist:
                    i.final()
                    i.displayText()
                    
            for b in self.mainloopButtons:
                if b.words=='':
                    b.renderImg(GameGUI.gameDisplay)
                else:
                    b.renderTxt(GameGUI.gameDisplay)
                    
            mouse = pygame.mouse.get_pos()
            if 180+140 > mouse[0] > 180 and 330+194 > mouse[1] > 330:
                self.selectTextrock.displayText()
            if 410+140 > mouse[0] > 410 and 330+194 > mouse[1] > 330:
                self.selectTextpaper.displayText()
            if 640+140 > mouse[0] > 640 and 330+194 > mouse[1] > 330:
                self.selectTextscissors.displayText()
                
            pygame.display.update()
            GameGUI.clock.tick(15)
    

    
    def setVariablesfalse(self):
        self.winner = False
        self.rockClick=False
        self.paperClick=False
        self.scissorsClick=False
        self.backClick=False
        
        
    def mainLoop(self):
        self.transitionScene = False
        self.createPlayers()
        
        self.setVariablesfalse()
        
        self.createInputLoopButtons()

        
        
        self.createWinnerText()
        
        self.createScoreText()
        
        self.createCardTotalsText()
        
        self.createPlayerTurnText()
        
        
        while(self.winner==False):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    quit()

            self.createScoreText()
            self.p1score.displayText()
            self.p2score.displayText()
            
            self.getPlayerCardDicts()
            self.getWinner()
            self.cardInput()
            self.distributePoint()

            GameGUI.clock.tick(15)

 
    def showWinnerCardscene(self, playerwinner, showcardwin):
        self.cardwinimage = ''
        if showcardwin == '':
            self.cardwinimage = Images.Tonegawa
        else:
            if playerwinner == self.p1winsRoundtext:
                if showcardwin == 'R':
                    self.cardwinimage = Images.RockCardImage
                if showcardwin == 'P':
                    self.cardwinimage = Images.PaperCardImage
                if showcardwin == 'S':
                    self.cardwinimage = Images.ScissorsCardImage
            if playerwinner == self.p2winsRoundtext:
                if showcardwin == 'R':
                    self.cardwinimage = Images.RockCardImage
                if showcardwin == 'P':
                    self.cardwinimage = Images.PaperCardImage
                if showcardwin == 'S':
                    self.cardwinimage = Images.ScissorsCardImage

        passed_time = 0
        self.cardwinscene=True
        while (self.cardwinscene):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.backButton.get_event(event)
            self.backButton.renderTxt(GameGUI.gameDisplay)
            
            if self.click_time != 0:
                passed_time = (pygame.time.get_ticks()-self.click_time) / 1000
                GameGUI.gameDisplay.fill(Colors.black)
                
                if passed_time >= 1:
                    if showcardwin == '':
                        GameGUI.gameDisplay.blit(self.cardwinimage, ((GameGUI.display_width-740)/2, (GameGUI.display_height-370)/2))
                    else:
                        GameGUI.gameDisplay.blit(self.cardwinimage, ((GameGUI.display_width-140)/2,(GameGUI.display_height-195)/2))
                    playerwinner.displayText()
                    
                if passed_time >=2:
                    self.cardwinscene = False

            pygame.display.update()
            GameGUI.clock.tick(15)

    def displayaftertime(self, surfobj, resettime=0, loop=False,interval=True, action=''):
        if loop==True:
            intrvl=resettime
            
            for obj in surfobj:
                if self.counter >= intrvl:
                    obj.displayText()
        
                intrvl+=1
            
        # else:
        #     intrvl=resettime
        #     if self.counter>= intrvl:
        #         action()
        #can add other possibilities here

    def winScene(self, playerwinner):
        GameGUI.gameDisplay.fill(Colors.black)

        time_delay = 80 # 0.5 seconds
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event , time_delay )
        self.counter = 1
        self.music.playtypeeffect()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == timer_event:
                    self.counter+=1
                    
                self.backButton.get_event(event)
                
            self.backButton.renderTxt(GameGUI.gameDisplay)
            
            self.displayaftertime(playerwinner, resettime=0, loop=True)
            # counter time is hardcoded here
            if self.counter ==65:
                self.music.stopmusic()
            pygame.display.update()
            GameGUI.clock.tick(15)
            
game = Game()
game.run()