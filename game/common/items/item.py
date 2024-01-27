from game.common.enums import ObjectType
from game.common.game_object import GameObject
from game.utils.vector import Vector
from typing import Self


class Item(GameObject):

    def __init__(self, value: int = 0, science_point_value: int = 0, quantity: int = 1, stack_size: int = 1,
                 durability: int | None = None, position: Vector | None = None, name: str | None = None):
        super().__init__()
        self.__quantity = None  # This is here to prevent an error
        self.__durability = None  # This is here to prevent an error
        self.science_point_value: int = science_point_value #Science point value of an item
        self.object_type: ObjectType = ObjectType.ITEM
        self.value: int = value  # Value can more specified based on purpose (e.g., the sell price)
        self.stack_size: int = stack_size  # the max quantity this item can contain
        self.durability: int | None = durability  # durability can be None to represent infinite durability
        self.quantity: int = quantity  # the current amount of this item
        self.position: Vector | None = position  # position of item
        self.name: str | None = name  # name affiliated with item

    @property
    def durability(self) -> int | None:
        return self.__durability

    @property
    def value(self) -> int :
        return self.__value
    @property
    def science_point_value(self) -> int :
        return self.__science_point_value
    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def stack_size(self) -> int:
        return self.__stack_size
    
    @property
    def position(self) -> Vector | None:
        return self.__position
    
    @property
    def name(self) -> str | None:
        return self.__name

    @durability.setter
    def durability(self, durability: int | None) -> None:
        if durability is not None and not isinstance(durability, int):
            raise ValueError(f'{self.__class__.__name__}.durability must be an int or None.')
        if durability is not None and self.stack_size != 1:
            raise ValueError(
                f'{self.__class__.__name__}.durability must be set to None if stack_size is not equal to 1.')
        self.__durability = durability

    @value.setter
    def value(self, value: int) -> None:
        if value is None or not isinstance(value, int):
            raise ValueError(f'{self.__class__.__name__}.value must be an int.')
        self.__value: int = value

    @science_point_value.setter
    def science_point_value(self, science_point_value: int) -> None:
        if science_point_value is None or not isinstance(science_point_value, int):
            raise ValueError(f'{self.__class__.__name__}.science_point_value must be an int.')
        self.__science_point_value: int = science_point_value

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        if quantity is None or not isinstance(quantity, int):
            raise ValueError(f'{self.__class__.__name__}.quantity must be an int.')
        if quantity < 0:
            raise ValueError(f'{self.__class__.__name__}.quantity must be greater than or equal to 0.')

        # The self.quantity is set to the lower value between stack_size and the given quantity
        # The remaining given quantity is returned if it's larger than self.quantity
        if quantity > self.stack_size:
            raise ValueError(f'{self.__class__.__name__}.quantity cannot be greater than '
                             f'{self.__class__.__name__}.stack_size')
        self.__quantity: int = quantity

    @stack_size.setter
    def stack_size(self, stack_size: int) -> None:
        if stack_size is None or not isinstance(stack_size, int):
            raise ValueError(f'{self.__class__.__name__}.stack_size must be an int.')
        if self.durability is not None and stack_size != 1:
            raise ValueError(f'{self.__class__.__name__}.stack_size must be 1 if {self.__class__.__name__}.durability '
                             f'is not None.')
        if self.__quantity is not None and stack_size < self.__quantity:
            raise ValueError(f'{self.__class__.__name__}.stack_size must be greater than or equal to the quantity.')
        self.__stack_size: int = stack_size

    @position.setter
    def position(self, position: Vector | None) -> None:
        if position is not None and not isinstance(position, Vector):
            raise ValueError(f'{self.__class__.__name__}.position must be a Vector or None.')
        self.__position: Vector | None = position

    @name.setter
    def name(self, name: str | None) -> None:
        if name is not None and not isinstance(name, str):
            raise ValueError(f'{self.__class__.__name__}.name must be a str or None.')
        self.__name: str | None = name

    def take(self, item: Self) -> Self | None:
        ...

    def pick_up(self, item: Self) -> Self | None:
        ...

    def to_json(self) -> dict:
        ...

    def from_json(self, data: dict) -> Self:
        ...
