from ..error import Halt
from .instruction import Instruction, Noop


class Label(Noop):
    def __init__(self, name):
        super().__init__()
        self.name = name


class Call(Instruction):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def execute(self, vm):
        loc = vm.find_label(self.name)
        vm.cstack.push(vm.pc)
        vm.pc = loc + 1


class Ujmp(Instruction):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def execute(self, vm):
        loc = vm.find_label(self.name)
        vm.pc = loc + 1


class Zjmp(Instruction):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def execute(self, vm):
        test_value = vm.vstack.pop()

        if test_value == 0:
            loc = vm.find_label(self.name)
            vm.pc = loc + 1


class Njmp(Instruction):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def execute(self, vm):
        test_value = vm.vstack.pop()

        if test_value < 0:
            loc = vm.find_label(self.name)
            vm.pc = loc + 1


class Ret(Instruction):
    def execute(self, vm):
        vm.pc = vm.cstack.pop()


class End(Instruction):
    def execute(self, vm):
        raise Halt
