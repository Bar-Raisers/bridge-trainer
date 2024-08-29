from typing import Any, Dict

from dealing.filters import BalancedFilter, DistributionFilter
from enums import Seat
from models import Distribution


def parse_balanced_distribution_criteria(
    attributes: Dict[str, Any]
) -> DistributionFilter:
    seat = Seat(attributes["seat"])
    return BalancedFilter(seat=seat)


def parse_distribution_criteria(attributes: Dict[str, Any]) -> DistributionFilter:
    seat = Seat(attributes["seat"])
    distribution = Distribution(distribution=attributes["distribution"])
    return DistributionFilter(
        seat=seat,
        distribution=distribution,
    )
