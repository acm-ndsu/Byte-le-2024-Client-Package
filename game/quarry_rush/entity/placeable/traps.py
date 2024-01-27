from game.common.stations.occupiable_station import OccupiableStation
from game.utils.vector import Vector
from game.common.enums import *
from game.quarry_rush.avatar.inventory_manager import InventoryManager
from game.config import LANDMINE_STEAL_RATE, EMP_STEAL_RATE, LANDMINE_RANGE, EMP_RANGE
from typing import Self
from typing import Callable


class Trap(OccupiableStation):

    def __init__(self, steal_rate: float = 0.0,
                 owner_company: Company = Company.CHURCH, target_company: Company = Company.TURING,
                 opponent_position: Callable[[], Vector] = lambda: Vector(), position: Vector = Vector(), range: int = 1):
        super().__init__()
        # rate for stealing items from opposing avatar when trap detonates (if none, pass 0.0)
        self.steal_rate: float = steal_rate
        # company of the owner of the trap
        self.owner_company: Company = owner_company
        # company of the target
        self.target_company: Company = target_company
        # function that returns Vector of opponent position
        self.opponent_position: Callable[[], Vector] = opponent_position
        # the position of the trap
        self.position: Vector = position
        # the range for detonation of a trap
        self.range: int = range
        # assigning the object type
        self.object_type: ObjectType = ObjectType.TRAP

    @property
    def steal_rate(self) -> float:
        return self.__steal_rate

    @property
    def owner_company(self) -> Company:
        return self.__owner_company

    @property
    def target_company(self) -> Company:
        return self.__target_company

    @property
    def opponent_position(self) -> Callable[[], Vector]:
        return self.__opponent_position

    @property
    def position(self) -> Vector:
        return self.__position

    @property
    def range(self) -> int:
        return self.__range

    @steal_rate.setter
    def steal_rate(self, steal_rate: float) -> None:
        if steal_rate is None or not isinstance(steal_rate, float):
            raise ValueError(
                f'{self.__class__.__name__}.steal_rate must be a float.')
        self.__steal_rate = steal_rate

    @opponent_position.setter
    def opponent_position(self, opponent_position: Callable[[], Vector]) -> None:
        try:
            if not isinstance(opponent_position, Callable):
                raise Exception
            if not isinstance(opponent_position(), Vector):
                raise Exception
        except:
            raise ValueError(
                f'{self.__class__.__name__}.opponent_position must be of type Callable[[], Vector].'
            )

        self.__opponent_position = opponent_position

    @position.setter
    def position(self, position: Vector) -> None:
        if position is None or not isinstance(position, Vector):
            raise ValueError(
                f'{self.__class__.__name__}.position must be a Vector.')
        self.__position = position

    @range.setter
    def range(self, range: int) -> None:
        if range is None or not isinstance(range, int):
            raise ValueError(
                f'{self.__class__.__name__}.range must be an int.')
        self.__range = range

    @owner_company.setter
    def owner_company(self, owner_company: Company) -> None:
        if owner_company is None or not isinstance(owner_company, Company):
            raise ValueError(
                f'{self.__class__.__name__}.owner_company must be of enum type Company.')
        self.__owner_company = owner_company

    @target_company.setter
    def target_company(self, target_company: Company) -> None:
        if target_company is None or not isinstance(target_company, Company):
            raise ValueError(
                f'{self.__class__.__name__}.target_company must be of enum type Company.')
        self.__target_company = target_company

    # in_range method, checks to see if opposing player is in range of detonating a trap
    def in_range(self) -> bool:
        ...

    # detonation method, calls in_range and steal to detonate trap
    def detonate(self, inventory_manager: InventoryManager) -> bool:
        ...

    # json methods
    def to_json(self) -> dict:
        ...

    def from_json(self, data: dict) -> Self:
        ...


# default classes for Landmine and EMP with existing detection_reduction and steal_rate

class Landmine(Trap):

    def __init__(self, owner_company: Company = Company.CHURCH, target_company: Company = Company.TURING,
                 opponent_position: Callable[[], Vector] = lambda: Vector(), position: Vector = Vector()):
        super().__init__(LANDMINE_STEAL_RATE, owner_company, target_company, opponent_position, position,
                         LANDMINE_RANGE)
        self.object_type: ObjectType = ObjectType.LANDMINE


class EMP(Trap):

    def __init__(self, owner_company: Company = Company.CHURCH, target_company: Company = Company.TURING,
                 opponent_position: Callable[[], Vector] = lambda: Vector(), position: Vector = Vector()):
        super().__init__(EMP_STEAL_RATE, owner_company, target_company, opponent_position, position, EMP_RANGE)
        self.object_type: ObjectType = ObjectType.EMP
