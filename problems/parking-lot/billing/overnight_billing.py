from ticket import Ticket
from .billing_strategy import BillingStrategy

class OvernightBilling(BillingStrategy):
    bill = 12

    def get_bill(self, ticket: Ticket) -> float:
        return self.bill