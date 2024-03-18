import random
from enum import Enum


class Suit(Enum):
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    CLUBS = 'Clubs'
    SPADES = 'Spades'


class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class CardDeck:
    def __init__(self, deck):
        self.deck = deck

    def shuffle_deck(self):
        """Shuffle the deck of cards."""
        random.shuffle(self.deck)

    def print_deck(self):
        """Print the sorted deck of cards."""
        for card in self.deck:
            print(f"{Rank(card[0]).name} of {Suit(card[1]).name}")


deck = CardDeck([(rank.value, suit.value) for suit in Suit for rank in Rank])
