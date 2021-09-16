import pygame

class GameGUI:
    
    display_width = 960
    display_height = 550
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    caption = pygame.display.set_caption('Restricted Rock Paper Scissors')
    clock = pygame.time.Clock()
    
class Mouse:
    mousePos = pygame.mouse.get_pos()
    

    
class Colors:
    black = (0,0,0)
    white = (255,255,255)
    red = (150,0,0)  
    brightRed = (255,0,0)
    green = (0,200,0)
    brightGreen = (0,255,0)
    blue = (0,0,150)
    brightBlue = (0,0,255)
    yellow = (255,255, 0)
    pink = (244,100,255)
    
class Fonts:
    karmaticArcadefont = r"ka1.ttf"
    amaticBoldfont = r"Amatic-Bold.ttf"

class Font(Fonts):
    def __init__(self, fontLocation, wordsSize):
        self.fontLocation = fontLocation
        self.wordsFont = pygame.font.Font(fontLocation,wordsSize)
    def __str__(self):
        return f'{self.fontLocation}'
                
class Text(Font, GameGUI):
    
    def __init__(self,color=Colors.red,fontLocation=Fonts.amaticBoldfont, wordsSize=50, 
            words='', x=0, y=0, rectPosition='center', bgColor=None
            ):
        Font.__init__(self, fontLocation, wordsSize)
        GameGUI.__init__(self)
        self.color = color
        self.x=x
        self.y=y
        self.words = f'{words}'
        self.rectPosition = rectPosition
        self.bgColor = bgColor
        
    def createText(self):
        self.wordsSurface = self.wordsFont.render(self.words, True, self.color, self.bgColor)
        return self.wordsSurface, self.wordsSurface.get_rect()
    
    def messageDisplay(self):
        self.TextSurf, self.TextRect = self.createText()
        return self.TextSurf, self.TextRect
    
    def centerTextRect(self):
        if self.rectPosition == 'center':
            self.TextRect.center = ((self.x),(self.y))
        if self.rectPosition == 'topleft':
            self.TextRect.topleft = ((self.x),(self.y))
        if self.rectPosition == 'topright':
            self.TextRect.topright = ((self.x),(self.y))
        
    def displayText(self):
        self.gameDisplay.blit(self.TextSurf, self.TextRect)
        
    def final(self):
        self.createText()
        self.messageDisplay()
        self.centerTextRect()

class MovingText:

    def wordsString(self, string):
        words = string
        return words
    
    def createtextlist(self, wordstring, wsize):
        textlist = [Text(wordsSize=wsize, fontLocation=Fonts.karmaticArcadefont) for i in range(len(wordstring))]
        return textlist
    
    def singlelinetext(self, textlist, wordsstring):
        nextletter = 0
        moveright = GameGUI.display_width/2 - 150
        for obj in textlist:
            obj.words = wordsstring[nextletter]
            nextletter +=1
            obj.y = GameGUI.display_height/2
            obj.x= moveright
            obj.final()
            moveright+=30
    
    def multilinetext(self, textlist, wordsstring):
        
        nextletter=0
        moveright = 100
        halfway=(int(len(wordsstring)/2))
            
        for obj in textlist:
            obj.words = wordsstring[nextletter]
            obj.y=150
            if nextletter==halfway:
                moveright = 100
            if nextletter>=halfway:
                nextletter+=1
                obj.x= moveright
                obj.y = 220
                obj.final()
                moveright+=24
            else:
                nextletter +=1
                obj.x= moveright
                obj.final()
                moveright+=24
                
    def linetextcomplete(self, string, multOrSing, wsize):
        words = self.wordsString(string)
        textlist = self.createtextlist(words, wsize)
        multOrSing(textlist, words)
        return textlist

class WaitForClick:
    def __init__(self):
        self.wait = False
    def true(self):
        self.wait = True
    def false(self):
        self.wait = False

waitforclick = WaitForClick()
class Button:
    def __init__(self, command, fontLocation='', wordsSize='', color='',  
            words='', bgColor=None, rect=(0,0,50,70), imageSurface=''
            ):
        self.rect = pygame.Rect(rect)
        self.imageSurface = imageSurface
        self.bgColor = bgColor
        self.words = words
        self.color = color
        self.command = command
        self.fontLocation = fontLocation
        self.wordsSize = wordsSize
        
        
    def renderImg(self, screen):
        screen.blit(self.imageSurface, self.rect)
        
    def renderTxt(self, screen):
        self.font = Font(self.fontLocation,self.wordsSize)
        self.wordsSurface = self.font.wordsFont.render(self.words, True, self.color,self.bgColor)
        screen.blit(self.wordsSurface, self.rect)
        
    def renderImgText(self,screen):
        self.renderImg(screen)
        self.renderTxt(screen)
        
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.command()
                waitforclick.false()
                

