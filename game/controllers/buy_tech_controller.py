from game.common.game_object import GameObject
from game.common.player import Player
from game.common.map.game_board import GameBoard
from game.common.map.tile import Tile
from game.common.enums import *
from game.quarry_rush.station.company_station import CompanyStation
from game.utils.vector import Vector
from game.controllers.controller import Controller


class BuyTechController(Controller):
    def __init__(self):
        super().__init__()

    def handle_actions(self, action: ActionType, client: Player, world: GameBoard):
        ...

    def __is_on_home_base(self, client: Player, world: GameBoard):
        ...
