import unittest

from common.enums import Seat, Suit
from common.models import Deal, Distribution, Hand
from common.tests.utilities import generate_hand_with_distribution
from dealing.filters import SuitLengthFilter


class SuitLengthFilterTestCase(unittest.TestCase):

    def test_suit_length_within_range(self):
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
        filter = SuitLengthFilter(
            seat=Seat.NORTH,
            suit=Suit.SPADES,
            minimum_suit_length=4,
            maximum_suit_length=6,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertTrue(evaluation)

    def test_suit_length_outside_range(self):
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
        filter = SuitLengthFilter(
            seat=Seat.NORTH,
            suit=Suit.CLUBS,
            minimum_suit_length=4,
            maximum_suit_length=6,
        )

        # When
        evaluation = filter.evaluate(deal)

        # Then
        self.assertFalse(evaluation)

    def test_suit_length_for_every_suit(self):
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
        spades_filter = SuitLengthFilter(
            seat=Seat.NORTH,
            suit=Suit.SPADES,
            minimum_suit_length=5,
            maximum_suit_length=5,
        )
        hearts_filter = SuitLengthFilter(
            seat=Seat.NORTH,
            suit=Suit.HEARTS,
            minimum_suit_length=4,
            maximum_suit_length=4,
        )
        diamonds_filter = SuitLengthFilter(
            seat=Seat.NORTH,
            suit=Suit.DIAMONDS,
            minimum_suit_length=3,
            maximum_suit_length=3,
        )
        clubs_filter = SuitLengthFilter(
            seat=Seat.NORTH,
            suit=Suit.CLUBS,
            minimum_suit_length=1,
            maximum_suit_length=1,
        )

        # When
        spades_evaluation = spades_filter.evaluate(deal)
        hearts_evaluation = hearts_filter.evaluate(deal)
        diamonds_evaluation = diamonds_filter.evaluate(deal)
        clubs_evaluation = clubs_filter.evaluate(deal)

        # Then
        self.assertTrue(spades_evaluation)
        self.assertTrue(hearts_evaluation)
        self.assertTrue(diamonds_evaluation)
        self.assertTrue(clubs_evaluation)

    def test_suit_length_filter_in_every_seat(self):
        # Given
        distribution = Distribution(distribution="5=4=3=1")
        hand = generate_hand_with_distribution(distribution)

        north_deal = Deal(
            board_number=1,
            north=hand,
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        east_deal = Deal(
            board_number=1,
            north=Hand(cards=[]),
            east=hand,
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )
        south_deal = Deal(
            board_number=1,
            north=Hand(cards=[]),
            east=Hand(cards=[]),
            south=hand,
            west=Hand(cards=[]),
        )
        west_deal = Deal(
            board_number=1,
            north=Hand(cards=[]),
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=hand,
        )

        north_filter, east_filter, south_filter, west_filter = (
            SuitLengthFilter(
                seat=seat,
                suit=Suit.SPADES,
                minimum_suit_length=5,
                maximum_suit_length=5,
            )
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
