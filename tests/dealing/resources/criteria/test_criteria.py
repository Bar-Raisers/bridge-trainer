import unittest
from unittest import mock

from dealing.resources.criteria import parse_criteria


class ParseCriteriaTestCase(unittest.TestCase):

    @mock.patch("dealing.resources.criteria.parse_high_card_points_criteria")
    def test_parse_criteria_with_high_card_points_criteria(self, mock_filter):
        # Given
        attributes = {
            "type": "high_card_points",
        }

        # When
        parse_criteria(attributes)

        # Then
        self.assertTrue(mock_filter.called)


if __name__ == "__main__":
    unittest.main()
