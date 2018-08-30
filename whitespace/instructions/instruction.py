import abc


class Instruction(abc.ABC):
    @abc.abstractmethod
    def execute(self, vm):
        pass


class Noop(Instruction):
    def execute(self, vm):
        pass
