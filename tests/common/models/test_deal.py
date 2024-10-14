import unittest

from common.enums import Rank, Seat, Suit, Vulnerability
from common.models import Card, Deal, Hand


class DealTestCase(unittest.TestCase):

    def test_constructor_populates_dealer(self):
        # Given
        board_number = 1
        expected_dealer = Seat.NORTH

        # When
        deal = Deal(
            board_number=board_number,
            north=Hand(cards=[]),
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )

        # Then
        self.assertEqual(expected_dealer, deal.dealer)

    def test_constructor_populates_vulnerability(self):
        # Given
        board_number = 1
        expected_vulnerability = Vulnerability.NONE

        # When
        deal = Deal(
            board_number=board_number,
            north=Hand(cards=[]),
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )

        # Then
        self.assertEqual(expected_vulnerability, deal.vulnerability)

    def test_str(self):
        # Given
        north = Hand(cards=[Card(rank=Rank.ACE, suit=Suit.SPADES)])
        east = Hand(cards=[Card(rank=Rank.ACE, suit=Suit.HEARTS)])
        south = Hand(cards=[Card(rank=Rank.ACE, suit=Suit.DIAMONDS)])
        west = Hand(cards=[Card(rank=Rank.ACE, suit=Suit.CLUBS)])

        deal = Deal(
            board_number=1,
            north=north,
            east=east,
            south=south,
            west=west,
        )
        expected_string = (
            f"{Seat.NORTH}: AS\n"
            f"{Seat.EAST}: AH\n"
            f"{Seat.SOUTH}: AD\n"
            f"{Seat.WEST}: AC"
        )

        # When
        string = str(deal)

        # Then
        self.assertEqual(expected_string, string)

    def test_get_hand(self):
        # Given
        north = Hand(cards=[Card(rank=Rank.ACE, suit=Suit.SPADES)])
        east = Hand(cards=[Card(rank=Rank.ACE, suit=Suit.HEARTS)])
        south = Hand(cards=[Card(rank=Rank.ACE, suit=Suit.DIAMONDS)])
        west = Hand(cards=[Card(rank=Rank.ACE, suit=Suit.CLUBS)])

        deal = Deal(
            board_number=1,
            north=north,
            east=east,
            south=south,
            west=west,
        )

        # When
        hand = deal.get_hand(Seat.NORTH)

        # Then
        self.assertListEqual(north.cards, hand.cards)
