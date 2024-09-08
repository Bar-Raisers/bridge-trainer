from common.enums import Seat, Suit
from dealing.filters.base import DealFilter
from models import Deal
from utilities.hand import get_holding_in_suit


class SuitLengthFilter(DealFilter):

    def __init__(
        self,
        seat: Seat,
        suit: Suit,
        minimum_suit_length: int,
        maximum_suit_length: int,
    ) -> None:
        self.seat = seat
        self.suit = suit
        self.minimum_suit_length = minimum_suit_length
        self.maximum_suit_length = maximum_suit_length

    def evaluate(self, deal: Deal) -> bool:
        hand = deal.get_hand(self.seat)
        holding = get_holding_in_suit(hand, self.suit)

        if holding.length < self.minimum_suit_length:
            return False
        if holding.length > self.maximum_suit_length:
            return False

        return True
