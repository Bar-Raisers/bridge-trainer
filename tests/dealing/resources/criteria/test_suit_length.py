import unittest

from common.enums import Seat, Suit
from dealing.filters import SuitLengthFilter
from dealing.resources.criteria import parse_suit_length_criteria


class ParseSuitLengthCriteriaTestCase(unittest.TestCase):

    def test_parse_suit_length_criteria(self):
        # Given
        seat = Seat.NORTH
        suit = Suit.SPADES
        minimum_suit_length = 5
        maximum_suit_length = 5

        attributes = {
            "type": "suit_length",
            "seat": seat.value,
            "suit": suit.value,
            "minimum": minimum_suit_length,
            "maximum": maximum_suit_length,
        }

        # When
        filter = parse_suit_length_criteria(attributes)

        # Then
        self.assertIsInstance(filter, SuitLengthFilter)
        self.assertEqual(seat, filter.seat)
        self.assertEqual(suit, filter.suit)
        self.assertEqual(minimum_suit_length, filter.minimum_suit_length)
        self.assertEqual(maximum_suit_length, filter.maximum_suit_length)
