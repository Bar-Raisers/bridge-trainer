import unittest

from pydantic import ValidationError

from common.models import Distribution


class DistributionTestCase(unittest.TestCase):

    def test_equals_with_matching_exact_distributions(self):
        # Given
        distribution_one = Distribution(distribution="5=4=3=1")
        distribution_two = Distribution(distribution="5=4=3=1")

        # When
        comparison = distribution_one == distribution_two

        # Then
        self.assertTrue(comparison)

    def test_equals_with_different_exact_distributions(self):
        # Given
        distribution_one = Distribution(distribution="5=4=3=1")
        distribution_two = Distribution(distribution="5=3=3=2")

        # When
        comparison = distribution_one == distribution_two

        # Then
        self.assertFalse(comparison)

    def test_equals_with_matching_inexact_distributions(self):
        # Given
        distribution_one = Distribution(distribution="5-4-3-1")
        distribution_two = Distribution(distribution="5-4-3-1")

        # When
        comparison = distribution_one == distribution_two

        # Then
        self.assertTrue(comparison)

    def test_equals_with_different_inexact_distributions(self):
        # Given
        distribution_one = Distribution(distribution="5-4-3-1")
        distribution_two = Distribution(distribution="5-3-3-2")

        # When
        comparison = distribution_one == distribution_two

        # Then
        self.assertFalse(comparison)

    def test_equals_sorts_before_comparison_with_matching_inexact_distributions(self):
        # Given
        distribution_one = Distribution(distribution="5-4-3-1")
        distribution_two = Distribution(distribution="4-5-3-1")

        # When
        comparison = distribution_one == distribution_two

        # Then
        self.assertTrue(comparison)

    def test_is_exact_with_exact_distribution(self):
        # Given
        distribution_str = "4=3=3=3"
        distribution = Distribution(distribution=distribution_str)

        # When
        is_exact = distribution.is_exact

        # Then
        self.assertTrue(is_exact)

    def test_is_exact_with_inexact_distribution(self):
        # Given
        distribution_str = "4-3-3-3"
        distribution = Distribution(distribution=distribution_str)

        # When
        is_exact = distribution.is_exact

        # Then
        self.assertFalse(is_exact)

    def test_matches_with_matching_exact_distributions(self):
        # Given
        distribution_one = Distribution(distribution="4=3=3=3")
        distribution_two = Distribution(distribution="4=3=3=3")

        # When
        is_matching = distribution_one.matches(distribution_two)

        # Then
        self.assertTrue(is_matching)

    def test_matches_with_different_exact_distributions(self):
        # Given
        distribution_one = Distribution(distribution="4=3=3=3")
        distribution_two = Distribution(distribution="4=4=3=2")

        # When
        is_matching = distribution_one.matches(distribution_two)

        # Then
        self.assertFalse(is_matching)

    def test_matches_with_matching_exact_and_inexact_distributions(self):
        # Given
        distribution_one = Distribution(distribution="4=3=3=3")
        distribution_two = Distribution(distribution="4-3-3-3")

        # When
        is_matching = distribution_one.matches(distribution_two)

        # Then
        self.assertTrue(is_matching)

    def test_matches_with_different_exact_and_inexact_distributions(self):
        # Given
        distribution_one = Distribution(distribution="4=3=3=3")
        distribution_two = Distribution(distribution="4-4-3-2")

        # When
        is_matching = distribution_one.matches(distribution_two)

        # Then
        self.assertFalse(is_matching)

    def test_matches_with_matching_inexact_distributions(self):
        # Given
        distribution_one = Distribution(distribution="4-3-3-3")
        distribution_two = Distribution(distribution="4-3-3-3")

        # When
        is_matching = distribution_one.matches(distribution_two)

        # Then
        self.assertTrue(is_matching)

    def test_matches_with_different_inexact_distributions(self):
        # Given
        distribution_one = Distribution(distribution="4-3-3-3")
        distribution_two = Distribution(distribution="4-4-3-2")

        # When
        is_matching = distribution_one.matches(distribution_two)

        # Then
        self.assertFalse(is_matching)

    def test_matches_does_not_sort_distributions_before_comparison_with_two_exact_distributions(
        self,
    ):
        # Given
        distribution_one = Distribution(distribution="3=3=3=4")
        distribution_two = Distribution(distribution="4=3=3=3")

        # When
        is_matching = distribution_one.matches(distribution_two)

        # Then
        self.assertFalse(is_matching)

    def test_matches_sorts_distributions_before_comparison_with_one_inexact_distribution(
        self,
    ):
        # Given
        distribution_one = Distribution(distribution="3=3=3=4")
        distribution_two = Distribution(distribution="3-4-3-3")

        # When
        is_matching = distribution_one.matches(distribution_two)

        # Then
        self.assertTrue(is_matching)

    def test_matches_sorts_distributions_before_comparison_with_two_inexact_distributions(
        self,
    ):
        # Given
        distribution_one = Distribution(distribution="3-3-3-4")
        distribution_two = Distribution(distribution="3-4-3-3")

        # When
        is_matching = distribution_one.matches(distribution_two)

        # Then
        self.assertTrue(is_matching)

    def test_str_with_exact_distribution(self):
        # Given
        expected_str = "4=3=3=3"
        distribution = Distribution(distribution=expected_str)

        # When
        string = str(distribution)

        # Then
        self.assertEqual(expected_str, string)

    def test_str_with_inexact_distribution(self):
        # Given
        expected_str = "4-3-3-3"
        distribution = Distribution(distribution=expected_str)

        # When
        string = str(distribution)

        # Then
        self.assertEqual(expected_str, string)

    def test_suit_lengths_with_exact_distribution(self):
        # Given
        distribution_str = "2=4=5=2"
        distribution = Distribution(distribution=distribution_str)

        # When
        suit_lengths = distribution.suit_lengths

        # Then: returns the suit lengths in original order.
        expected_suit_lengths = [2, 4, 5, 2]
        self.assertListEqual(expected_suit_lengths, suit_lengths)

    def test_suit_lengths_with_inexact_distribution(self):
        # Given
        distribution_str = "2-4-5-2"
        distribution = Distribution(distribution=distribution_str)

        # When
        suit_lengths = distribution.suit_lengths

        # Then: returns the suit lengths sorted high to low.
        expected_suit_lengths = [5, 4, 2, 2]
        self.assertListEqual(expected_suit_lengths, suit_lengths)

    def test_validate_distribution_with_mixed_dashes_and_equals(self):
        # Given
        malformed_distribution = "4-3=3-3"

        # When & Then
        with self.assertRaises(ValidationError):
            Distribution(distribution=malformed_distribution)

    def test_validate_distribution_with_suit_lengths_summing_above_thirteen(self):
        # Given
        malformed_distribution = "9=4=1=0"

        # When & Then
        with self.assertRaises(ValidationError):
            Distribution(distribution=malformed_distribution)


if __name__ == "__main__":
    unittest.main()
