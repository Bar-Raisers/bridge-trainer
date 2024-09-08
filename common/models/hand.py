from typing import List, Optional

from pydantic import BaseModel

from common.models.card import Card


class Hand(BaseModel):

    cards: List[Card] = []

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cards = sorted(self.cards)

    def __str__(self) -> str:
        return ", ".join([str(card) for card in self.cards])
