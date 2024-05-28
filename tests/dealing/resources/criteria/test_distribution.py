import unittest

from dealing.filters import DistributionFilter
from dealing.resources.criteria import parse_distribution_criteria
from enums import Seat
from models import Distribution


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
