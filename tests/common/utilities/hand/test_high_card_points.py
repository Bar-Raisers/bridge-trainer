import unittest

from common.enums import Rank, Suit
from common.models import Card, Hand
from common.utilities.hand.high_card_points import calculate_high_card_points


class HighCardPointsTestCase(unittest.TestCase):

    def test_calculate_high_card_points_with_aces(self):
        # Given
        cards = [
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
        ]
        hand = Hand(cards=cards)
        expected_high_card_points = 8

        # When
        high_card_points = calculate_high_card_points(hand)

        # Then
        self.assertEqual(expected_high_card_points, high_card_points)

    def test_calculate_high_card_points_with_kings(self):
        # Given
        cards = [
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.HEARTS),
        ]
        hand = Hand(cards=cards)
        expected_high_card_points = 6

        # When
        high_card_points = calculate_high_card_points(hand)

        # Then
        self.assertEqual(expected_high_card_points, high_card_points)

    def test_calculate_high_card_points_with_queens(self):
        # Given
        cards = [
            Card(rank=Rank.QUEEN, suit=Suit.SPADES),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
        ]
        hand = Hand(cards=cards)
        expected_high_card_points = 4

        # When
        high_card_points = calculate_high_card_points(hand)

        # Then
        self.assertEqual(expected_high_card_points, high_card_points)

    def test_calculate_high_card_points_with_jacks(self):
        # Given
        cards = [
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.JACK, suit=Suit.HEARTS),
        ]
        hand = Hand(cards=cards)
        expected_high_card_points = 2

        # When
        high_card_points = calculate_high_card_points(hand)

        # Then
        self.assertEqual(expected_high_card_points, high_card_points)

    def test_calculate_high_card_points_without_honour_cards(self):
        # Given
        cards = [
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.FOUR, suit=Suit.HEARTS),
        ]
        hand = Hand(cards=cards)
        expected_high_card_points = 0

        # When
        high_card_points = calculate_high_card_points(hand)

        # Then
        self.assertEqual(expected_high_card_points, high_card_points)

    def test_calculate_high_card_points_with_mixed_cards(self):
        # Given
        cards = [
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.KING, suit=Suit.SPADES),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.TWO, suit=Suit.HEARTS),
            Card(rank=Rank.KING, suit=Suit.DIAMONDS),
            Card(rank=Rank.JACK, suit=Suit.DIAMONDS),
            Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
            Card(rank=Rank.QUEEN, suit=Suit.CLUBS),
            Card(rank=Rank.JACK, suit=Suit.CLUBS),
            Card(rank=Rank.EIGHT, suit=Suit.CLUBS),
            Card(rank=Rank.TWO, suit=Suit.CLUBS),
        ]
        hand = Hand(cards=cards)
        expected_high_card_points = 20

        # When
        high_card_points = calculate_high_card_points(hand)

        # Then
        self.assertEqual(expected_high_card_points, high_card_points)
