import unittest
from unittest import mock

from dealing.parsing import parse_filter


class ParsingTestCase(unittest.TestCase):

    @mock.patch("dealing.parsing.parse_high_card_points_filter")
    def test_parse_filter_with_high_card_points_filter(self, mock_filter):
        # Given
        attributes = {
            "type": "high_card_points",
        }

        # When
        parse_filter(attributes)

        # Then
        self.assertTrue(mock_filter.called)


if __name__ == "__main__":
    unittest.main()
