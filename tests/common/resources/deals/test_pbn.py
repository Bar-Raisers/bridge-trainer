import unittest

from common.enums import Rank, Seat, Suit, Vulnerability
from common.models import Card, Deal, Hand
from common.resources.deals.pbn import PBNImportFormatter
from dealing.models import DeckFactory


class PBNImportFormatterTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        deck = DeckFactory.create_sorted_deck()
        spades = Hand(cards=[deck.draw() for _ in range(13)])
        hearts = Hand(cards=[deck.draw() for _ in range(13)])
        diamonds = Hand(cards=[deck.draw() for _ in range(13)])
        clubs = Hand(cards=[deck.draw() for _ in range(13)])

        cls.deals = [
            Deal(board_number=1, north=spades, east=hearts, south=diamonds, west=clubs),
            Deal(board_number=2, north=hearts, east=diamonds, south=clubs, west=spades),
        ]

    def test_format_with_zero_deals(self):
        # Given
        deals = []
        expected_output = "% PBN 2.1\n" "% IMPORT\n"

        # When
        pbn_string = PBNImportFormatter.format(deals)

        # Then
        self.assertEqual(expected_output, pbn_string)

    def test_format_with_one_deal(self):
        # Given
        deals = [self.deals[0]]
        expected_output = (
            "% PBN 2.1\n"
            "% IMPORT\n"
            "\n"
            '[Board "1"]\n'
            '[Dealer "N"]\n'
            '[Vulnerable "None"]\n'
            '[Deal "N:AKQJT98765432... .AKQJT98765432.. ..AKQJT98765432. ...AKQJT98765432"]\n'
        )

        # When
        pbn_string = PBNImportFormatter.format(deals)

        # Then
        self.assertEqual(expected_output, pbn_string)

    def test_format_with_multiple_deals(self):
        # Given
        deals = self.deals
        expected_output = (
            "% PBN 2.1\n"
            "% IMPORT\n"
            "\n"
            '[Board "1"]\n'
            '[Dealer "N"]\n'
            '[Vulnerable "None"]\n'
            '[Deal "N:AKQJT98765432... .AKQJT98765432.. ..AKQJT98765432. ...AKQJT98765432"]\n'
            "\n"
            '[Board "2"]\n'
            '[Dealer "E"]\n'
            '[Vulnerable "NS"]\n'
            '[Deal "N:.AKQJT98765432.. ..AKQJT98765432. ...AKQJT98765432 AKQJT98765432..."]\n'
        )

        # When
        pbn_string = PBNImportFormatter.format(deals)

        # Then
        self.assertEqual(expected_output, pbn_string)
