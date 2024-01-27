from __future__ import annotations

import random
from typing import Self, Callable

from game.common.avatar import Avatar
from game.common.enums import *
from game.common.game_object import GameObject
from game.common.map.tile import Tile
from game.common.map.wall import Wall
from game.common.stations.occupiable_station import OccupiableStation
from game.common.stations.station import Station
from game.quarry_rush.avatar.inventory_manager import InventoryManager
from game.quarry_rush.entity.placeable.dynamite import Dynamite
from game.quarry_rush.station.ore_occupiable_station import OreOccupiableStation
from game.utils.vector import Vector
from game.quarry_rush.entity.placeable.traps import Trap
from game.quarry_rush.station.company_station import TuringStation, ChurchStation
from game.quarry_rush.entity.placeable.traps import EMP, Landmine


class TrapQueue(GameObject):
    def __init__(self):
        super().__init__()
        self.__traps: list[Trap | None] = []
        self.__max_traps = 10

    def add_trap(self, trap: Trap, remove_trap_at: Callable[[Vector], None]):
        ...

    def detonate(self, inventory_manager: InventoryManager, remove_trap_at: Callable[[Vector], None], avatar: Avatar) -> None:
        ...

    def dequeue_trap_at(self, position: Vector):
        ...

    def size(self) -> int:
        ...

    def to_json(self):
        ...

    def from_json(self, data: dict) -> Self:
        ...


class DynamiteList(GameObject):

    def __init__(self):
        super().__init__()
        self.__dynamite_list: list[Dynamite] = []

    def add_dynamite(self, dynamite: Dynamite):
        ...

    def detonate(self):
        ...

    def size(self) -> int:
        ...

    def get_from_list(self, index: int) -> Dynamite:
        ...

    def to_json(self) -> dict:
        ...

    def from_json(self, data: dict) -> Self:
        ...


class GameBoard(GameObject):

    def __init__(self, seed: int | None = None, map_size: Vector = Vector(),
                 locations: dict[tuple[Vector]:list[GameObject]] | None = None, walled: bool = False):

        super().__init__()
        # game_map is initially going to be None. Since generation is slow, call generate_map() as needed
        self.game_map: list[list[Tile]] | None = None
        self.seed: int | None = seed
        random.seed(seed)
        self.object_type: ObjectType = ObjectType.GAMEBOARD
        self.event_active: int | None = None
        self.map_size: Vector = map_size
        # when passing Vectors as a tuple, end the tuple of Vectors with a comma so it is recognized as a tuple
        self.locations: dict | None = locations
        self.walled: bool = walled
        self.inventory_manager: InventoryManager = InventoryManager()
        self.church_trap_queue = TrapQueue()
        self.turing_trap_queue = TrapQueue()
        self.dynamite_list: DynamiteList = DynamiteList()

    @property
    def seed(self) -> int:
        return self.__seed

    @seed.setter
    def seed(self, seed: int | None) -> None:
        if self.game_map is not None:
            raise RuntimeError(f'{self.__class__.__name__} variables cannot be changed once generate_map is run.')
        if seed is not None and not isinstance(seed, int):
            raise ValueError(f'{self.__class__.__name__}.seed must be an integer or None.')
        self.__seed = seed

    @property
    def game_map(self) -> list[list[Tile]] | None:
        return self.__game_map

    @game_map.setter
    def game_map(self, game_map: list[list[Tile]]) -> None:
        if game_map is not None and (not isinstance(game_map, list) or
                                     any(map(lambda l: not isinstance(l, list), game_map)) or
                                     any([any(map(lambda g: not isinstance(g, Tile), tile_list))
                                          for tile_list in game_map])):
            raise ValueError(f'{self.__class__.__name__}.game_map must be a list[list[Tile]].')
        self.__game_map = game_map

    @property
    def map_size(self) -> Vector:
        return self.__map_size

    @map_size.setter
    def map_size(self, map_size: Vector) -> None:
        if self.game_map is not None:
            raise RuntimeError(f'{self.__class__.__name__} variables cannot be changed once generate_map is run.')
        if map_size is None or not isinstance(map_size, Vector):
            raise ValueError(f'{self.__class__.__name__}.map_size must be a Vector.')
        self.__map_size = map_size

    @property
    def locations(self) -> dict:
        return self.__locations

    @locations.setter
    def locations(self, locations: dict[tuple[Vector]:list[GameObject]] | None) -> None:
        if self.game_map is not None:
            raise RuntimeError(f'{self.__class__.__name__} variables cannot be changed once generate_map is run.')
        if locations is not None and not isinstance(locations, dict):
            raise ValueError("Locations must be a dict. The key must be a tuple of Vector Objects, and the "
                             "value a list of GameObject.")
        # if locations is not None:
        #     for k, v in locations.items():
        #         if len(k) != len(v):
        #             raise ValueError("Cannot set the locations for the game_board. A key has a different "
        #                              "length than its key.")

        self.__locations = locations

    @property
    def walled(self) -> bool:
        return self.__walled

    @walled.setter
    def walled(self, walled: bool) -> None:
        if self.game_map is not None:
            raise RuntimeError(f'{self.__class__.__name__} variables cannot be changed once generate_map is run.')
        if walled is None or not isinstance(walled, bool):
            raise ValueError(f'{self.__class__.__name__}.walled must be a bool.')

        self.__walled = walled

    def generate_map(self) -> None:
        ...

    def __populate_map(self) -> None:
        ...

    def __occupied_filter(self, game_object_list: list[GameObject]) -> list[GameObject]:
        """
        A helper method that returns a list of game objects that have the 'occupied_by' attribute.
        :param game_object_list:
        :return: a list of game object
        """
        ...

    def __help_populate(self, vector_list: list[Vector], game_object_list: list[GameObject]) -> None:
        """
        A helper method that helps populate the game map.
        :param vector_list:
        :param game_object_list:
        :return: None
        """

        ...

# Returns the Vector and a list of GameObject for whatever objects you are trying to get
    def get_objects(self, look_for: ObjectType) -> list[tuple[Vector, list[GameObject]]]:
        ...

# Add the objects to the end of to_return (a list of GameObject)
    def __get_objects_help(self, look_for: ObjectType, temp: GameObject | Tile, to_return: list[GameObject]):
        ...

    def to_json(self) -> dict:
        ...

    def generate_event(self, start: int, end: int) -> None:
        ...

    def __from_json_helper(self, data: dict) -> GameObject:
        ...

    def from_json(self, data: dict) -> Self:
        ...

    # removes trap from game_map based on position, method called in trap queue detonate method
    def remove_trap_at(self, position: Vector) -> None:
        ...

    def trap_detonation_control(self, avatars: dict[Company, Avatar]) -> None:
        ...

    def dynamite_detonation_control(self):
        ...
        
    def defuse_trap_at(self, position: Vector) -> None:
        ...
