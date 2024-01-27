import uuid

from game.common.enums import ObjectType
from typing import Self


class GameObject:
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.object_type = ObjectType.NONE
        self.state = "idle"

    def to_json(self) -> dict:
        ...

    def from_json(self, data: dict) -> Self:
        ...

    def obfuscate(self):
        ...
