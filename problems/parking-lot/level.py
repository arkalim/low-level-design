from typing import Optional

from vehicle.vehicle_type import VehicleType
from vehicle.vehicle import Vehicle
from spot import Spot

class Level():
    def __init__(self, id: str, spot_dist: dict[VehicleType, int]):
        self.id = id
        self.spots: dict[VehicleType, list[Spot]] = {type: [] for type in VehicleType}
        for vehicle_type, spot_count in spot_dist.items():
            self.spots[vehicle_type] = [Spot(f"{self.id}{i}", vehicle_type) for i in range(spot_count)]

    def park(self, vehicle: Vehicle) -> Optional[Spot]:
        for spot in self.spots[vehicle.type]:
            if spot.park(vehicle):
                return spot
    
    def unpark(self, vehicle: Vehicle) -> Optional[Spot]:
        for spot in self.spots[vehicle.type]:
            if spot.vehicle == vehicle:
                spot.unpark()
                return spot
