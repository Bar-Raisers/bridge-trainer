from typing import List

from dealing.filters.base import DealFilter
from models import Deal


class AndFilter(DealFilter):

    def __init__(
        self,
        filters: List[DealFilter],
    ) -> None:
        self.filters = filters

    def evaluate(self, deal: Deal) -> bool:
        for filter in self.filters:
            if not filter.evaluate(deal):
                return False

        return True
