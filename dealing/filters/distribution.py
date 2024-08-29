from common.constants.distribution import BALANCED_DISTRIBUTIONS
from common.enums import Seat
from common.models import Deal, Distribution
from common.utilities.hand import get_distribution
from dealing.filters.base import DealFilter


class BalancedFilter(DealFilter):

    def __init__(
        self,
        seat: Seat,
    ) -> None:
        self.seat = seat

    def evaluate(self, deal: Deal) -> bool:
        hand = deal.get_hand(self.seat)
        distribution = get_distribution(hand)

        for d in BALANCED_DISTRIBUTIONS:
            if d.matches(distribution):
                return True

        return False


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


class BalancedFilter(DealFilter):

    BALANCED_DISTRIBUTIONS = [
        Distribution(distribution="5-3-3-2"),
        Distribution(distribution="4-4-3-2"),
        Distribution(distribution="4-3-3-3"),
    ]

    def __init__(
        self,
        seat: Seat,
    ) -> None:
        self.seat = seat

    def evaluate(self, deal: Deal) -> bool:
        hand = deal.get_hand(self.seat)
        distribution = get_distribution(hand)

        for balanced_distribution in self.BALANCED_DISTRIBUTIONS:
            if distribution.matches(balanced_distribution):
                return True

        return False
