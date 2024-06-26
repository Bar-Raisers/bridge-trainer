from dealing.filters.base import DealFilter
from enums import Seat
from models import Deal, Distribution
from utilities.hand import get_distribution


class DistributionFilter(DealFilter):

    def __init__(
        self,
        seat: Seat,
        distribution: Distribution,
    ) -> None:
        self.seat = seat
        self.distribution = distribution

    def evaluate(self, deal: Deal) -> bool:
        hand = deal.get_hand(self.seat)
        distribution = get_distribution(hand)
        return self.distribution.matches(distribution)
