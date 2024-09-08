from typing import Any, Dict

from common.enums import Seat
from dealing.filters import DistributionFilter
from models import Distribution


def parse_distribution_criteria(attributes: Dict[str, Any]) -> DistributionFilter:
    seat = Seat(attributes["seat"])
    distribution = Distribution(distribution=attributes["distribution"])
    return DistributionFilter(
        seat=seat,
        distribution=distribution,
    )
