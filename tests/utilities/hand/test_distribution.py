import unittest

from enums import Rank, Suit
from models import Card, Distribution, Hand
from utilities.hand.distribution import get_distribution


class DistributionTestCase(unittest.TestCase):

    def test_get_distribution(self):
        # Given
        hand = Hand(
            cards=[
                # 5 Spades
                Card(rank=Rank.ACE, suit=Suit.SPADES),
                Card(rank=Rank.KING, suit=Suit.SPADES),
                Card(rank=Rank.QUEEN, suit=Suit.SPADES),
                Card(rank=Rank.JACK, suit=Suit.SPADES),
                Card(rank=Rank.TEN, suit=Suit.SPADES),
                # 5 Hearts
                Card(rank=Rank.ACE, suit=Suit.HEARTS),
                Card(rank=Rank.KING, suit=Suit.HEARTS),
                Card(rank=Rank.QUEEN, suit=Suit.HEARTS),
                Card(rank=Rank.JACK, suit=Suit.HEARTS),
                Card(rank=Rank.TEN, suit=Suit.HEARTS),
                # 2 Diamonds
                Card(rank=Rank.ACE, suit=Suit.DIAMONDS),
                Card(rank=Rank.KING, suit=Suit.DIAMONDS),
                # 1 Club
                Card(rank=Rank.ACE, suit=Suit.CLUBS),
            ],
        )
        expected_distribution = Distribution(distribution="5=5=2=1")

        # When
        distribution = get_distribution(hand)

        # Then
        self.assertEqual(expected_distribution, distribution)


if __name__ == "__main__":
    unittest.main()
