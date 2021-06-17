from pydantic import BaseModel


class Vector(BaseModel):
    x: int
    y: int


class Ship(BaseModel):
    coordinates: Vector
    size: int
    orientation: int
