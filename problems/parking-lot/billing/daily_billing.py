import math

from ticket import Ticket
from .billing_strategy import BillingStrategy

class DailyBilling(BillingStrategy):
    rate = 30

    def get_bill(self, ticket: Ticket) -> float:
        hours = math.ceil(ticket.getDuration() / 60 / 60)
        days = math.ceil(hours / 24)
        return self.rate * days