import unittest

from common.enums import Rank, Seat, Suit
from common.models import Card, Deal, Distribution, Hand
from dealing.filters import DistributionFilter


class DistributionFilterTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 5=4=3=1 Hand
        cls.hand = Hand(
            cards=[
                Card(rank=Rank.ACE, suit=Suit.SPADES),
                Card(rank=Rank.KING, suit=Suit.SPADES),
                Card(rank=Rank.QUEEN, suit=Suit.SPADES),
                Card(rank=Rank.JACK, suit=Suit.SPADES),
                Card(rank=Rank.TEN, suit=Suit.SPADES),
                Card(rank=Rank.ACE, suit=Suit.HEARTS),
                Card(rank=Rank.KING, suit=Suit.HEARTS),
                Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
                Card(rank=Rank.JACK, suit=Suit.HEARTS),
                Card(rank=Rank.ACE, suit=Suit.DIAMONDS),
                Card(rank=Rank.KING, suit=Suit.DIAMONDS),
                Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS),
                Card(rank=Rank.ACE, suit=Suit.CLUBS),
            ],
        )

    def test_distribution_filter_with_matching_exact_distribution(self):
        # Given a 5=4=3=1 hand in North.
        deal = Deal(
            board_number=1,
            north=self.hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        distribution = Distribution(distribution="5=4=3=1")
        filter = DistributionFilter(
            seat=Seat.NORTH,
            distribution=distribution,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertTrue(evaluation)

    def test_distribution_filter_with_different_exact_distribution(self):
        # Given a 5=4=3=1 hand in North.
        deal = Deal(
            board_number=1,
            north=self.hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        distribution = Distribution(distribution="1=3=4=5")
        filter = DistributionFilter(
            seat=Seat.NORTH,
            distribution=distribution,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertFalse(evaluation)

    def test_distribution_filter_with_matching_inexact_distribution(self):
        # Given a 5=4=3=1 hand in North.
        deal = Deal(
            board_number=1,
            north=self.hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        distribution = Distribution(distribution="5-4-3-1")
        filter = DistributionFilter(
            seat=Seat.NORTH,
            distribution=distribution,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertTrue(evaluation)

    def test_distribution_filter_with_different_inexact_distribution(self):
        # Given a 5=4=3=1 hand in North.
        deal = Deal(
            board_number=1,
            north=self.hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        distribution = Distribution(distribution="4-4-3-2")
        filter = DistributionFilter(
            seat=Seat.NORTH,
            distribution=distribution,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertFalse(evaluation)

    def test_distribution_filter_in_every_seat(self):
        # Given a 5=4=3=1 Hand in Every Seat.
        template_kwargs = {
            "board_number": 1,
            "north": Hand(cards=[]),
            "east": Hand(cards=[]),
            "south": Hand(cards=[]),
            "west": Hand(cards=[]),
        }

        north_kwargs = template_kwargs.copy()
        north_kwargs["north"] = self.hand
        north_deal = Deal(**north_kwargs)

        east_kwargs = template_kwargs.copy()
        east_kwargs["east"] = self.hand
        east_deal = Deal(**east_kwargs)

        south_kwargs = template_kwargs.copy()
        south_kwargs["south"] = self.hand
        south_deal = Deal(**south_kwargs)

        west_kwargs = template_kwargs.copy()
        west_kwargs["west"] = self.hand
        west_deal = Deal(**west_kwargs)

        distribution = Distribution(distribution="5=4=3=1")
        north_filter, east_filter, south_filter, west_filter = (
            DistributionFilter(seat=seat, distribution=distribution) for seat in Seat
        )

        # When
        north_evaluation = north_filter.evaluate(north_deal)
        east_evaluation = east_filter.evaluate(east_deal)
        south_evaluation = south_filter.evaluate(south_deal)
        west_evaluation = west_filter.evaluate(west_deal)

        # Then
        self.assertTrue(north_evaluation)
        self.assertTrue(east_evaluation)
        self.assertTrue(south_evaluation)
        self.assertTrue(west_evaluation)


if __name__ == "__main__":
    unittest.main()
