from common.enums import Seat
from common.models import Deal
from common.utilities.hand import calculate_high_card_points
from dealing.filters.base import DealFilter


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
