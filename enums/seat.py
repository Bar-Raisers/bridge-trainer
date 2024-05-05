from enum import Enum


class Seat(Enum):

    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"

    def __hash__(self) -> int:
        return hash(self.value)
