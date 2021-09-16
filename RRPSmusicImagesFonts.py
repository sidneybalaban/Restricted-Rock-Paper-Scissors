import pygame
pygame.init()

class Images:
    # AkagiVsKaiji=pygame.image.load(r'AkagiVsKaiji.jpg')
    AkagiVsKaiji=pygame.image.load(r'AkagiVsKaijiLarge.jpg')
    ChairmanHappy = pygame.image.load(r'ChairmanHappy400wh622h.jpg')   
    kaijiupset = pygame.image.load(r'kaijiCrying740w370h.jpg')
    akaginormal = pygame.image.load(r'akagiSmile740w370h.jpg')
    Tonegawa = pygame.image.load(r'Tonegawa740w370h.jpg')
    
    
    RockImageintro = pygame.image.load(r'PlainRockImage70w98hQuit.jpg')
    PaperImageintro = pygame.image.load(r'PlainPaperImage70w98hStart.jpg')
    ScissorsImageIntro = pygame.image.load(r'PlainScissorsImage70w98h.jpg')
    
    RockCardImage = pygame.image.load(r'RockCard140w195h.jpg')
    PaperCardImage = pygame.image.load(r'PaperCard140w195h.jpg')
    ScissorsCardImage = pygame.image.load(r'ScissorsCard140w195h.jpg')
    
    cardsPicTransition = pygame.image.load(r'cardsPicTransition960w550h.jpg')
    
   
    
class Music:
    def __init__(self):
        self.ZawaIntro = r'youtubeZawa.wav'
        self.typingsounds = r'DigitalTypingSoundEffect.wav'
    def playmusic(self):
        pygame.mixer.music.load(self.ZawaIntro)
        pygame.mixer.music.play(-1)
        
    def playtypeeffect(self):
        pygame.mixer.music.load(self.typingsounds)
        pygame.mixer.music.play(-1)
    def stopmusic(self):
        pygame.mixer.music.stop()
    def pausemusic(self):
        pygame.mixer.music.pause()
    def unpausemusic(self):
        pygame.mixer.music.unpause()

class Fonts:
    karmaticArcadefont = r"ka1.ttf"
    amaticBoldfont = r"Amatic-Bold.ttf"

class Font(Fonts):
    def __init__(self, fontLocation, wordsSize):
        self.fontLocation = fontLocation
        self.wordsFont = pygame.font.Font(fontLocation,wordsSize)
    def __str__(self):
        return self.fontLocation