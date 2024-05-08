from __future__ import annotations

from enum import Enum


class Rank(Enum):

    ACE = "A"
    KING = "K"
    QUEEN = "Q"
    JACK = "J"
    TEN = "T"
    NINE = "9"
    EIGHT = "8"
    SEVEN = "7"
    SIX = "6"
    FIVE = "5"
    FOUR = "4"
    THREE = "3"
    TWO = "2"

    def __lt__(self, other: Rank) -> bool:
        if self.__class__ is not other.__class__:
            return NotImplemented

        members = list(self.__class__)
        return members.index(self) < members.index(other)

    @property
    def symbol(self) -> str:
        return self.value

    @staticmethod
    def from_symbol(symbol: str) -> Rank:
        return Rank(symbol)
