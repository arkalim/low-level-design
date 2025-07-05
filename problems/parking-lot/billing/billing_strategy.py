from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ticket import Ticket

from abc import ABC, abstractmethod

class BillingStrategy(ABC):
    @abstractmethod
    def get_bill(self, ticket: Ticket) -> float:
        pass