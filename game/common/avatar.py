from typing import Self

from game.common.enums import ObjectType, Company, Tech
from game.common.game_object import GameObject
from game.quarry_rush.ability.emp_active_ability import EMPActiveAbility
from game.quarry_rush.ability.landmine_active_ability import LandmineActiveAbility
from game.quarry_rush.ability.trap_defusal_active_ability import TrapDefusalActiveAbility
from game.quarry_rush.tech.tech import TechInfo
from game.utils.vector import Vector
from game.quarry_rush.tech.tech_tree import TechTree
from game.quarry_rush.avatar.avatar_functions import AvatarFunctions
from game.quarry_rush.ability.dynamite_active_ability import DynamiteActiveAbility


class Avatar(GameObject):

    def __init__(self, company: Company = Company.CHURCH, position: Vector | None = None):
        super().__init__()
        self.object_type: ObjectType = ObjectType.AVATAR
        self.score: int = 0
        self.science_points: int = 0
        self.position: Vector | None = position
        self.movement_speed: int = 1  # determines how many tiles the player moves
        self.drop_rate: int = 1  # determines how many items are dropped after mining
        self.abilities: dict = self.__create_abilities_dict()  # used to manage unlocking new abilities
        self.__tech_tree: TechTree = self.__create_tech_tree()  # the tech tree cannot be set; made private for security
        self.__company: Company = company
        self.dynamite_active_ability: DynamiteActiveAbility = DynamiteActiveAbility()
        self.landmine_active_ability: LandmineActiveAbility = LandmineActiveAbility()
        self.emp_active_ability: EMPActiveAbility = EMPActiveAbility()
        self.trap_defusal_active_ability: TrapDefusalActiveAbility = TrapDefusalActiveAbility()

    @property
    def company(self) -> Company:
        return self.__company

    @property
    def score(self) -> int:
        return self.__score

    @property
    def science_points(self) -> int:
        return self.__science_points

    @property
    def position(self) -> Vector | None:
        return self.__position

    @property
    def movement_speed(self) -> int:
        return self.__movement_speed

    @property
    def drop_rate(self) -> int:
        return self.__drop_rate

    @property
    def abilities(self):
        return self.__abilities

    @company.setter
    def company(self, company: Company) -> None:
        self.__company = company

    @score.setter
    def score(self, score: int) -> None:
        if score is None or not isinstance(score, int):
            raise ValueError(f'{self.__class__.__name__}.score must be an int.')

        if score < 0:
            raise ValueError(f'{self.__class__.__name__}.score must be a positive int.')

        self.__score: int = score

    @science_points.setter
    def science_points(self, points: int) -> None:
        if points is None or not isinstance(points, int):
            raise ValueError(f'{self.__class__.__name__}.science_points must be an int.')

        if points < 0:
            raise ValueError(f'{self.__class__.__name__}.science_points must be a positive int.')

        self.__science_points: int = points

    @position.setter
    def position(self, position: Vector | None) -> None:
        if position is not None and not isinstance(position, Vector):
            raise ValueError(f'{self.__class__.__name__}.position must be a Vector or None.')
        self.__position: Vector | None = position

    @movement_speed.setter
    def movement_speed(self, speed: int) -> None:
        if speed is None or not isinstance(speed, int):
            raise ValueError(f'{self.__class__.__name__}.movement_speed must be an int.')

        if speed < 0:
            raise ValueError(f'{self.__class__.__name__}.movement_speed must be a positive int.')

        self.__movement_speed: int = speed

    @drop_rate.setter
    def drop_rate(self, drop_rate: int) -> None:
        if drop_rate is None or not isinstance(drop_rate, int):
            raise ValueError(f'{self.__class__.__name__}.drop_rate must be an int.')

        if drop_rate < 0:
            raise ValueError(f'{self.__class__.__name__}.drop_rate must be a positive int.')

        self.__drop_rate = drop_rate

    @abilities.setter
    def abilities(self, abilities: dict[bool]) -> None:
        if abilities is None or not isinstance(abilities, dict):
            raise ValueError(f'{self.__class__.__name__}.abilities must be a dict.')

        for ability, value in abilities.items():
            if value is None or not isinstance(value, bool):
                raise ValueError(f'Every value in the {self.__class__.__name__}.abilities dict must be a bool.')

        self.__abilities = abilities

    # Tech Tree methods and implementation------------------------------------------------------------------------------

    # Helper method to create the tech tree
    def __create_tech_tree(self) -> TechTree:
        ...

    def __increase_movement(self, amt: int) -> None:
        ...

    def __increase_drop_rate(self, amt: int) -> None:
        ...

    def __unlock_overdrive_movement(self) -> None:
        ...

    def __unlock_overdrive_mining(self) -> None:
        ...

    def __unlock_dynamite(self) -> None:
        ...

    def __unlock_landmines(self) -> None:
        ...

    def __unlock_emps(self) -> None:
        ...

    def __unlock_trap_defusal(self) -> None:
        ...

    # Helper method to create a dictionary that stores bool values for which abilities the player unlocked
    def __create_abilities_dict(self) -> dict:
        ...

    def buy_new_tech(self, tech_name: str) -> bool:

        ...

    def is_researched(self, tech_name: Tech | str) -> bool:
        ...

    def get_researched_techs(self) -> list[str]:
        ...

    def get_all_tech_names(self) -> list[str]:
        ...
    
    def get_tech_info(self, tech_name: str | Tech) -> TechInfo | None:
        ...

    # Dynamite placing functionality ----------------------------------------------------------------------------------
    # if avatar calls place dynamite, set to true, i.e. they want to place dynamite
    def can_place_dynamite(self) -> bool:
        ...

    def can_place_landmine(self) -> bool:
        ...

    def can_place_emp(self) -> bool:
        ...

    def can_defuse_trap(self) -> bool:
        ...

    # method to return the opposing team based on the avatar's company
    def get_opposing_team(self) -> Company:
        ...

    # method to return your company
    def get_company(self) -> Company:
        ...

    def to_json(self) -> dict:
        ...

    def from_json(self, data: dict) -> Self:
        ...
