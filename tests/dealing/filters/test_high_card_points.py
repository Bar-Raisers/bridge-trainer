import unittest

from dealing.filters import HighCardPointsFilter
from enums import Rank, Seat, Suit
from models import Card, Deal, Hand


class HighCardPointsTestCase(unittest.TestCase):

    def test_high_card_points_filter_within_range(self):
        # Given a hand worth 17 high card points
        cards = [
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.SPADES),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.FOUR, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.THREE, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.JACK, suit=Suit.DIAMONDS),
            Card(rank=Rank.SIX, suit=Suit.DIAMONDS),
            Card(rank=Rank.KING, suit=Suit.CLUBS),
            Card(rank=Rank.EIGHT, suit=Suit.CLUBS),
        ]
        deal = Deal(
            board_number=1,
            north=Hand(cards=cards),
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = HighCardPointsFilter(
            seat=Seat.NORTH,
            minimum_high_card_points=15,
            maximum_high_card_points=17,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertTrue(evaluation)

    def test_high_card_points_filter_outside_range(self):
        # Given a hand worth 17 high card points
        cards = [
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.SPADES),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.FOUR, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.THREE, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.JACK, suit=Suit.DIAMONDS),
            Card(rank=Rank.SIX, suit=Suit.DIAMONDS),
            Card(rank=Rank.KING, suit=Suit.CLUBS),
            Card(rank=Rank.EIGHT, suit=Suit.CLUBS),
        ]
        deal = Deal(
            board_number=1,
            north=Hand(cards=cards),
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = HighCardPointsFilter(
            seat=Seat.NORTH,
            minimum_high_card_points=10,
            maximum_high_card_points=12,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertFalse(evaluation)

    def test_high_card_points_filter_in_every_seat(self):
        # Given four hands worth 17 high card points
        cards = [
            Card(rank=Rank.ACE, suit=Suit.SPADES),
            Card(rank=Rank.JACK, suit=Suit.SPADES),
            Card(rank=Rank.TEN, suit=Suit.SPADES),
            Card(rank=Rank.SEVEN, suit=Suit.SPADES),
            Card(rank=Rank.FOUR, suit=Suit.SPADES),
            Card(rank=Rank.ACE, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
            Card(rank=Rank.THREE, suit=Suit.HEARTS),
            Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
            Card(rank=Rank.JACK, suit=Suit.DIAMONDS),
            Card(rank=Rank.SIX, suit=Suit.DIAMONDS),
            Card(rank=Rank.KING, suit=Suit.CLUBS),
            Card(rank=Rank.EIGHT, suit=Suit.CLUBS),
        ]
        deal = Deal(
            board_number=1,
            north=Hand(cards=cards),
            east=Hand(cards=cards),
            south=Hand(cards=cards),
            west=Hand(cards=cards),
        )

        north_filter = HighCardPointsFilter(
            seat=Seat.NORTH,
            minimum_high_card_points=15,
            maximum_high_card_points=17,
        )
        east_filter = HighCardPointsFilter(
            seat=Seat.EAST,
            minimum_high_card_points=15,
            maximum_high_card_points=17,
        )
        south_filter = HighCardPointsFilter(
            seat=Seat.SOUTH,
            minimum_high_card_points=10,
            maximum_high_card_points=12,
        )
        west_filter = HighCardPointsFilter(
            seat=Seat.WEST,
            minimum_high_card_points=10,
            maximum_high_card_points=12,
        )

        # When
        north_evaluation = north_filter.evaluate(deal)
        east_evaluation = east_filter.evaluate(deal)
        south_evaluation = south_filter.evaluate(deal)
        west_evaluation = west_filter.evaluate(deal)

        # Then
        self.assertTrue(north_evaluation)
        self.assertTrue(east_evaluation)
        self.assertFalse(south_evaluation)
        self.assertFalse(west_evaluation)


if __name__ == "__main__":
    unittest.main()
