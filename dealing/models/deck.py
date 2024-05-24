from random import shuffle
from typing import List

from pydantic import BaseModel

from enums import Rank, Suit
from models import Card


class Deck(BaseModel):

    cards: List[Card]

    def draw(self) -> Card:
        return self.cards.pop(0)

    def is_empty(self) -> bool:
        return len(self.cards) == 0

    def shuffle(self) -> None:
        shuffle(self.cards)


class DeckFactory:

    @staticmethod
    def create_sorted_deck() -> Deck:
        cards = []

        for suit in list(Suit):
            for rank in list(Rank):
                cards.append(Card(rank=rank, suit=suit))

        return Deck(cards=cards)

    @classmethod
    def create_shuffled_deck(cls) -> Deck:
        deck = cls.create_sorted_deck()
        deck.shuffle()
        return deck
