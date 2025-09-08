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

# if __name__ == "__main__":
#     address1 = Address("Iceland", "Main St 1", "Reykjavik", 101)
#     address2 = Address("Iceland", "Harbor St 5", "Akureyri", 600)
#     merchant = Person("Alice", "1234567890", address1)
#     buyer = Person("Bob", "0987654321", address2)
#     size = Size(10, 20, 5)
#     product = Product("Book", 29.99, size)
#     package = Package(ShipmentType.plane, product, merchant, buyer)
#     package2 = Package(ShipmentType.car, product, merchant, buyer)
#     package3 = Package(ShipmentType.carrier_pigeon, product, merchant, buyer)

#     service = ShipmentService()
#     transport = Plane()
#     transport2 = Car()
#     transport3 = CarrierPigeon()
#     service.ship(transport, package)
#     service.ship(transport2, package2)
#     service.ship(transport3, package3)