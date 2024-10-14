import unittest
from typing import Any, List
from unittest import mock

from common.models import Distribution
from common.tests.utilities.distribution import generate_hand_with_distribution
from common.utilities.hand import get_distribution


class GenerateHandTestCase(unittest.TestCase):

    @mock.patch("common.tests.utilities.distribution.shuffle")
    def test_generate_hand_with_inexact_distribution(self, mock_shuffle):
        # Mocks
        def shuffle_side_effect(items: List[Any]) -> None:
            items.reverse()

        mock_shuffle.side_effect = shuffle_side_effect

        # Given
        distribution = Distribution(distribution="4-3-3-3")
        expected_distribution = Distribution(distribution="3=3=3=4")

        # When
        hand = generate_hand_with_distribution(distribution)

        # Then
        self.assertTrue(mock_shuffle.is_called)
        self.assertTrue(get_distribution(hand).matches(expected_distribution))

    @mock.patch("common.tests.utilities.distribution.shuffle")
    def test_generate_hand_with_exact_distribution(self, mock_shuffle):
        # Given
        distribution = Distribution(distribution="4=3=3=3")

        # When
        hand = generate_hand_with_distribution(distribution)

        # Then
        self.assertTrue(get_distribution(hand).matches(distribution))
        self.assertTrue(mock_shuffle.is_not_called)


if __name__ == "__main__":
    unittest.main()
