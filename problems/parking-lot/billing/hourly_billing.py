import math

from ticket import Ticket
from .billing_strategy import BillingStrategy

class HourlyBilling(BillingStrategy):
    rate = 3

    def get_bill(self, ticket: Ticket) -> float:
        hours = math.ceil(ticket.get_duration() / 60 / 60)
        return self.rate * hours