import unittest
from typing import Hashable

from enums.seat import Seat


class SeatTestCase(unittest.TestCase):

    def test_is_hashable(self):
        # Given
        seat = Seat.NORTH

        # When
        seat_hash = hash(seat)
        is_hashable = isinstance(seat, Hashable)

        # Then
        self.assertTrue(is_hashable)
