from typing import Callable


class AvatarFunctions:

    def __init__(self,
                 increase_movement: Callable[[int], None],
                 increase_mining: Callable[[int], None],
                 unlock_movement_overdrive: Callable[[], None],
                 unlock_mining_overdrive: Callable[[], None],
                 unlock_dynamite: Callable[[], None],
                 unlock_landmines: Callable[[], None],
                 unlock_emps: Callable[[], None],
                 unlock_trap_defusal: Callable[[], None]):
        self.increase_movement = increase_movement
        self.increase_mining = increase_mining
        self.unlock_movement_overdrive = unlock_movement_overdrive
        self.unlock_mining_overdrive = unlock_mining_overdrive
        self.unlock_dynamite = unlock_dynamite
        self.unlock_landmines = unlock_landmines
        self.unlock_emps = unlock_emps
        self.unlock_trap_defusal = unlock_trap_defusal
