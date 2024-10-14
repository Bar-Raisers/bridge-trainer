import unittest

from dealing.filters import (
    AndFilter,
    HighCardPointsFilter,
    NotFilter,
    OrFilter,
    SuitLengthFilter,
)
from dealing.resources.criteria import (
    parse_and_criteria,
    parse_not_criteria,
    parse_or_criteria,
)


class ParseAndCriteriaTestCase(unittest.TestCase):

    def test_parse_and_criteria(self):
        # Given
        attributes = {
            "type": "and",
            "filters": [
                {
                    "type": "high_card_points",
                    "seat": "north",
                    "minimum": 10,
                    "maximum": 10,
                },
                {
                    "type": "suit_length",
                    "seat": "north",
                    "suit": "spades",
                    "minimum": 4,
                    "maximum": 5,
                },
            ],
        }

        # When
        filter = parse_and_criteria(attributes)

        # Then
        self.assertIsInstance(filter, AndFilter)
        self.assertEqual(2, len(filter.filters))
        self.assertIsInstance(filter.filters[0], HighCardPointsFilter)
        self.assertIsInstance(filter.filters[1], SuitLengthFilter)


class ParseNotCriteriaTestCase(unittest.TestCase):

    def test_parse_not_criteria(self):
        # Given
        attributes = {
            "type": "not",
            "filter": {
                "type": "high_card_points",
                "seat": "north",
                "minimum": 10,
                "maximum": 10,
            },
        }

        # When
        filter = parse_not_criteria(attributes)

        # Then
        self.assertIsInstance(filter, NotFilter)
        self.assertIsInstance(filter.filter, HighCardPointsFilter)


class ParseOrCriteriaTestCase(unittest.TestCase):

    def test_parse_or_criteria(self):
        # Given
        attributes = {
            "type": "or",
            "filters": [
                {
                    "type": "high_card_points",
                    "seat": "north",
                    "minimum": 10,
                    "maximum": 10,
                },
                {
                    "type": "suit_length",
                    "seat": "north",
                    "suit": "spades",
                    "minimum": 4,
                    "maximum": 5,
                },
            ],
        }

        # When
        filter = parse_or_criteria(attributes)

        # Then
        self.assertIsInstance(filter, OrFilter)
        self.assertEqual(2, len(filter.filters))
        self.assertIsInstance(filter.filters[0], HighCardPointsFilter)
        self.assertIsInstance(filter.filters[1], SuitLengthFilter)
