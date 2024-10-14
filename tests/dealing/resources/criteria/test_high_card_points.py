import unittest

from common.enums import Seat
from dealing.filters import HighCardPointsFilter
from dealing.resources.criteria import parse_high_card_points_criteria


class ParseHighCardPointsCriteriaTestCase(unittest.TestCase):

    def test_parse_high_card_points_criteria(self):
        # Given
        seat = Seat.NORTH
        minimum_high_card_points = 15
        maximum_high_card_points = 17
        attributes = {
            "type": "high_card_points",
            "seat": seat.value,
            "minimum": minimum_high_card_points,
            "maximum": maximum_high_card_points,
        }

        # When
        filter = parse_high_card_points_criteria(attributes)

        # Then
        self.assertIsInstance(filter, HighCardPointsFilter)
        self.assertEqual(seat, filter.seat)
        self.assertEqual(minimum_high_card_points, filter.minimum_high_card_points)
        self.assertEqual(maximum_high_card_points, filter.maximum_high_card_points)
