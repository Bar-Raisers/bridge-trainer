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
        representation = {
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
        return representation[self]
