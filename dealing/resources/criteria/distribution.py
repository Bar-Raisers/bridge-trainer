from typing import Any, Dict

from common.enums import Seat
from common.models import Distribution
from dealing.filters import BalancedFilter, DistributionFilter


def parse_balanced_criteria(attributes: Dict[str, Any]) -> BalancedFilter:
    seat = Seat(attributes["seat"])
    return BalancedFilter(seat=seat)


def parse_distribution_criteria(attributes: Dict[str, Any]) -> DistributionFilter:
    seat = Seat(attributes["seat"])
    distribution = Distribution(distribution=attributes["distribution"])
    return DistributionFilter(
        seat=seat,
        distribution=distribution,
    )
