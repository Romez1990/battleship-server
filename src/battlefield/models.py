from __future__ import annotations
from enum import Enum
from typing import (
    Callable,
    TypeVar,
)

from pydantic import BaseModel

T = TypeVar('T')


class Vector(BaseModel):
    x: int
    y: int

    def __add__(self, other: Vector) -> Vector:
        return Vector(x=self.x + other.x, y=self.y + other.y)


class Rectangle:
    def __init__(self, coordinates: Vector, size: Vector) -> None:
        self.__coordinates = coordinates
        self.__size = size
        self.__end_coordinates = coordinates + size

    @property
    def coordinates(self) -> Vector:
        return self.__coordinates

    @property
    def size(self) -> Vector:
        return self.__size

    @property
    def end_coordinates(self) -> Vector:
        return self.__end_coordinates

    def collides(self, other: object) -> bool:
        if isinstance(other, Rectangle):
            collides_on_x = self.coordinates.x < other.end_coordinates.x and other.coordinates.x < self.end_coordinates.x
            collides_on_y = self.coordinates.y < other.end_coordinates.y and other.coordinates.y < self.end_coordinates.y
            return collides_on_x and collides_on_y
        if isinstance(other, Vector):
            return self.collides(Rectangle(other, Vector(x=1, y=1)))
        raise Exception('collides is undefined')


class Orientation(Enum):
    horizontal = 0
    vertical = 1

    def switch(self, on_horizontal: Callable[[], T], on_vertical: Callable[[], T]) -> T:
        if self is Orientation.horizontal:
            return on_horizontal()
        if self is Orientation.vertical:
            return on_vertical()
        raise Exception('invalid orientation')


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

    def collides(self, coordinates: Vector) -> bool:
        ship_size = Rectangle(
            self.coordinates,
            self.orientation.switch(
                lambda: Vector(x=self.size, y=1),
                lambda: Vector(x=1, y=self.size),
            )
        )
        return ship_size.collides(coordinates)

    def hit(self, shop: Vector) -> None:
        self.__damaged_parts.append(shop)

    def is_destroyed(self) -> bool:
        return len(self.__damaged_parts) == self.size

    def to_ship(self) -> Ship:
        return Ship(coordinates=self.__coordinates, size=self.__size, orientation=self.__orientation)
