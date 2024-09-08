import unittest

from common.enums import Rank, Seat, Suit
from common.models import Card, Deal, Hand
from dealing.filters import (
    AndFilter,
    HighCardPointsFilter,
    NotFilter,
    OrFilter,
    SuitLengthFilter,
)


class BooleanFilterTestCase(unittest.TestCase):

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
        cls.spades_length_filter_5 = SuitLengthFilter(
            seat=Seat.NORTH,
            suit=Suit.SPADES,
            minimum_suit_length=5,
            maximum_suit_length=5,
        )
        cls.spades_length_filter_4 = SuitLengthFilter(
            seat=Seat.NORTH,
            suit=Suit.SPADES,
            minimum_suit_length=4,
            maximum_suit_length=4,
        )


class AndFilterTestCase(BooleanFilterTestCase):

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
                self.spades_length_filter_5,
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
                self.spades_length_filter_5,
            ]
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertFalse(evaluation)


class NotFilterTestCase(BooleanFilterTestCase):

    def test_not_filter_with_passing_filter(self):
        # Given a 14 HCP, 5=4=3=1 hand in North.
        deal = Deal(
            board_number=1,
            north=self.hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = NotFilter(filter=self.high_card_points_filter_14)

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertFalse(evaluation)

    def test_not_filter_with_failing_filter(self):
        # Given a 14 HCP, 5=4=3=1 hand in North.
        deal = Deal(
            board_number=1,
            north=self.hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = NotFilter(filter=self.high_card_points_filter_15)

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertTrue(evaluation)


class OrFilterTestCase(BooleanFilterTestCase):

    def test_or_filter_with_passing_filters(self):
        # Given a 14 HCP, 5=4=3=1 hand in North.
        deal = Deal(
            board_number=1,
            north=self.hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = OrFilter(
            filters=[
                self.high_card_points_filter_14,
                self.spades_length_filter_5,
            ]
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertTrue(evaluation)

    def test_or_filter_with_one_passing_and_one_failing_filter(self):
        # Given a 14 HCP, 5=4=3=1 hand in North.
        deal = Deal(
            board_number=1,
            north=self.hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = OrFilter(
            filters=[
                self.high_card_points_filter_15,
                self.spades_length_filter_5,
            ]
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertTrue(evaluation)

    def test_or_filter_with_only_failing_filters(self):
        # Given a 14 HCp, 5=4=3=1 hand in North.
        deal = Deal(
            board_number=1,
            north=self.hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = OrFilter(
            filters=[
                self.high_card_points_filter_15,
                self.spades_length_filter_4,
            ]
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertFalse(evaluation)
