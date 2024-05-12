from typing import List

from dealing.engine.base import DealEngine
from dealing.models.deck import DeckFactory
from models.deal import Deal
from models.hand import Hand


class BruteForceDealEngine(DealEngine):

    def _generate_deal(self, board_number: int) -> Deal:
        deck = DeckFactory.create_shuffled_deck()
        north = Hand(cards=[deck.draw() for _ in range(13)])
        east = Hand(cards=[deck.draw() for _ in range(13)])
        south = Hand(cards=[deck.draw() for _ in range(13)])
        west = Hand(cards=[deck.draw() for _ in range(13)])

        return Deal(
            board_number=board_number,
            north=north,
            east=east,
            south=south,
            west=west,
        )
