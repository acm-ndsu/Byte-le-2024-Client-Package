from game.common.stations.occupiable_station import OccupiableStation
from game.common.avatar import Avatar
from game.common.enums import Company
from game.quarry_rush.avatar.inventory_manager import InventoryManager
from game.common.enums import ObjectType
from typing import Self

from game.quarry_rush.entity.placeable.dynamite import Dynamite
from game.quarry_rush.entity.placeable.traps import Landmine, EMP


class CompanyStation(OccupiableStation):

    def __init__(self, company: Company):
        super().__init__()
        self.company: Company = company
        self.object_type = ObjectType.COMPANY_STATION

    # company getter and setter methods
    @property
    def company(self) -> Company:
        return self.__company

    @company.setter
    def company(self, company: Company) -> None:
        if company is None or not isinstance(company, Company):
            raise ValueError(f'{self.__class__.__name__}.company must be a Company.')
        self.__company = company

    def take_action(self, avatar: Avatar, inventory_manager: InventoryManager) -> None:
        ...

    def to_json(self) -> dict:
        ...

    def from_json(self, data: dict) -> Self:
        ...


class ChurchStation(CompanyStation):

    def __init__(self):
        super().__init__(Company.CHURCH)
        self.object_type = ObjectType.CHURCH_STATION


class TuringStation(CompanyStation):

    def __init__(self):
        super().__init__(Company.TURING)
        self.object_type = ObjectType.TURING_STATION
