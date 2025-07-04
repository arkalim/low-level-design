from typing import Optional

from vehicle.vehicle_type import VehicleType
from vehicle.vehicle import Vehicle
from spot import Spot

class Level():
    def __init__(self, spot_dist: dict[VehicleType, int]):
        self.spots: dict[VehicleType, list[Spot]] = {type: [] for type in VehicleType}
        for vehicle_type, spot_count in spot_dist.items():
            self.spots[vehicle_type] = [Spot(i+1, vehicle_type) for i in range(spot_count)]

    def park(self, vehicle: Vehicle) -> Optional[int]:
        for spot in self.spots[vehicle.type]:
            if spot.park(vehicle):
                return spot.number
        return
    
    def unpark(self, vehicle: Vehicle) -> Optional[int]:
        for spot in self.spots[vehicle.type]:
            if spot.vehicle == vehicle:
                spot.unpark()
                return spot.number
