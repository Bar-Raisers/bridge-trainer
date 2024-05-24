from abc import ABC, abstractmethod

from models import Deal


class DealFilter(ABC):

    @abstractmethod
    def evaluate(self, deal: Deal) -> bool:
        raise NotImplementedError
