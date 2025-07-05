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

    def park(self, vehicle: Vehicle, billing_strategy: BillingStrategy) -> bool:
        for i, level in enumerate(self.levels):
            spot = level.park(vehicle)
            if spot:
                self.tickets[vehicle] = Ticket(vehicle, spot, billing_strategy)
                print(f">>> Parked {vehicle.type.name} with license {vehicle.license} in level {i+1} at spot number {spot.number}")
                return True
        print(f">>> Failed to park {vehicle.type.name} with license {vehicle.license} in the parking lot")
        return False
    
    def unpark(self, vehicle: Vehicle) -> bool:
        for i, level in enumerate(self.levels):
            spot = level.unpark(vehicle)
            if spot:
                self.tickets[vehicle].unpark()
                print(f">>> Unparked {vehicle.type.name} with license {vehicle.license} from level {i+1} at spot number {spot.number}")
                return True
        print(f">>> Failed to unpark {vehicle.type.name} with license {vehicle.license} from the parking lot")
        return False
    
    def get_bill(self, vehicle: Vehicle) -> float:
        if vehicle not in self.tickets:
            return 0
        return self.tickets[vehicle].get_bill()
