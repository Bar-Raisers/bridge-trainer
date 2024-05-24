from abc import ABC, abstractmethod
from typing import List

from dealing.filters import DealFilter
from models import Deal


class DealEngine(ABC):

    def __init__(self, criteria: DealFilter) -> None:
        self.criteria = criteria

    def generate(self, deal_quantity: int) -> List[Deal]:
        deals = []
        generated_deals = 0

        while generated_deals < deal_quantity:
            deal = self._generate_deal(board_number=generated_deals + 1)
            if self.criteria.evaluate(deal):
                deals.append(deal)
                generated_deals += 1

        return deals

    @abstractmethod
    def _generate_deal(self, board_number: int) -> Deal:
        raise NotImplementedError
