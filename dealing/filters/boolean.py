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


class NotFilter(DealFilter):

    def __init__(
        self,
        filter: DealFilter,
    ) -> None:
        self.filter = filter

    def evaluate(self, deal: Deal) -> bool:
        return not self.filter.evaluate(deal)


class OrFilter(DealFilter):

    def __init__(
        self,
        filters: List[DealFilter],
    ) -> None:
        self.filters = filters

    def evaluate(self, deal: Deal) -> bool:
        for filter in self.filters:
            if filter.evaluate(deal):
                return True

        return False
