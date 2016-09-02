from abc import ABCMeta, abstractmethod


class Instruction(metaclass=ABCMeta):
    def __init__(self):
        self.vm = None
        self.source_location = None

    def execute(self):
        if self.vm:
            self._execute()
        else:
            raise AssertionError('VM must be set')

    @abstractmethod
    def _execute(self):
        pass


class Noop(Instruction):
    def execute(self):
        pass

    def _execute(self):
        pass
