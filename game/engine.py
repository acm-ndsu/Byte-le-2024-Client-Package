import importlib
import json
import logging
import sys
import threading
import traceback
from datetime import datetime

from tqdm import tqdm

from game.common.map.game_board import GameBoard
from game.common.player import Player
from game.config import *
from game.controllers.master_controller import MasterController
from game.utils.helpers import write_json_file
from game.utils.thread import Thread, CommunicationThread
from game.utils.validation import verify_code, verify_num_clients
from game.client.user_client import UserClient


class Engine:
    def __init__(self, quiet_mode=False, use_filenames_as_team_names=False):
        self.clients = list()
        self.master_controller = MasterController()
        self.tick_number = 0

        self.game_logs = dict()
        self.world = None
        self.current_world_key = None

        self.quiet_mode = quiet_mode
        self.use_filenames = use_filenames_as_team_names

    # Starting point of the engine. Runs other methods then sits on top of a basic game loop until over
    def loop(self):
        ...

    # Finds, checks, and instantiates clients
    def boot(self):
        ...

    # Loads in the world
    def load(self):
        ...

    # Sits on top of all actions that need to happen before the player takes their turn
    def pre_tick(self):
        ...

    # Does actions like lets the player take their turn and asks master controller to perform game logic
    def tick(self):
        ...

    # Does any actions that need to happen after the game logic, then creates the game log for the turn
    def post_tick(self):
        ...

    # Attempts to safely handle an engine shutdown given any game state
    def shutdown(self, source=None):
        ...

    # Debug print statement
    def debug(*args):
        ...


if __name__ == '__main__':
    game = Engine()
    game.loop()
