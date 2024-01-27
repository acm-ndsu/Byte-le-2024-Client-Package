import threading
import traceback

from game.common.enums import ActionType


class Thread(threading.Thread):

    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.args = args
        self.func = func
        self.result: list[ActionType] = []
        self.error = None

    def run(self):
        ...


class CommunicationThread(Thread):

    def __init__(self, func, args=None, variable_type=None):
        super().__init__(func, args)
        self.type = variable_type

        class InternalObject:
            def __init__(self):
                self.value = None

        self.safeObject = InternalObject()

    def run(self):
        ...

    def retrieve_value(self):
        ...

