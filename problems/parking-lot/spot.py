from typing import Optional
from vehicle.vehicle_type import VehicleType
from vehicle.vehicle import Vehicle

class Spot():
    def __init__(self, id: str, type: VehicleType):
        self.id = id
        self.type = type
        self.vehicle: Optional[Vehicle] = None

    def park(self, vehicle: Vehicle) -> bool:
        if not self.vehicle and self.type == vehicle.type:
            self.vehicle = vehicle
            return True
        return False

    def unpark(self) -> bool:
        if self.vehicle:
            self.vehicle = None

            return True
        return False
