from typing import List, Optional

from pydantic import BaseModel, field_validator

from common.models.card import Card


class Holding(BaseModel):

    cards: List[Card] = []

    def __init__(self, cards: Optional[List[Card]] = None) -> None:
        super().__init__(cards=cards)
        self.cards = sorted(self.cards)

    def __str__(self) -> str:
        return "".join([card.rank.symbol for card in self.cards])

    @property
    def length(self) -> int:
        return len(self.cards)

    @field_validator("cards")
    @classmethod
    def validate_cards_have_same_suit(cls, cards: List[Card]) -> List[Card]:
        if not cards:
            return []

        expected_suit = cards[0].suit
        for card in cards:
            if card.suit != expected_suit:
                raise ValueError("holdings must contain cards with the same suit")

        return cards
