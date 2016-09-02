from ..error import Halt, LabelMissingError
from .instruction import Instruction


class Label(Instruction):
    def __init__(self, name):
        super(Label, self).__init__()
        self.name = name

    def execute(self):
        pass

    def _execute(self):
        pass


class Call(Instruction):
    def __init__(self, name):
        super(Call, self).__init__()
        self.name = name

    def _execute(self):
        index = find_label(self.vm.instructions, self.name)
        self.vm.cstack.push(self.vm.pc)
        self.vm.pc = index + 1


class Ujmp(Instruction):
    def __init__(self, name):
        super(Ujmp, self).__init__()
        self.name = name

    def _execute(self):
        index = find_label(self.vm.instructions, self.name)
        self.vm.pc = index + 1


class Zjmp(Instruction):
    def __init__(self, name):
        super(Zjmp, self).__init__()
        self.name = name

    def _execute(self):
        test_value = self.vm.vstack.pop()

        if test_value == 0:
            index = find_label(self.vm.instructions, self.name)
            self.vm.pc = index + 1


class Njmp(Instruction):
    def __init__(self, name):
        super(Njmp, self).__init__()
        self.name = name

    def _execute(self):
        test_value = self.vm.vstack.pop()

        if test_value < 0:
            index = find_label(self.vm.instructions, self.name)
            self.vm.pc = index + 1


class Ret(Instruction):
    def _execute(self):
        self.vm.pc = self.vm.cstack.pop()


class End(Instruction):
    def execute(self):
        raise Halt

    def _execute(self):
        pass


def find_label(instructions, name):
    for index, instruction in enumerate(instructions):
        if isinstance(instruction, Label) and instruction.name == name:
            return index
    raise LabelMissingError(name)
