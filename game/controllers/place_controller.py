from game.common.enums import *
from game.common.map.game_board import GameBoard
from game.common.map.tile import Tile
from game.common.player import Player
from game.controllers.controller import Controller
from game.quarry_rush.entity.placeable.dynamite import Dynamite
from game.quarry_rush.entity.placeable.traps import Landmine, EMP, Trap
from game.utils.vector import Vector


class PlaceController(Controller):
    def __init__(self) -> None:
        super().__init__()

    def handle_actions(self, action: ActionType, client: Player, world: GameBoard) -> None:
        ...

    def __place_dynamite(self, client: Player, tile: Tile, world: GameBoard) -> None:
        ...

    def __place_landmine(self, client: Player, tile: Tile, world: GameBoard) -> None:
        ...

    def __place_emp(self, client: Player, tile: Tile, world: GameBoard) -> None:
        ...

    def __add_to_trap_queue(self, client: Player, world: GameBoard, placed_object: Trap) -> None:
        ...
