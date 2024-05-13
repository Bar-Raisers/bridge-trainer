import unittest
from typing import List
from unittest import mock

from dealing.models.deck import Deck, DeckFactory
from enums.rank import Rank
from enums.suit import Suit
from models.card import Card


class DeckTestCase(unittest.TestCase):

    def test_draw(self):
        # Given
        card_one = Card(rank=Rank.ACE, suit=Suit.SPADES)
        card_two = Card(rank=Rank.KING, suit=Suit.SPADES)
        card_three = Card(rank=Rank.QUEEN, suit=Suit.SPADES)
        deck = Deck(cards=[card_one, card_two, card_three])

        # When
        drawn_one = deck.draw()
        drawn_two = deck.draw()
        drawn_three = deck.draw()

        # Then
        self.assertEqual(card_one, drawn_one)
        self.assertEqual(card_two, drawn_two)
        self.assertEqual(card_three, drawn_three)
        self.assertTrue(deck.is_empty())

    def test_draw_with_empty_deck(self):
        # Given
        deck = Deck(cards=[])

        # When & Then
        with self.assertRaises(IndexError):
            deck.draw()

    def test_is_empty_with_cards_in_deck(self):
        # Given
        card_one = Card(rank=Rank.ACE, suit=Suit.SPADES)
        card_two = Card(rank=Rank.KING, suit=Suit.SPADES)
        deck = Deck(cards=[card_one, card_two])

        # When
        is_empty = deck.is_empty()

        # Then
        self.assertFalse(is_empty)

    def test_is_empty_without_cards_in_deck(self):
        # Given
        deck = Deck(cards=[])

        # When
        is_empty = deck.is_empty()

        # Then
        self.assertTrue(is_empty)

    @mock.patch("dealing.models.deck.shuffle")
    def test_shuffle(self, mock_shuffle):
        # Mock: Reverse Deck on shuffle().
        def shuffle_side_effect(cards: List[Card]) -> None:
            cards.reverse()

        mock_shuffle.side_effect = shuffle_side_effect

        # Given
        card_one = Card(rank=Rank.ACE, suit=Suit.SPADES)
        card_two = Card(rank=Rank.KING, suit=Suit.SPADES)
        card_three = Card(rank=Rank.QUEEN, suit=Suit.SPADES)
        deck = Deck(cards=[card_one, card_two, card_three])

        # When
        deck.shuffle()

        # Then
        self.assertEqual(card_three, deck.cards[0])
        self.assertEqual(card_two, deck.cards[1])
        self.assertEqual(card_one, deck.cards[2])


class DeckFactoryTestCase(unittest.TestCase):

    def test_create_sorted_deck(self):
        # When
        sorted_deck = DeckFactory.create_sorted_deck()

        # Then
        sorted_cards = sorted(sorted_deck.cards)
        self.assertListEqual(sorted_cards, sorted_deck.cards)

    @mock.patch("dealing.models.deck.shuffle")
    def test_create_shuffled_deck(self, mock_shuffle):
        # Mock: Reverse Deck on shuffle().
        def shuffle_side_effect(cards: List[Card]) -> None:
            cards.reverse()

        mock_shuffle.side_effect = shuffle_side_effect

        # When
        shuffled_deck = DeckFactory.create_shuffled_deck()

        # Then
        reversed_cards = sorted(shuffled_deck.cards, reverse=True)
        self.assertListEqual(reversed_cards, shuffled_deck.cards)


if __name__ == "__main__":
    unittest.main()
