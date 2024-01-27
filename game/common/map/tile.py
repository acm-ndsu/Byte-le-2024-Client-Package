from typing import Self

from game.common.avatar import Avatar
from game.common.enums import ObjectType
from game.common.game_object import GameObject
from game.common.map.occupiable import Occupiable
from game.common.map.wall import Wall
from game.common.stations.station import Station
from game.common.stations.occupiable_station import OccupiableStation
from game.quarry_rush.entity.placeable.dynamite import Dynamite
from game.quarry_rush.entity.placeable.traps import EMP, Landmine
from game.quarry_rush.station.company_station import ChurchStation, TuringStation


class Tile(Occupiable):

    def __init__(self, occupied_by: GameObject = None):
        super().__init__(occupied_by)
        self.object_type: ObjectType = ObjectType.TILE

    def from_json(self, data: dict) -> Self:
        ...
