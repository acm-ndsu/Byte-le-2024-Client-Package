from __future__ import annotations

from game.common.game_object import GameObject
from game.common.enums import ObjectType
from typing import Self, Tuple


class Vector(GameObject):

    def __init__(self, x: int = 0, y: int = 0):
        super().__init__()
        self.object_type: ObjectType = ObjectType.VECTOR
        self.x = x
        self.y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int) -> None:
        if x is None or not isinstance(x, int):
            raise ValueError(f"The given x value, {x}, is not an integer.")
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int) -> None:
        if y is None or not isinstance(y, int):
            raise ValueError(f"The given y value, {y}, is not an integer.")
        self.__y = y

    @staticmethod
    def add_vectors(vector_1: 'Vector', vector_2: 'Vector') -> 'Vector':
        ...

    @staticmethod
    def from_xy_tuple(xy_tuple: Tuple[int, int]) -> 'Vector':
        ...

    @staticmethod
    def from_yx_tuple(yx_tuple: Tuple[int, int]) -> 'Vector':
        ...

    def add_to_vector(self, other_vector: Self) -> None:
        ...

    def add_x_y(self, x: int, y: int) -> None:
        ...

    def add_x(self, x: int) -> None:
        ...

    def add_y(self, y: int) -> None:
        ...

    def as_tuple(self) -> Tuple[int, int]:
        ...

    def to_json(self) -> dict:
        ...

    def from_json(self, data) -> Self:
        ...

    def __str__(self) -> str:
        ...
    
    def length(self) -> int:
        ...
    
    def negative(self) -> Self:
        ...
    
    def distance(self, other_vector: Vector) -> int:
        ...
