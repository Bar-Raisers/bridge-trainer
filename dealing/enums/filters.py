from enum import Enum


class FilterType(Enum):
    AND = "and"
    DISTRIBUTION = "distribution"
    HIGH_CARD_POINTS = "high_card_points"
    SUIT_LENGTH = "suit_length"

    def __hash__(self) -> int:
        return hash(self.value)

    def __str__(self) -> str:
        return self.value
