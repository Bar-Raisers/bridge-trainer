from __future__ import annotations
from typing import List

from pydantic import BaseModel

from models.card import Card


class Hand(BaseModel):

    cards: List[Card] = []

    def __init__(self, cards: Optional[List[Card]] = None) -> None:
        super().__init__(cards=cards)
        self.cards = sorted(self.cards)

    def __str__(self) -> str:
        return ", ".join(
            [
                str(card)
                for card in self.cards
            ]
        )
