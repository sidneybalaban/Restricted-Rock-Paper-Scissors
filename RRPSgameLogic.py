class Player:
    def __init__(self, score, computerplayer=False):
        self.score = str(score)
        self.computerplayer = computerplayer
        
    def addPoint(self):
        self.score = str(int(self.score)+1)
       
    def removePoint(self):
        self.score = str(int(self.score)-1)
    
    def chosenCard(self, card):
        self.card = card
    
    def addDeck(self, deck):
        if(not hasattr(self, 'deck')):
            self.deck = deck
    
    def cardTotals(self):
        self.cardtotals = {'Rock total': '0', 'Paper total': '0', 'Scissors total': '0'}
        for i in self.deck.cards:
            if i == CardName.ROCK:
                self.cardtotals['Rock total'] =  str(int(self.cardtotals['Rock total'])+1)
            if i == CardName.PAPER:
                self.cardtotals['Paper total'] =  str(int(self.cardtotals['Paper total'])+1)
            if i == CardName.SCISSORS:
                self.cardtotals['Scissors total'] =  str(int(self.cardtotals['Scissors total'])+1)
        return self.cardtotals
    
    def chosenAndRemoveCard(self, card):
        self.chosenCard(card)
        self.deck.removeCard(card)
    
    def __str__(self):
        return f'Player has score: {self.score} with {self.cardTotals()}'
        
    
class Deck:
    def __init__(self, cards=[]):
        self.cards = cards
        
    def getCards(self):
        return self.cards
        
    def addCard(self, card):
        self.cards.append(card)
        
    def removeCard(self, card):
        self.cards.remove(card)

    def __str__(self):
        return "cards: " + ", ".join([str(card) for card in self.cards])

class Card:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
    
    def __str__(self):
        return f'{self.name}'
    
    def __lt__(self, other):
        return self.name < other.name
    
from enum import Enum    
class CardName(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3