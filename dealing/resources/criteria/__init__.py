from typing import Any, Dict

from dealing.enums import FilterType
from dealing.filters import DealFilter
from dealing.resources.criteria.distribution import parse_distribution_criteria
from dealing.resources.criteria.high_card_points import parse_high_card_points_criteria
from dealing.resources.criteria.suit_length import parse_suit_length_criteria


def parse_criteria(attributes: Dict[str, Any]) -> DealFilter:
    parse_by_type = {
        FilterType.DISTRIBUTION: parse_distribution_criteria,
        FilterType.HIGH_CARD_POINTS: parse_high_card_points_criteria,
        FilterType.SUIT_LENGTH: parse_suit_length_criteria,
    }
    filter_type = FilterType(attributes["type"])
    return parse_by_type[filter_type](attributes)


__all__ = [
    "parse_criteria",
    "parse_distribution_criteria",
    "parse_high_card_points_criteria",
    "parse_suit_length_criteria",
]
