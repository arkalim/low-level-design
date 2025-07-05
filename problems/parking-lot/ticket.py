from time import time

from vehicle.vehicle import Vehicle
from spot import Spot
from billing.billing_strategy import BillingStrategy

class Ticket:
    def __init__(self, vehicle: Vehicle, spot: Spot, billing_strategy: BillingStrategy):
        self.vehicle = vehicle
        self.spot = spot
        self.park_timestamp = int(time())
        self.unpark_timestamp = None
        self.billing_strategy = billing_strategy

    def getDuration(self) -> int:
        if self.unpark_timestamp is None:
            return int(time()) - self.park_timestamp
        return self.unpark_timestamp - self.park_timestamp
    
    def unpark(self):
        self.unpark_timestamp = int(time())

    def get_bill(self) -> float:
        return self.billing_strategy.get_bill(self)