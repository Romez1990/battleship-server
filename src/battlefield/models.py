from enum import Enum
from pydantic import BaseModel


class Vector(BaseModel):
    x: int
    y: int


class Orientation(Enum):
    horizontal = 0
    vertical = 1


class Ship(BaseModel):
    coordinates: Vector
    size: int
    orientation: Orientation


class GameShip:
    def __init__(self, ship: Ship) -> None:
        self.__coordinates = ship.coordinates
        self.__size = ship.size
        self.__orientation = ship.orientation
        self.__damaged_parts: list[Vector] = []

    @property
    def coordinates(self) -> Vector:
        return self.__coordinates

    @property
    def size(self) -> int:
        return self.__size

    @property
    def orientation(self) -> Orientation:
        return self.__orientation

    def hit(self, shop: Vector) -> None:
        self.__damaged_parts.append(shop)

    @property
    def destroyed(self) -> bool:
        return self.__damaged_parts == self.size

    def to_ship(self) -> Ship:
        return Ship(coordinates=self.__coordinates, size=self.__size, orientation=self.__orientation)
