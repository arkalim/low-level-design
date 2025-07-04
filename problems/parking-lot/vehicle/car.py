from .vehicle_type import VehicleType
from .vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, license: str):
        super().__init__(license, VehicleType.car)
