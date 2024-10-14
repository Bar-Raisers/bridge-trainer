import unittest

from common.enums import Rank, Suit
from common.models import Card, Distribution, Hand, Holding
from common.tests.utilities import generate_hand_with_distribution
from common.utilities.hand.holding import get_holding_in_suit


class HoldingTestCase(unittest.TestCase):

    def test_get_holding_in_suit_with_void(self):
        # Given
        distribution = Distribution(distribution="0=1=5=7")
        hand = generate_hand_with_distribution(distribution)
        expected_spade_holding = Holding([])

        # When
        holding = get_holding_in_suit(hand, Suit.SPADES)

        # Then
        self.assertListEqual(expected_spade_holding.cards, holding.cards)

    def test_get_holding_in_suit_with_singleton(self):
        # Given
        distribution = Distribution(distribution="0=1=5=7")
        hand = generate_hand_with_distribution(distribution)
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
        # Given
        distribution = Distribution(distribution="0=1=5=7")
        hand = generate_hand_with_distribution(distribution)
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
