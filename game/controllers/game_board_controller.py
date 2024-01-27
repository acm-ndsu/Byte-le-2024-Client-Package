from game.common.map.game_board import GameBoard
from game.controllers.controller import Controller
from game.controllers.dynamite_controller import DynamiteController


class GameBoardController(Controller):

    def __init__(self, world: GameBoard):
        super().__init__()
        self.dynamite_controller = DynamiteController()  # used to manage explosions and collections
        self.world: GameBoard = world

    def pre_tick(self) -> None:
        ...

    def post_tick(self) -> None:
        ...
