import unittest

from dealing.filters import AndFilter, HighCardPointsFilter, SuitLengthFilter
from enums import Rank, Seat, Suit
from models import Card, Deal, Hand


class AndFilterTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 14 HCP Hand with 5=4=3=1 Shape.
        cls.hand = Hand(
            cards=[
                Card(rank=Rank.ACE, suit=Suit.SPADES),
                Card(rank=Rank.KING, suit=Suit.SPADES),
                Card(rank=Rank.QUEEN, suit=Suit.SPADES),
                Card(rank=Rank.JACK, suit=Suit.SPADES),
                Card(rank=Rank.TEN, suit=Suit.SPADES),
                Card(rank=Rank.ACE, suit=Suit.HEARTS),
                Card(rank=Rank.TEN, suit=Suit.HEARTS),
                Card(rank=Rank.NINE, suit=Suit.HEARTS),
                Card(rank=Rank.EIGHT, suit=Suit.HEARTS),
                Card(rank=Rank.TEN, suit=Suit.DIAMONDS),
                Card(rank=Rank.NINE, suit=Suit.DIAMONDS),
                Card(rank=Rank.EIGHT, suit=Suit.DIAMONDS),
                Card(rank=Rank.TEN, suit=Suit.CLUBS),
            ],
        )
        cls.high_card_points_filter_14 = HighCardPointsFilter(
            seat=Seat.NORTH,
            minimum_high_card_points=14,
            maximum_high_card_points=14,
        )
        cls.high_card_points_filter_15 = HighCardPointsFilter(
            seat=Seat.NORTH,
            minimum_high_card_points=15,
            maximum_high_card_points=15,
        )
        cls.suit_length_filter_5_spades = SuitLengthFilter(
            seat=Seat.NORTH,
            suit=Suit.SPADES,
            minimum_suit_length=5,
            maximum_suit_length=5,
        )

    def test_and_filter(self):
        # Given a 14 HCP, 5=4=3=1 hand in North.
        deal = Deal(
            board_number=1,
            north=self.hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = AndFilter(
            filters=[
                self.high_card_points_filter_14,
                self.suit_length_filter_5_spades,
            ]
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertTrue(evaluation)

    def test_and_filter_with_failing_filter(self):
        # Given a 14 HCP, 5=4=3=1 hand in North.
        deal = Deal(
            board_number=1,
            north=self.hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = AndFilter(
            filters=[
                self.high_card_points_filter_15,
                self.suit_length_filter_5_spades,
            ]
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertFalse(evaluation)
