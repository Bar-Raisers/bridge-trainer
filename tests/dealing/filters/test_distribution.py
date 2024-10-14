import unittest

from common.enums import Seat
from common.models import Deal, Distribution, Hand
from common.tests.utilities import generate_hand_with_distribution
from dealing.filters import BalancedFilter, DistributionFilter


class BalancedFilterTestCase(unittest.TestCase):

    def test_balanced_filter_with_4333_hand(self):
        # Given
        distribution_4333 = Distribution(distribution="4=3=3=3")
        hand_4333 = generate_hand_with_distribution(distribution_4333)

        deal = Deal(
            board_number=1,
            north=hand_4333,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = BalancedFilter(
            seat=Seat.NORTH,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertTrue(evaluation)

    def test_balanced_filter_with_4432_hand(self):
        # Given
        distribution_4432 = Distribution(distribution="4=4=3=2")
        hand_4432 = generate_hand_with_distribution(distribution_4432)

        deal = Deal(
            board_number=1,
            north=hand_4432,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = BalancedFilter(
            seat=Seat.NORTH,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertTrue(evaluation)

    def test_balanced_filter_with_5332_hand(self):
        # Given
        distribution_5332 = Distribution(distribution="5=3=3=2")
        hand_5332 = generate_hand_with_distribution(distribution_5332)

        deal = Deal(
            board_number=1,
            north=hand_5332,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = BalancedFilter(
            seat=Seat.NORTH,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertTrue(evaluation)

    def test_balanced_filter_with_hand_containing_two_doubletons(self):
        # Given
        distribution_5422 = Distribution(distribution="5=4=2=2")
        two_doubletons_hand = generate_hand_with_distribution(distribution_5422)

        deal = Deal(
            board_number=1,
            north=two_doubletons_hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = BalancedFilter(
            seat=Seat.NORTH,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertFalse(evaluation)

    def test_balanced_filter_with_hand_containing_singleton(self):
        # Given
        distribution_5431 = Distribution(distribution="5=4=3=1")
        singleton_hand = generate_hand_with_distribution(distribution_5431)

        deal = Deal(
            board_number=1,
            north=singleton_hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = BalancedFilter(
            seat=Seat.NORTH,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertFalse(evaluation)

    def test_balanced_filter_with_hand_containing_void(self):
        # Given
        distribution_5440 = Distribution(distribution="5=4=4=0")
        void_hand = generate_hand_with_distribution(distribution_5440)

        deal = Deal(
            board_number=1,
            north=void_hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = BalancedFilter(
            seat=Seat.NORTH,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertFalse(evaluation)


class DistributionFilterTestCase(unittest.TestCase):

    def test_distribution_filter_with_matching_exact_distribution(self):
        # Given
        distribution = Distribution(distribution="5=4=3=1")
        hand = generate_hand_with_distribution(distribution)

        deal = Deal(
            board_number=1,
            north=hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        filter = DistributionFilter(
            seat=Seat.NORTH,
            distribution=distribution,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertTrue(evaluation)

    def test_distribution_filter_with_different_exact_distribution(self):
        # Given
        hand_distribution = Distribution(distribution="5=4=3=1")
        hand = generate_hand_with_distribution(hand_distribution)

        deal = Deal(
            board_number=1,
            north=hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )

        filter_distribution = Distribution(distribution="1=3=4=5")
        filter = DistributionFilter(
            seat=Seat.NORTH,
            distribution=filter_distribution,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertFalse(evaluation)

    def test_distribution_filter_with_matching_inexact_distribution(self):
        # Given
        hand_distribution = Distribution(distribution="5=4=3=1")
        hand = generate_hand_with_distribution(hand_distribution)

        deal = Deal(
            board_number=1,
            north=hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )

        filter_distribution = Distribution(distribution="5-4-3-1")
        filter = DistributionFilter(
            seat=Seat.NORTH,
            distribution=filter_distribution,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertTrue(evaluation)

    def test_distribution_filter_with_different_inexact_distribution(self):
        # Given
        hand_distribution = Distribution(distribution="5=4=3=1")
        hand = generate_hand_with_distribution(hand_distribution)

        deal = Deal(
            board_number=1,
            north=hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )

        filter_distribution = Distribution(distribution="4-4-3-2")
        filter = DistributionFilter(
            seat=Seat.NORTH,
            distribution=filter_distribution,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertFalse(evaluation)

    def test_distribution_filter_in_every_seat(self):
        # Given
        hand_distribution = Distribution(distribution="5=4=3=1")
        hand = generate_hand_with_distribution(hand_distribution)

        template_kwargs = {
            "board_number": 1,
            "north": Hand(cards=[]),
            "east": Hand(cards=[]),
            "south": Hand(cards=[]),
            "west": Hand(cards=[]),
        }

        north_kwargs = template_kwargs.copy()
        north_kwargs["north"] = hand
        north_deal = Deal(**north_kwargs)

        east_kwargs = template_kwargs.copy()
        east_kwargs["east"] = hand
        east_deal = Deal(**east_kwargs)

        south_kwargs = template_kwargs.copy()
        south_kwargs["south"] = hand
        south_deal = Deal(**south_kwargs)

        west_kwargs = template_kwargs.copy()
        west_kwargs["west"] = hand
        west_deal = Deal(**west_kwargs)

        filter_distribution = Distribution(distribution="5=4=3=1")
        north_filter, east_filter, south_filter, west_filter = (
            DistributionFilter(seat=seat, distribution=filter_distribution)
            for seat in Seat
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
