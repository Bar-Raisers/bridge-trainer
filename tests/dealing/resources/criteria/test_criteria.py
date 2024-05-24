import unittest
from unittest import mock

from dealing.resources.criteria import parse_criteria


class ParseCriteriaTestCase(unittest.TestCase):

    @mock.patch("dealing.resources.criteria.parse_high_card_points_criteria")
    def test_parse_criteria_with_high_card_points_criteria(self, mock_filter):
        # Given
        attributes = {
            "type": "high_card_points",
            "seat": "north",
            "minimum": 10,
            "maximum": 15,
        }

        # When
        parse_criteria(attributes)

        # Then
        self.assertTrue(mock_filter.called)

    @mock.patch("dealing.resources.criteria.parse_suit_length_criteria")
    def test_parse_criteria_with_suit_length_criteria(self, mock_filter):
        # Given
        attributes = {
            "type": "suit_length",
            "seat": "north",
            "suit": "spades",
            "minimum": 5,
            "maximum": 5,
        }

        # When
        parse_criteria(attributes)

        # Then
        self.assertTrue(mock_filter.called)


if __name__ == "__main__":
    unittest.main()
