from vehicle_type import VehicleType
from parking_lot import ParkingLot
from level import Level

from car import Car
from bus import Bus
from motorcycle import Motorcycle

def main():
    # create a parking lot
    parking_lot = ParkingLot()

    # add 2 levels totalling 5 car, 2 motorcycle and 1 bus spots
    parking_lot.add_level(Level({VehicleType.car: 3, VehicleType.motorcycle: 1}))
    parking_lot.add_level(Level({VehicleType.car: 2, VehicleType.bus: 1, VehicleType.motorcycle: 1}))

    # create vehicles
    car_1 = Car("CAR1")
    bus_1 = Bus("BUS1")
    motorcycle_1 = Motorcycle("MOT1")

    car_2 = Car("CAR2")
    bus_2 = Bus("BUS2")
    motorcycle_2 = Motorcycle("MOT2")

    # park the vehicles
    [parking_lot.park(vehicle) for vehicle in [car_1, car_2, bus_1, bus_2, motorcycle_1, motorcycle_2]]

    # unpark the vehicles
    [parking_lot.unpark(vehicle) for vehicle in [car_1, car_2, bus_1, bus_2, motorcycle_1, motorcycle_2]]

if __name__ == "__main__":
    main()
