from typing import Any, Dict

from dealing.filters import SuitLengthFilter
from enums import Seat, Suit


def parse_suit_length_criteria(attributes: Dict[str, Any]) -> SuitLengthFilter:
    seat = Seat(attributes["seat"])
    suit = Suit(attributes["suit"])
    minimum_suit_length = attributes["minimum"]
    maximum_suit_length = attributes["maximum"]
    return SuitLengthFilter(
        seat=seat,
        suit=suit,
        minimum_suit_length=minimum_suit_length,
        maximum_suit_length=maximum_suit_length,
    )
