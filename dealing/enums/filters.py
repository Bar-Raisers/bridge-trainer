from enum import Enum


class FilterType(Enum):

    HIGH_CARD_POINTS = "high_card_points"

    def __hash__(self) -> int:
        return hash(self.value)

    def __str__(self) -> str:
        return self.value
