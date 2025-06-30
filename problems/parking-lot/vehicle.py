from abc import ABC
from vehicle_type import VehicleType

class Vehicle(ABC):
    def __init__(self, license: str, type: VehicleType):
        self.license = license
        self.type = type
