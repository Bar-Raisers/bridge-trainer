import unittest

from pydantic import ValidationError

from common.enums import Rank, Suit
from models import Card, Holding


class HoldingTestCase(unittest.TestCase):

    def test_constructor_with_unsorted_hand(self):
        # Given
        ace_spades = Card(rank=Rank.ACE, suit=Suit.SPADES)
        queen_spades = Card(rank=Rank.QUEEN, suit=Suit.SPADES)
        ten_spades = Card(rank=Rank.TEN, suit=Suit.SPADES)

        unsorted_cards = [ten_spades, ace_spades, queen_spades]
        sorted_cards = [ace_spades, queen_spades, ten_spades]

        # When
        holding = Holding(cards=unsorted_cards)

        # Then
        self.assertListEqual(sorted_cards, holding.cards)

    def test_length_property(self):
        # Given
        holding = Holding(
            cards=[
                Card(rank=Rank.ACE, suit=Suit.SPADES),
                Card(rank=Rank.QUEEN, suit=Suit.SPADES),
                Card(rank=Rank.TEN, suit=Suit.SPADES),
            ],
        )
        expected_length = 3

        # When
        length = holding.length

        # Then
        self.assertEqual(expected_length, length)

    def test_length_property_with_void(self):
        # Given
        holding = Holding(cards=[])
        expected_length = 0

        # When
        length = holding.length

        # Then
        self.assertEqual(expected_length, length)

    def test_str_with_void(self):
        # Given
        holding = Holding(cards=[])
        expected_string = ""

        # When
        string = str(holding)

        # Then
        self.assertEqual(expected_string, string)

    def test_str_with_singleton(self):
        # Given
        holding = Holding(cards=[Card(rank=Rank.QUEEN, suit=Suit.SPADES)])
        expected_string = "Q"

        # When
        string = str(holding)

        # Then
        self.assertEqual(expected_string, string)

    def test_str_with_multiple_cards(self):
        # Given
        holding = Holding(
            cards=[
                Card(rank=Rank.ACE, suit=Suit.SPADES),
                Card(rank=Rank.QUEEN, suit=Suit.SPADES),
                Card(rank=Rank.TEN, suit=Suit.SPADES),
            ]
        )
        expected_string = "AQT"

        # When
        string = str(holding)

        # Then
        self.assertEqual(expected_string, string)

    def test_validate_cards_have_same_suit_with_identical_suits(self):
        # Given
        cards = [
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
        ]

        # When
        holding = Holding(cards=cards)

        # Then: Holding instance is created without error.
        self.assertIsInstance(holding, Holding)

    def test_validate_cards_have_same_suit_with_different_suits(self):
        # Given
        cards = [
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
        ]

        # When & Then
        with self.assertRaises(ValidationError):
            Holding(cards=cards)


if __name__ == "__main__":
    unittest.main()
