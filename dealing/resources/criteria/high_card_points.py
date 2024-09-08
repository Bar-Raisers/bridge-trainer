from typing import Any, Dict

from common.enums import Seat
from dealing.filters import HighCardPointsFilter


def parse_high_card_points_criteria(attributes: Dict[str, Any]) -> HighCardPointsFilter:
    seat = Seat(attributes["seat"])
    minimum_high_card_points = attributes["minimum"]
    maximum_high_card_points = attributes["maximum"]
    return HighCardPointsFilter(
        seat=seat,
        minimum_high_card_points=minimum_high_card_points,
        maximum_high_card_points=maximum_high_card_points,
    )
