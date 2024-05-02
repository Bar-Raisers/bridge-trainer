import unittest

from enums.rank import Rank


class RankTestCase(unittest.TestCase):

    def assert_rank_matches_str(self, rank: Rank, expected_string: str):
        # When
        rank_string = str(rank)

        # Then
        self.assertEqual(expected_string, rank_string)

    def test_str(self):
        # Given
        rank_to_string_map = {
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
        for rank, expected_string in rank_to_string_map.items():
            self.assert_rank_matches_str(rank, expected_string)


if __name__ == "__main__":
    unittest.main()
