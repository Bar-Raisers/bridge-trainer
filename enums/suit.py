from __future__ import annotations
from enum import Enum


class Suit(Enum):

    SPADES = "spades"
    HEARTS = "hearts"
    DIAMONDS = "diamonds"
    CLUBS = "clubs"

    def __lt__(self, other: Suit) -> bool:
        if self.__class__ is not other.__class__:
            return NotImplemented
        
        members = list(self.__class__)
        return members.index(self) < members.index(other)

    def __str__(self) -> str:
        return self.symbol

    @property
    def symbol(self) -> str:
        suit_to_symbol_map = {
            Suit.SPADES: "S",
            Suit.HEARTS: "H",
            Suit.DIAMONDS: "D",
            Suit.CLUBS: "C",
        }
        return suit_to_symbol_map[self]

    @staticmethod
    def from_name(name: str) -> "Suit":
        return Suit(name)

    @staticmethod
    def from_symbol(symbol: str) -> "Suit":
        symbol_to_suit_map = {
            "S": Suit.SPADES,
            "H": Suit.HEARTS,
            "D": Suit.DIAMONDS,
            "C": Suit.CLUBS,
        }
        return symbol_to_suit_map[symbol]
