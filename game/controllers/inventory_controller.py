from game.common.enums import *
from game.common.avatar import Avatar
from game.common.player import Player
from game.controllers.controller import Controller
from game.common.map.game_board import GameBoard


class InventoryController(Controller):

    def __init__(self):
        super().__init__()

    def handle_actions(self, action: ActionType, client: Player, world: GameBoard) -> None:
        ...
