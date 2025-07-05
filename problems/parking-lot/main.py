import time
from parking_lot import ParkingLot
from level import Level

from vehicle.vehicle_type import VehicleType
from vehicle.car import Car
from vehicle.bus import Bus
from vehicle.motorcycle import Motorcycle

from billing.hourly_billing import HourlyBilling
from billing.overnight_billing import OvernightBilling

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
    [parking_lot.park(vehicle, HourlyBilling()) for vehicle in [car_1, car_2, motorcycle_1, motorcycle_2]]
    [parking_lot.park(vehicle, OvernightBilling()) for vehicle in [bus_1, bus_2]]

    # wait for a while
    time.sleep(10)

    # unpark the vehicles
    [parking_lot.unpark(vehicle) for vehicle in [car_1, car_2, bus_1, bus_2, motorcycle_1, motorcycle_2]]

    # get bills for the vehicles
    for vehicle in [car_1, car_2, bus_1, bus_2, motorcycle_1, motorcycle_2]:
        bill = parking_lot.get_bill(vehicle)
        print(f">>> Bill for {vehicle.license} = ${bill}")

if __name__ == "__main__":
    main()
