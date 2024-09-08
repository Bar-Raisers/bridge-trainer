from common.enums import Seat
from dealing.filters.base import DealFilter
from models import Deal
from utilities.hand import calculate_high_card_points


class HighCardPointsFilter(DealFilter):

    def __init__(
        self,
        seat: Seat,
        minimum_high_card_points: int,
        maximum_high_card_points: int,
    ) -> None:
        self.seat = seat
        self.minimum_high_card_points = minimum_high_card_points
        self.maximum_high_card_points = maximum_high_card_points

    def evaluate(self, deal: Deal) -> bool:
        hand = deal.get_hand(self.seat)
        high_card_points = calculate_high_card_points(hand)

        if high_card_points < self.minimum_high_card_points:
            return False
        if high_card_points > self.maximum_high_card_points:
            return False

        return True
