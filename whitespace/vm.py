from .console import Console
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

        # TODO: Execute instructions

    def _reset(self):
        self.vstack = Stack('vstack')
        self.cstack = Stack('cstack')
        self.memory = Memory()
        self.pc = 0
