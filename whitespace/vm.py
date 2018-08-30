from .error import Halt, LabelMissingError, OutOfBoundsError
from .instructions import Label
from .memory import Memory
from .stack import Stack


class VM:
    def __init__(self):
        self.instructions = []
        self._reset()

    def find_label(self, name):
        for loc, instruction in enumerate(self.instructions):
            if isinstance(instruction, Label) and instruction.name == name:
                return loc

        raise LabelMissingError(name)

    def run(self):
        self._reset()

        try:
            while True:
                instruction = self._fetch_instruction()
                self.pc += 1
                instruction.execute(self)
        except Halt:
            pass

    def _reset(self):
        self.vstack = Stack('value stack')
        self.cstack = Stack('call stack')
        self.memory = Memory()
        self.pc = 0

    def _fetch_instruction(self):
        try:
            return self.instructions[self.pc]
        except IndexError:
            raise OutOfBoundsError('program counter: %d' % self.pc)
