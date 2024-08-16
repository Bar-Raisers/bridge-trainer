from typing import Any, Dict

from dealing.enums import FilterType
from dealing.filters import AndFilter, DealFilter, NotFilter, OrFilter
from dealing.resources.criteria.distribution import parse_distribution_criteria
from dealing.resources.criteria.high_card_points import parse_high_card_points_criteria
from dealing.resources.criteria.suit_length import parse_suit_length_criteria


def parse_and_criteria(attributes: Dict[str, Any]) -> AndFilter:
    subfilters = [parse_criteria(criteria) for criteria in attributes["filters"]]
    return AndFilter(filters=subfilters)


def parse_not_criteria(attributes: Dict[str, Any]) -> NotFilter:
    subfilter = parse_criteria(attributes["filter"])
    return NotFilter(filter=subfilter)


def parse_or_criteria(attributes: Dict[str, Any]) -> OrFilter:
    subfilters = [parse_criteria(criteria) for criteria in attributes["filters"]]
    return OrFilter(filters=subfilters)


def parse_criteria(attributes: Dict[str, Any]) -> DealFilter:
    parse_by_type = {
        FilterType.AND: parse_and_criteria,
        FilterType.DISTRIBUTION: parse_distribution_criteria,
        FilterType.HIGH_CARD_POINTS: parse_high_card_points_criteria,
        FilterType.NOT: parse_not_criteria,
        FilterType.OR: parse_or_criteria,
        FilterType.SUIT_LENGTH: parse_suit_length_criteria,
    }
    filter_type = FilterType(attributes["type"])
    return parse_by_type[filter_type](attributes)


__all__ = [
    "parse_and_criteria",
    "parse_criteria",
    "parse_distribution_criteria",
    "parse_high_card_points_criteria",
    "parse_or_criteria",
    "parse_suit_length_criteria",
]
