import unittest

from enums.suit import Suit


class SuitTestCase(unittest.TestCase):

    def test_less_than_comparison(self):
        # Given
        lesser = Suit.SPADES
        greater = Suit.HEARTS

        # When
        comparison = lesser < greater

        # Then
        self.assertTrue(comparison)

    def test_greater_than_comparison(self):
        # Given
        lesser = Suit.SPADES
        greater = Suit.HEARTS

        # When
        comparison = greater > lesser

        # Then
        self.assertTrue(comparison)

    def test_symbol_property(self):
        # Given
        suit_to_symbol_map = {
            Suit.SPADES: "S",
            Suit.HEARTS: "H",
            Suit.DIAMONDS: "D",
            Suit.CLUBS: "C",
        }

        # When & Then
        for suit, expected_symbol in suit_to_symbol_map.items():
            symbol = suit.symbol
            self.assertEqual(expected_symbol, symbol)

    def test_suit_from_name(self):
        # Given
        name_to_suit_map = {
            "spades": Suit.SPADES,
            "hearts": Suit.HEARTS,
            "diamonds": Suit.DIAMONDS,
            "clubs": Suit.CLUBS,
        }

        # When & Then
        for suit_name, expected_suit in name_to_suit_map.items():
            suit = Suit.from_name(suit_name)
            self.assertEqual(expected_suit, suit)

    def test_suit_from_symbol(self):
        # Given
        symbol_to_suit_map = {
            "S": Suit.SPADES,
            "H": Suit.HEARTS,
            "D": Suit.DIAMONDS,
            "C": Suit.CLUBS,
        }

        # When & Then
        for symbol, expected_suit in symbol_to_suit_map.items():
            suit = Suit.from_symbol(symbol)
            self.assertEqual(expected_suit, suit)


if __name__ == "__main__":
    unittest.main()
