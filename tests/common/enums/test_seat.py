import unittest
from typing import Hashable

from common.enums import Seat


class SeatTestCase(unittest.TestCase):

    def test_is_hashable(self):
        # Given
        seat = Seat.NORTH

        # When
        seat_hash = hash(seat)
        is_hashable = isinstance(seat, Hashable)

        # Then
        self.assertTrue(is_hashable)

    def test_get_dealer_seat_from_board_number(self):
        # Given
        dealer_by_board_number = {
            1: Seat.NORTH,
            2: Seat.EAST,
            3: Seat.SOUTH,
            4: Seat.WEST,
            5: Seat.NORTH,
            6: Seat.EAST,
            7: Seat.SOUTH,
            8: Seat.WEST,
        }

        # When & Then
        for board_number, expected_dealer in dealer_by_board_number.items():
            dealer = Seat.get_dealer_seat_from_board_number(board_number)
            self.assertEqual(expected_dealer, dealer)
