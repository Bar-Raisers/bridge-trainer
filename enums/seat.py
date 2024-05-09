from __future__ import annotations

from enum import Enum


class Seat(Enum):

    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"

    def __hash__(self) -> int:
        return hash(self.value)

    @classmethod
    def get_dealer_seat_from_board_number(cls, board_number: int) -> Seat:
        return list(cls)[(board_number - 1) % 4]
