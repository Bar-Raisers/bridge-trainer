import unittest
from typing import Hashable

from dealing.enums.filters import FilterType


class FilterTypeTestCase(unittest.TestCase):

    def test_is_hashable(self):
        # Given
        filter_type = FilterType.HIGH_CARD_POINTS

        # When
        filter_type_hash = hash(filter_type)
        is_hashable = isinstance(filter_type, Hashable)

        # Then
        self.assertTrue(is_hashable)


if __name__ == "__main__":
    unittest.main()
