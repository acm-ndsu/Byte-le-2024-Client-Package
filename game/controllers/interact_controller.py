from game.common.enums import *
from game.common.game_object import GameObject
from game.controllers.controller import Controller
from game.common.player import Player
from game.common.stations.station import Station
from game.common.map.game_board import GameBoard
from game.utils.vector import Vector
from game.quarry_rush.station.ore_occupiable_station import OreOccupiableStation


class InteractController(Controller):

    def __init__(self):
        super().__init__()

    def handle_actions(self, action: ActionType, client: Player, world: GameBoard, target: GameObject | ObjectType = Station()) -> None:
        ...
