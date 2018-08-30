from .instruction import Instruction


class Push(Instruction):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def execute(self, vm):
        vm.vstack.push(self.n)


class Dup(Instruction):
    def execute(self, vm):
        vm.vstack.push(vm.vstack.top())


class Swap(Instruction):
    def execute(self, vm):
        a = vm.vstack.pop()
        b = vm.vstack.pop()

        vm.vstack.push(a)
        vm.vstack.push(b)


class Discard(Instruction):
    def execute(self, vm):
        vm.vstack.pop()
