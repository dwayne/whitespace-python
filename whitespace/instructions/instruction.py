from abc import ABCMeta, abstractmethod

class Instruction(metaclass=ABCMeta):
    def __init__(self, vm):
        self.vm = vm

    @abstractmethod
    def execute(self):
        pass
