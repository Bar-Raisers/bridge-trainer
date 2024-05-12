import unittest

from dealing.engine.base import DealEngine
from dealing.filters.base import DealFilter
from models.deal import Deal
from models.hand import Hand


class MockDealFilter(DealFilter):

    def evaluate(self, deal: Deal) -> bool:
        return True


class MockDealEngine(DealEngine):

    def _generate_deal(self, board_number: int) -> Deal:
        return Deal(
            board_number=board_number,
            north=Hand(cards=[]),
            east=Hand(cards=[]),
            south=Hand(cards=[]),
            west=Hand(cards=[]),
        )


class DealEngineTestCase(unittest.TestCase):

    def test_generate_with_negative_deal_quantities(self):
        # Given
        criteria = MockDealFilter()
        deal_engine = MockDealEngine(criteria)

        # When
        negative_deals = deal_engine.generate(-1)

        # Then
        self.assertEqual(0, len(negative_deals))

    def test_generate_with_positive_deal_quantities(self):
        # Given
        criteria = MockDealFilter()
        deal_engine = MockDealEngine(criteria)

        # When
        one_deal = deal_engine.generate(1)
        ten_deals = deal_engine.generate(10)
        hundred_deals = deal_engine.generate(100)

        # Then
        self.assertEqual(1, len(one_deal))
        self.assertEqual(10, len(ten_deals))
        self.assertEqual(100, len(hundred_deals))

    def test_generate_with_zero_deal_quantity(self):
        # Given
        criteria = MockDealFilter()
        deal_engine = MockDealEngine(criteria)

        # When
        zero_deals = deal_engine.generate(0)

        # Then
        self.assertEqual(0, len(zero_deals))
