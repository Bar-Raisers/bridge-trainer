from __future__ import annotations

from pydantic import BaseModel

from enums.rank import Rank
from enums.suit import Suit


class Card(BaseModel):

    rank: Rank
    suit: Suit

    def __eq__(self, other: Card) -> bool:
        if self.__class__ is not other.__class__:
            return NotImplemented

        return self.rank == other.rank and self.suit == other.suit

    def __hash__(self) -> int:
        return hash(str(self.rank) + str(self.suit))

    def __lt__(self, other: Card) -> bool:
        if self.__class__ is not other.__class__:
            return NotImplemented

        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False

        return self.rank < other.rank

    def __str__(self) -> str:
        return f"{self.rank.symbol}{self.suit.symbol}"
