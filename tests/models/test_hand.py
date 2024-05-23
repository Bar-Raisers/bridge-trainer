import unittest

from enums.rank import Rank
from enums.suit import Suit
from models.card import Card
from models.hand import Hand


class HandTestCase(unittest.TestCase):

    def test_constructor_with_unsorted_hand(self):
        # Given
        ace_spades = Card(rank=Rank.ACE, suit=Suit.SPADES)
        queen_spades = Card(rank=Rank.QUEEN, suit=Suit.SPADES)
        ten_spades = Card(rank=Rank.TEN, suit=Suit.SPADES)

        unsorted_cards = [ten_spades, ace_spades, queen_spades]
        sorted_cards = [ace_spades, queen_spades, ten_spades]

        # When
        hand = Hand(cards=unsorted_cards)

        # Then
        self.assertListEqual(sorted_cards, hand.cards)

    def test_str(self):
        # Given
        hand = Hand(
            cards=[
                Card(rank=Rank.ACE, suit=Suit.SPADES),
                Card(rank=Rank.QUEEN, suit=Suit.SPADES),
                Card(rank=Rank.TEN, suit=Suit.SPADES),
            ]
        )
        expected_string = "AS, QS, TS"

        # When
        string = str(hand)

        # Then
        self.assertEqual(expected_string, string)


if __name__ == "__main__":
    unittest.main()
