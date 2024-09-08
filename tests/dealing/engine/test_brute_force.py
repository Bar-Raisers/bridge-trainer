import unittest

from common.models import Deal
from dealing.engine import BruteForceDealEngine
from dealing.filters import DealFilter


class MockDealFilter(DealFilter):

    def evaluate(self, deal: Deal) -> bool:
        return True


class BruteForceDealEngineTestCase(unittest.TestCase):

    def test_generate(self):
        # Given
        criteria = MockDealFilter()
        deal_engine = BruteForceDealEngine(criteria)

        # When
        deals = deal_engine.generate(1)

        # Then
        self.assertEqual(1, len(deals))
        self.assertEqual(1, deals[0].board_number)
        self.assertEqual(13, len(deals[0].north.cards))
        self.assertEqual(13, len(deals[0].east.cards))
        self.assertEqual(13, len(deals[0].south.cards))
        self.assertEqual(13, len(deals[0].west.cards))

        card_set = set()
        card_set.update(deals[0].north.cards)
        card_set.update(deals[0].east.cards)
        card_set.update(deals[0].south.cards)
        card_set.update(deals[0].west.cards)
        self.assertEqual(52, len(card_set))
