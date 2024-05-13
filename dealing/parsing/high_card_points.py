from typing import Any, Dict

from dealing.filters.high_card_points import HighCardPointsFilter
from enums.seat import Seat


def parse_high_card_points_filter(attributes: Dict[str, Any]) -> HighCardPointsFilter:
    seat = Seat(attributes["seat"])
    minimum_high_card_points = attributes["minimum"]
    maximum_high_card_points = attributes["maximum"]

    return HighCardPointsFilter(
        seat=seat,
        minimum_high_card_points=minimum_high_card_points,
        maximum_high_card_points=maximum_high_card_points,
    )
