from .instruction import Instruction


class Store(Instruction):
    def _execute(self):
        value = self.vm.vstack.pop()
        address = self.vm.vstack.pop()

        self.vm.memory[address] = value


class Retrieve(Instruction):
    def _execute(self):
        address = self.vm.vstack.pop()

        self.vm.vstack.push(self.vm.memory[address])
