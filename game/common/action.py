from game.common.enums import *


class Action:

    def __init__(self):
        self.object_type = ObjectType.ACTION
        self._example_action = None

    def set_action(self, action):
        ...

    def to_json(self):
        ...

    def from_json(self, data):
        ...

    def __str__(self):
        ...
