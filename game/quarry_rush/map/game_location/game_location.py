from json import load

from game.quarry_rush.map.game_location.game_location_dict import GAME_LOCATION
from game.utils.vector import Vector
from game.common.game_object import GameObject
from game.common.map.wall import Wall
from game.quarry_rush.station.company_station import ChurchStation, TuringStation
from game.common.enums import Company
from game.common.avatar import Avatar


class GameLocation:

    def __init__(self):
        game_location: dict = GAME_LOCATION

        self.__walls: dict = game_location['walls']
        self.__turing_bases: dict = game_location['turing_bases']
        self.__church_bases: dict = game_location['church_bases']
        self.__avatars: dict = game_location['avatars']

    def generate_location(self) -> dict[tuple[Vector]: list[GameObject]]:
        ...
