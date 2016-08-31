from .instruction import Instruction


class Push(Instruction):
    def __init__(self, vm, n):
        super(Push, self).__init__(vm)
        self.n = n

    def execute(self):
        self.vm.vstack.push(self.n)


class Dup(Instruction):
    def execute(self):
        self.vm.vstack.push(self.vm.vstack.top())


class Swap(Instruction):
    def execute(self):
        a = self.vm.vstack.pop()
        b = self.vm.vstack.pop()

        self.vm.vstack.push(a)
        self.vm.vstack.push(b)


class Discard(Instruction):
    def execute(self):
        self.vm.vstack.pop()
