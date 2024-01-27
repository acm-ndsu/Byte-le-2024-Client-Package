from game.common.enums import DebugLevel, ActionType
from game.config import Debug
from game.common.player import Player
from game.common.map.game_board import GameBoard
import logging


class Controller:
    def __init__(self):
        self.debug_level = DebugLevel.CONTROLLER
        self.debug = False

    def handle_actions(self, action: ActionType, client: Player, world: GameBoard):
        ...

    def debug(self, *args):
        ...
