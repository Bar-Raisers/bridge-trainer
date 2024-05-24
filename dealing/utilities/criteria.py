import json

from dealing.filters import DealFilter
from dealing.resources.criteria import parse_criteria


def parse_criteria_from_json_file(json_file_path: str) -> DealFilter:
    with open(json_file_path) as json_file:
        criteria_json = json.load(json_file)
        return parse_criteria(criteria_json)
