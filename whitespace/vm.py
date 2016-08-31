from .console import Console
from .error import Halt, OutOfBoundsError
from .memory import Memory
from .stack import Stack


class VM:
    def __init__(self, console=Console()):
        self.console = console
        self.instructions = []
        self._reset()

    def load(self, instructions):
        self.instructions = list(instructions)

    def run(self):
        self._reset()

        try:
            self._run_loop()
        except Halt:
            pass

    def _reset(self):
        self.vstack = Stack('vstack')
        self.cstack = Stack('cstack')
        self.memory = Memory()
        self.pc = 0

    def _run_loop(self):
        while True:
            instruction = self._fetch_instruction()
            self.pc += 1
            instruction.execute()

    def _fetch_instruction(self):
        try:
            return self.instructions[self.pc]
        except IndexError:
            raise OutOfBoundsError('program counter: %s' % self.pc)
