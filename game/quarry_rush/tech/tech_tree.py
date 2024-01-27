from __future__ import annotations
from typing import Callable, TypeVar, Generic, Self
from game.quarry_rush.tech.tech import Tech, techs, TechInfo
from game.quarry_rush.avatar.avatar_functions import AvatarFunctions
from functools import reduce
from game.common.game_object import GameObject

T = TypeVar('T')
E = TypeVar('E')


class Tree(Generic[T]):
    def __init__(self, value: T, subs: list[Tree[T]]):
        self.value = value
        self.subs = subs

    def fmap(self, func: Callable[[T], E]) -> Tree[E]:
        ...


class TechTree(GameObject):

    def __init__(self, avatar_functions: AvatarFunctions):
        super().__init__()
        self.avatar_functions = avatar_functions
        self.tree = self.build_tree(avatar_functions)
        self.research('Mining Robotics')

    def tech_names(self) -> list[str]:
        ...

    def researched_techs(self) -> list[str]:
        ...

    def is_researched(self, tech_name: str) -> bool:
        ...

    def research(self, tech_name: str) -> bool:
        ...

    def tech_info(self, tech_name: str) -> TechInfo | None:
        ...

    def score(self) -> int:
        ...

    def build_tree(self, avatar_functions: AvatarFunctions) -> Tree[tuple[Tech, bool]]:
        ...

    def to_json(self) -> dict:
        ...

    def from_json(self, data: dict) -> Self:
        ...
