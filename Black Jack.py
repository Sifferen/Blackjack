from enum import Enum
from enum import IntEnum
from random import *

Fulldeck = []

Partialdeck = []


class Card(IntEnum):
    Two = 2
    Three =3
    Four = 4
    Five = 5 
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

class Suit(Enum):
    Spades = "Spades"
    Hearts = "Hearts"
    Clubs = "Clubs"
    Diamonds = "Diamonds"

class Playingcard():
    def __init__(self,cardvalue,cardsuit):
        self.card = cardvalue 
        self.suit = cardsuit


def createdeck():
    for suit in Suit:
        for card in Card:
            Fulldeck.append(Playingcard(Card(card),Suit(suit)))

    return Fulldeck

def drawcard(deck):
    randcard = randint(0,len(deck)-1)
    return deck.pop(randcard)
    



