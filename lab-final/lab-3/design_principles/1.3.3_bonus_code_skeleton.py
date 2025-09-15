from dataclasses import dataclass
from enum import Enum
from abc import ABC, abstractmethod

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


class Transport(ABC):
    @abstractmethod
    def prepare(self) -> None:
        pass

    @abstractmethod
    def deliver(self, package: Package) -> None:
        pass


class Ship(Transport):
    def prepare(self) -> None:
        print('reloading fuel supplies on ship')

    def deliver(self, package: Package) -> None:
        print(f'shipping package via ship from {package.merchant.address} to {package.buyer.address}')


class Plane(Transport):
    def prepare(self) -> None:
        print('jet fuels can\'t melt steel beams')

    def deliver(self, package: Package) -> None:
        print(f'flying package from {package.merchant.address} to {package.buyer.address}')


class Car(Transport):
    def prepare(self) -> None:
        print('adding gasoline... or diesel')

    def deliver(self, package: Package) -> None:
        print(f'driving package from {package.merchant.address} to {package.buyer.address}')


class CarrierPigeon(Transport):
    def prepare(self) -> None:
        print(f'beep beep I\'m a bird')

    def deliver(self, package: Package) -> None:
        print(f'beep beep I\'m a bird')


class ShipmentService:
    def ship(self, transport: Transport, package: Package) -> None:
        transport.prepare()
        transport.deliver(package)
