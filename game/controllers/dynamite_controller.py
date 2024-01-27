from __future__ import annotations

from game.common.enums import *
from game.common.map.game_board import GameBoard
from game.common.map.tile import Tile
from game.controllers.controller import Controller
from game.quarry_rush.entity.placeable.dynamite import Dynamite
from game.quarry_rush.station.ore_occupiable_station import OreOccupiableStation
from game.utils.vector import Vector


class DynamiteController(Controller):
    def __init__(self) -> None:
        super().__init__()

    def handle_detonation(self, dynamite: Dynamite, world: GameBoard) -> None:
        ...
