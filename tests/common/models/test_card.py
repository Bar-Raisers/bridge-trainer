import unittest

from common.enums import Rank, Suit
from common.models import Card


class CardTestCase(unittest.TestCase):

    def test_equal_comparison(self):
        # Given
        card_one = Card(rank=Rank.ACE, suit=Suit.SPADES)
        card_two = Card(rank=Rank.ACE, suit=Suit.SPADES)

        # When
        comparison = card_one == card_two

        # Then
        self.assertTrue(comparison)

    def test_not_equal_comparison(self):
        # Given
        card_one = Card(rank=Rank.ACE, suit=Suit.SPADES)
        card_two = Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS)

        # When
        comparison = card_one != card_two

        # Then
        self.assertTrue(comparison)

    def test_less_than_comparison(self):
        # Given
        lesser = Card(rank=Rank.ACE, suit=Suit.SPADES)
        greater = Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS)

        # When
        comparison = lesser < greater

        # Then
        self.assertTrue(comparison)

    def test_greater_than_comparison(self):
        # Given
        lesser = Card(rank=Rank.ACE, suit=Suit.SPADES)
        greater = Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS)

        # When
        comparison = greater > lesser

        # Then
        self.assertTrue(comparison)

    def test_str(self):
        # Given
        card = Card(rank=Rank.ACE, suit=Suit.SPADES)
        expected_string = "AS"

        # When
        string = str(card)

        # Then
        self.assertEqual(expected_string, string)
