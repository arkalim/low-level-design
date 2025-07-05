from typing import Optional

from level import Level
from ticket import Ticket

from vehicle.vehicle import Vehicle
from billing.billing_strategy import BillingStrategy

class ParkingLot():
    def __init__(self):
        self.levels: list[Level] = []
        self.tickets: dict[Vehicle, Ticket] = {}

    def add_level(self, level: Level):
        self.levels.append(level)

    def park(self, vehicle: Vehicle, billing_strategy: BillingStrategy) -> Optional[Ticket]:
        for level in self.levels:
            spot = level.park(vehicle)
            if spot:
                ticket = Ticket(vehicle, spot, billing_strategy)
                self.tickets[vehicle] = ticket
                return ticket
    
    def unpark(self, vehicle: Vehicle) -> Optional[Ticket]:
        for level in self.levels:
            spot = level.unpark(vehicle)
            if spot:
                ticket = self.tickets[vehicle]
                ticket.unpark()
                return ticket
