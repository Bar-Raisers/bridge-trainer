from typing import Any, Dict

from dealing.enums.filters import FilterType
from dealing.filters import DealFilter
from dealing.parsing.high_card_points import parse_high_card_points_filter


def parse_filter(attributes: Dict[str, Any]) -> DealFilter:
    parse_by_type = {
        FilterType.HIGH_CARD_POINTS: parse_high_card_points_filter,
    }
    filter_type = FilterType(attributes["type"])
    return parse_by_type[filter_type](attributes)
