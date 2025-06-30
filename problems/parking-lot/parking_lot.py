from level import Level
from vehicle import Vehicle

class ParkingLot():
    def __init__(self):
        self.levels: list[Level] = []

    def add_level(self, level: Level):
        self.levels.append(level)

    def park(self, vehicle: Vehicle) -> bool:
        for i, level in enumerate(self.levels):
            spot_number = level.park(vehicle)
            if spot_number is not None:
                print(f">>> Parked {vehicle.type.name} with license {vehicle.license} in level {i+1} at spot number {spot_number}")
                return True
        print(f">>> Failed to park {vehicle.type.name} with license {vehicle.license} in the parking lot")
        return False
    
    def unpark(self, vehicle: Vehicle) -> bool:
        for i, level in enumerate(self.levels):
            spot_number = level.unpark(vehicle)
            if spot_number:
                print(f">>> Unparked {vehicle.type.name} with license {vehicle.license} from level {i+1} at spot number {spot_number}")
                return True
        print(f">>> Failed to unpark {vehicle.type.name} with license {vehicle.license} from the parking lot")
        return False