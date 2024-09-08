import unittest

from common.enums import Seat
from common.models import Distribution
from dealing.filters import BalancedFilter, DistributionFilter
from dealing.resources.criteria import (
    parse_balanced_criteria,
    parse_distribution_criteria,
)


class ParseBalancedDistributionCriteriaTestCase(unittest.TestCase):

    def test_parse_balanced_distribution_criteria(self):
        # Given
        seat = Seat.NORTH
        attributes = {
            "type": "balanced",
            "seat": seat,
        }

        # When
        filter = parse_balanced_criteria(attributes)

        # Then
        self.assertIsInstance(filter, BalancedFilter)
        self.assertEqual(seat, filter.seat)


class ParseDistributionCriteriaTestCase(unittest.TestCase):

    def test_parse_distribution_criteria(self):
        # Given
        seat = Seat.NORTH
        distribution = "5=4=3=1"

        attributes = {
            "type": "distribution",
            "seat": seat,
            "distribution": distribution,
        }

        # When
        filter = parse_distribution_criteria(attributes)

        # Then
        expected_distribution = Distribution(distribution=distribution)
        self.assertIsInstance(filter, DistributionFilter)
        self.assertEqual(seat, filter.seat)
        self.assertEqual(expected_distribution, filter.distribution)


if __name__ == "__main__":
    unittest.main()
