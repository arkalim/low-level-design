import time
from parking_lot import ParkingLot
from level import Level

from vehicle.vehicle_type import VehicleType
from vehicle.car import Car
from vehicle.bus import Bus
from vehicle.motorcycle import Motorcycle

from billing.hourly_billing import HourlyBilling
from billing.overnight_billing import OvernightBilling
from billing.daily_billing import DailyBilling

def main():
    # create a parking lot
    parking_lot = ParkingLot()

    # add 2 levels totalling 5 car, 2 motorcycle and 1 bus spots
    parking_lot.add_level(Level("A", {VehicleType.car: 3, VehicleType.motorcycle: 1}))
    parking_lot.add_level(Level("B", {VehicleType.car: 2, VehicleType.bus: 1, VehicleType.motorcycle: 1}))

    # create vehicles
    car_1 = Car("CAR1")
    bus_1 = Bus("BUS1")
    motorcycle_1 = Motorcycle("MOT1")

    car_2 = Car("CAR2")
    bus_2 = Bus("BUS2")
    motorcycle_2 = Motorcycle("MOT2")

    # billing option chosen by each vehicle
    vehicle_billing_map = {
        car_1: HourlyBilling(),
        car_2: DailyBilling(),
        motorcycle_1: OvernightBilling(),
        motorcycle_2: DailyBilling(),
        bus_1: OvernightBilling(),
        bus_2: HourlyBilling(),
    }

    # park the vehicles
    for vehicle, billing_strategy in vehicle_billing_map.items():
        ticket = parking_lot.park(vehicle, billing_strategy)
        if ticket:
            print(f">>> Parked {vehicle.type.name} with license {vehicle.license} at spot {ticket.spot.id}")
        else:
            print(f">>> Failed to park {vehicle.type.name} with license {vehicle.license} in the parking lot")

    # wait for a while
    time.sleep(3)

    # unpark the vehicles
    for vehicle in vehicle_billing_map:
        ticket = parking_lot.unpark(vehicle)
        if ticket:
            print(f">>> Unparked {vehicle.type.name} with license {vehicle.license} from spot {ticket.spot.id} | Bill: ${ticket.get_bill()}")
        else:
            print(f">>> Failed to unpark {vehicle.type.name} with license {vehicle.license} from the parking lot")

if __name__ == "__main__":
    main()
