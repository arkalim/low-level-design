from vehicle_type import VehicleType
from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, license: str):
        super().__init__(license, VehicleType.motorcycle)
