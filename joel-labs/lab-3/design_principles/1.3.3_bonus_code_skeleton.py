from dataclasses import dataclass
from enum import Enum
from typing import List

class ShipmentType(Enum):
    plane = 0
    ship = 1
    car = 2
    carrier_pigeon = 3


@dataclass
class Size:
    width: float
    height: float
    weight: float


@dataclass
class Product:
    name: str
    price: float
    size: Size


@dataclass
class Address:
    country: str
    street_address: str
    city: str
    zip_code: int


@dataclass
class Person:
    name: str
    ssn: str
    address: Address


@dataclass
class Package:
    shipment_type: ShipmentType
    product: Product
    merchant: Person
    buyer: Person


class Ship:
    def reload_fuel_oil(self):
        print('reloading fuel supplies on ship')

    def ship(self, package: Package):
        print(f'shipping package via ship from {package.merchant.address} to {package.buyer.address}')


class Plane:
    def reload_jet_fuel(self):
        print('jet fuels can\'t melt steel beams')

    def fly(self, package: Package):
        print(f'flying package from {package.merchant.address} to {package.buyer.address}')


class Car:
    def reload_gas(self):
        print('adding gasoline... or diesel')

    def drive(self, package: Package):
        print(f'driving package from {package.merchant.address} to {package.buyer.address}')


class CarrierPigeon:
    def eat_seeds(self):
        print(f'beep beep I\'m a bird')

    def fly(self, package: Package):
        print(f'beep beep I\'m a bird')


class ShipmentService:
    def ship(self, package: Package):
        if package.shipment_type == ShipmentType.ship:
            ship = Ship()
            ship.reload_fuel_oil()
            ship.ship(package)

        elif package.shipment_type == ShipmentType.plane:
            plane = Plane()
            plane.reload_jet_fuel()
            plane.fly(package)

        elif package.shipment_type == ShipmentType.car:
            car = Car()
            car.reload_gas()
            car.drive(package)

        elif package.shipment_type == ShipmentType.carrier_pigeon:
            pigeon = CarrierPigeon()
            pigeon.eat_seeds()
            pigeon.fly(package)