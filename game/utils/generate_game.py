import random
from game.common.avatar import Avatar
from game.utils.vector import Vector
from game.config import *
from game.utils.helpers import write_json_file
from game.common.map.game_board import GameBoard
from game.quarry_rush.map.map_generator import MapGenerator


def generate(seed: int = random.randint(0, 1000000000)):
    ...
