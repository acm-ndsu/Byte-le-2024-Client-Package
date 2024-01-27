from json import load

from game.quarry_rush.map.collectable.collectable_weights_dict import COLLECTABLE_WEIGHTS
from game.utils.vector import Vector
from game.quarry_rush.station.ore_occupiable_station import OreOccupiableStation
from game.config import ORE_COUNT
import random as rand
import numpy as np
from perlin_noise import PerlinNoise


class CollectableGenerator:
    __board_size = 14  # This includes the borders. Field is 12x12
    __ore_count = ORE_COUNT

    def __init__(self, seed: int = rand.randint(0, 8675309)):
        collectable_weights = COLLECTABLE_WEIGHTS
        self.__ore_weights = collectable_weights['ore']
        self.__special_weights = collectable_weights['special']
        self.__ancient_tech_weights = collectable_weights['ancient_tech']
        self.__seed = seed

    def generate(self) -> dict[tuple[Vector], list[OreOccupiableStation]]:
        ...

    def generate_random_noise(self) -> list[list[float]]:
        ...

    def generate_perlin_noise(self) -> list[list[float]]:
        ...

    def adjust(self, raw: list[list[float]]) -> list[list[float]]:
        ...

    def layer(self, layer1: list[list[float]], layer2: list[list[float]]) -> list[list[float]]:
        ...

    def map_threshold(self, threshold: float, weight_map: list[list[float]]) -> list[list[bool]]:
        ...
