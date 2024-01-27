from game.common.action import Action
from game.common.game_object import GameObject
from game.common.avatar import Avatar
from game.common.enums import *
from game.client.user_client import UserClient


class Player(GameObject):
    def __init__(self, code: object | None = None, team_name: str | None = None, actions: list[ActionType] = [],
                 avatar: Avatar | None = None):
        super().__init__()
        self.object_type: ObjectType = ObjectType.PLAYER
        self.functional: bool = True
        self.error: str | None = None
        self.file_name: str | None = None
        self.team_name: str | None = team_name
        self.code: UserClient | None = code
        # self.action: Action = action
        self.actions: list[ActionType] = actions
        self.avatar: Avatar | None = avatar

    @property
    def error(self) -> str | None:
        return self.__error

    @error.setter
    def error(self, error: str | None) -> None:
        if error is not None and not isinstance(error, str):
            raise ValueError(f'{self.__class__.__name__}.error must be either a string or None.')
        self.__error = error

    @property
    def actions(self) -> list[ActionType] | list:  # change to Action if you want to use the action object
        return self.__actions

    @actions.setter
    def actions(self, actions: list[ActionType] | list) -> None:  # showing it returns nothing(like void in java)
        # if it's (not none = and) if its (none = or)
        # going across all action types and making it a boolean, if any are true this will be true\/
        if actions is None or not isinstance(actions, list) \
                or (len(actions) > 0
                    and any(map(lambda action_type: not isinstance(action_type, ActionType), actions))):
            raise ValueError(f'{self.__class__.__name__}.action must be an empty list or a list of action types')
            # ^if it's not either throw an error
        self.__actions = actions

    @property
    def functional(self) -> bool:
        return self.__functional

    @functional.setter  # do this for all the setters
    def functional(self, functional: bool) -> None:  # this enforces the type hinting
        if functional is None or not isinstance(functional, bool):  # if this statement is true throw an error
            raise ValueError(f'{self.__class__.__name__}.functional must be a boolean')
        self.__functional = functional

    @property
    def team_name(self) -> str | None:
        return self.__team_name

    @team_name.setter
    def team_name(self, team_name: str | None) -> None:
        if team_name is not None and not isinstance(team_name, str):
            raise ValueError(f'{self.__class__.__name__}.team_name must be a String or None')
        self.__team_name = team_name

    @property
    def file_name(self) -> str | None:
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name: str | None) -> None:
        if file_name is not None and not isinstance(file_name, str):
            raise ValueError(f'{self.__class__.__name__}.file_name must be a String or None')
        self.__file_name = file_name

    @property
    def avatar(self) -> Avatar:
        return self.__avatar

    @avatar.setter
    def avatar(self, avatar: Avatar) -> None:
        if avatar is not None and not isinstance(avatar, Avatar):
            raise ValueError(f'{self.__class__.__name__}.avatar must be Avatar or None')
        self.__avatar = avatar

    @property
    def object_type(self) -> ObjectType:
        return self.__object_type

    @object_type.setter
    def object_type(self, object_type: ObjectType) -> None:
        if object_type is None or not isinstance(object_type, ObjectType):
            raise ValueError(f'{self.__class__.__name__}.object_type must be ObjectType')
        self.__object_type = object_type

    def to_json(self):
        ...

    def from_json(self, data):
        ...

# to String
    def __str__(self):
        ...
