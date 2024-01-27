from game.common.enums import ActionType
from game.common.map.game_board import GameBoard
from game.common.player import Player
from game.controllers.controller import Controller
from game.utils.vector import Vector
from game.config import TRAP_DEFUSAL_RANGE


class DefuseController(Controller):
    def __init__(self) -> None:
        super().__init__()
        
    def handle_actions(self, action: ActionType, client: Player, world: GameBoard):
        ...
