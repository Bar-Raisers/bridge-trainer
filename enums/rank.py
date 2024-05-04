from enum import IntEnum


class Rank(IntEnum):

    ACE = 0
    KING = 1
    QUEEN = 2
    JACK = 3
    TEN = 4
    NINE = 5
    EIGHT = 6
    SEVEN = 7
    SIX = 8
    FIVE = 9
    FOUR = 10
    THREE = 11
    TWO = 12

    def __str__(self) -> str:
        return self.symbol

    @property
    def symbol(self) -> str:
        rank_to_symbol_map = {
            Rank.ACE: "A",
            Rank.KING: "K",
            Rank.QUEEN: "Q",
            Rank.JACK: "J",
            Rank.TEN: "T",
            Rank.NINE: "9",
            Rank.EIGHT: "8",
            Rank.SEVEN: "7",
            Rank.SIX: "6",
            Rank.FIVE: "5",
            Rank.FOUR: "4",
            Rank.THREE: "3",
            Rank.TWO: "2",
        }
        return rank_to_symbol_map[self]

    @staticmethod
    def from_symbol(symbol: str) -> "Rank":
        symbol_to_rank_map = {
            "A": Rank.ACE,
            "K": Rank.KING,
            "Q": Rank.QUEEN,
            "J": Rank.JACK,
            "T": Rank.TEN,
            "9": Rank.NINE,
            "8": Rank.EIGHT,
            "7": Rank.SEVEN,
            "6": Rank.SIX,
            "5": Rank.FIVE,
            "4": Rank.FOUR,
            "3": Rank.THREE,
            "2": Rank.TWO,
        }
        return symbol_to_rank_map[symbol]
