import unittest

from common.models import Distribution
from common.tests.utilities import generate_hand_with_distribution
from common.utilities.hand.distribution import get_distribution


class DistributionTestCase(unittest.TestCase):

    def test_get_distribution(self):
        # Given
        expected_distribution = Distribution(distribution="5=5=2=1")
        hand = generate_hand_with_distribution(expected_distribution)

        # When
        distribution = get_distribution(hand)

        # Then
        self.assertEqual(expected_distribution, distribution)


if __name__ == "__main__":
    unittest.main()
