import json
from typing import Any, Dict

from dealing.enums.filters import FilterType
from dealing.filters import DealFilter
from dealing.resources.criteria.high_card_points import parse_high_card_points_criteria


def load_criteria_from_json_file(json_file_path: str) -> Dict[str, Any]:
    with open(json_file_path) as json_file:
        return json.load(json_file)


def parse_criteria(attributes: Dict[str, Any]) -> DealFilter:
    parse_by_type = {
        FilterType.HIGH_CARD_POINTS: parse_high_card_points_criteria,
    }
    filter_type = FilterType(attributes["type"])
    return parse_by_type[filter_type](attributes)
