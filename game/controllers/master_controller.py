from copy import deepcopy
import random

from game.common.action import Action
from game.common.avatar import Avatar
from game.common.enums import *
from game.common.player import Player
import game.config as config   # this is for turns
from game.controllers import dynamite_controller
from game.controllers.defuse_controller import DefuseController
from game.controllers.dynamite_controller import DynamiteController
from game.utils.thread import CommunicationThread
from game.controllers.movement_controller import MovementController
from game.controllers.controller import Controller
from game.controllers.interact_controller import InteractController
from game.controllers.mine_controller import MineController
from game.controllers.buy_tech_controller import BuyTechController
from game.controllers.place_controller import PlaceController
from game.common.map.game_board import GameBoard
from game.config import MAX_NUMBER_OF_ACTIONS_PER_TURN
from game.utils.vector import Vector 


class MasterController(Controller):

    def __init__(self):
        super().__init__()
        self.game_over: bool = False
        # self.event_timer = GameStats.event_timer   # anything related to events are commented it out until made
        # self.event_times: tuple[int, int] | None = None
        self.turn: int = 1
        self.current_world_data: dict = None
        self.movement_controller: MovementController = MovementController()
        self.interact_controller: InteractController = InteractController()
        self.dynamite_controller: DynamiteController = DynamiteController()
        self.defuse_controller: DefuseController = DefuseController()
        self.mine_controller: MineController = MineController()
        self.buy_tech_controller: BuyTechController = BuyTechController()
        self.place_controller: PlaceController = PlaceController()

    # Receives all clients for the purpose of giving them the objects they will control
    def give_clients_objects(self, clients: list[Player], world: dict):
        ...

    # Receives world data from the generated game log and is responsible for interpreting it
    def interpret_current_turn_data(self, clients: list[Player], world: dict, turn):
        ...

    # Receive a specific client and send them what they get per turn. Also obfuscates necessary objects.
    def client_turn_arguments(self, client: Player, turn):
        ...

    # Perform the main logic that happens per turn
    def turn_logic(self, clients: list[Player], turn):
        ...

        # during turn logic; handling controller logic
        for client in clients:
            ...

    # Return serialized version of game
    def create_turn_log(self, clients: list[Player], turn: int):
        ...

    # Gather necessary data together in results file
    def return_final_results(self, clients: list[Player], turn):
        ...
