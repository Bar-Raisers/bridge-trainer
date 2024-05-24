import unittest

from enums import Rank, Suit
from models import Card, Hand, Holding
from utilities.hand.holding import get_holding_in_suit


class HoldingTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create Hand with 0-1-5-6 Distribution.
        cls.hand = Hand(
            cards=[
                # 1 Heart
                Card(rank=Rank.ACE, suit=Suit.HEARTS),
                # 5 Diamonds
                Card(rank=Rank.ACE, suit=Suit.DIAMONDS),
                Card(rank=Rank.KING, suit=Suit.DIAMONDS),
                Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
                Card(rank=Rank.JACK, suit=Suit.DIAMONDS),
                Card(rank=Rank.TEN, suit=Suit.DIAMONDS),
                # 6 Clubs
                Card(rank=Rank.ACE, suit=Suit.CLUBS),
                Card(rank=Rank.KING, suit=Suit.CLUBS),
                Card(rank=Rank.QUEEN, suit=Suit.CLUBS),
                Card(rank=Rank.JACK, suit=Suit.CLUBS),
                Card(rank=Rank.TEN, suit=Suit.CLUBS),
                Card(rank=Rank.NINE, suit=Suit.CLUBS),
            ],
        )

    def test_get_holding_in_suit_with_void(self):
        # Given: Hand constructed in setUpClass()
        hand = self.hand
        expected_spade_holding = Holding(cards=[])

        # When
        holding = get_holding_in_suit(hand, Suit.SPADES)

        # Then
        self.assertListEqual(expected_spade_holding.cards, holding.cards)

    def test_get_holding_in_suit_with_singleton(self):
        # Given: Hand constructed in setUpClass()
        hand = self.hand
        expected_heart_holding = Holding(
            cards=[
                Card(rank=Rank.ACE, suit=Suit.HEARTS),
            ],
        )

        # When
        holding = get_holding_in_suit(hand, Suit.HEARTS)

        # Then
        self.assertListEqual(expected_heart_holding.cards, holding.cards)

    def test_get_holding_in_suit_with_multiple_cards(self):
        # Given: Hand constructed in setUpClass()
        hand = self.hand
        expected_diamond_holding = Holding(
            cards=[
                Card(rank=Rank.ACE, suit=Suit.DIAMONDS),
                Card(rank=Rank.KING, suit=Suit.DIAMONDS),
                Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
                Card(rank=Rank.JACK, suit=Suit.DIAMONDS),
                Card(rank=Rank.TEN, suit=Suit.DIAMONDS),
            ],
        )

        # When
        holding = get_holding_in_suit(hand, Suit.DIAMONDS)

        # Then
        self.assertListEqual(expected_diamond_holding.cards, holding.cards)


if __name__ == "__main__":
    unittest.main()
