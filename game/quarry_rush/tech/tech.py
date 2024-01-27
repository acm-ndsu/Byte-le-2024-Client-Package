from typing import Callable
from game.quarry_rush.avatar.avatar_functions import AvatarFunctions
from game.config import IMPROVED_DRIVETRAIN_COST, SUPERIOR_DRIVETRAIN_COST, OVERDRIVE_DRIVETRAIN_COST, LANDMINE_COST, \
    EMP_COST, IMPROVED_MINING_COST, SUPERIOR_MINING_COST, OVERDRIVE_MINING_COST, DYNAMITE_COST, TRAP_DEFUSAL_COST, \
    IMPROVED_DRIVETRAIN_POINTS, SUPERIOR_DRIVETRAIN_POINTS, OVERDRIVE_DRIVETRAIN_POINTS, IMPROVED_MINING_POINTS, \
    SUPERIOR_MINING_POINTS, OVERDRIVE_MINING_POINTS, DYNAMITE_POINTS, LANDMINE_POINTS, EMP_POINTS, TRAP_DEFUSAL_POINTS


class Tech:

    def __init__(self, name: str, cost: int, point_value: int, apply: Callable[[], None]):
        self.name = name
        self.cost = cost
        self.point_value = point_value
        self.apply = apply


class TechInfo:

    def __init__(self, name: str, cost: int, point_value: int):
        self.name = name
        self.cost = cost
        self.point_value = point_value


def techs(avatar_functions: AvatarFunctions) -> dict[str, Tech]:
    ...
