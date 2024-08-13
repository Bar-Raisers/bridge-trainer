import unittest

from dealing.filters import AndFilter, HighCardPointsFilter, SuitLengthFilter
from dealing.resources.criteria import parse_and_criteria


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


if __name__ == "__main__":
    unittest.main()
