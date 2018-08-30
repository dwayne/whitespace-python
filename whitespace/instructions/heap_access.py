from .instruction import Instruction


class Store(Instruction):
    def execute(self, vm):
        value = vm.vstack.pop()
        address = vm.vstack.pop()

        vm.memory[address] = value


class Retrieve(Instruction):
    def execute(self, vm):
        address = vm.vstack.pop()

        vm.vstack.push(vm.memory[address])
