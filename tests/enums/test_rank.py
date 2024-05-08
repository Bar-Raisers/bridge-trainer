import unittest

from enums.rank import Rank


class RankTestCase(unittest.TestCase):

    def test_less_than_comparison(self):
        # Given
        lesser = Rank.ACE
        greater = Rank.KING

        # When
        comparison = lesser < greater

        # Then
        self.assertTrue(comparison)

    def test_greater_than_comparison(self):
        # Given
        lesser = Rank.ACE
        greater = Rank.KING

        # When
        comparison = greater > lesser

        # Then
        self.assertTrue(comparison)

    def test_symbol_property(self):
        # Given
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

        # When & Then
        for rank, expected_symbol in rank_to_symbol_map.items():
            symbol = rank.symbol
            self.assertEqual(expected_symbol, symbol)

    def test_rank_from_symbol(self):
        # Given
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

        # When & Then
        for symbol, expected_rank in symbol_to_rank_map.items():
            rank = Rank.from_symbol(symbol)
            self.assertEqual(expected_rank, rank)


if __name__ == "__main__":
    unittest.main()
