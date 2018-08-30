from .instruction import Instruction


class Putc(Instruction):
    def execute(self, vm):
        n = vm.vstack.pop()
        vm.screen.putc(n)


class Putn(Instruction):
    def execute(self, vm):
        n = vm.vstack.pop()
        vm.screen.putn(n)


class Getc(Instruction):
    def execute(self, vm):
        c = vm.keyboard.getc()
        address = vm.vstack.pop()
        vm.memory[address] = ord(c)


class Getn(Instruction):
    def execute(self, vm):
        address = vm.vstack.pop()
        vm.memory[address] = vm.keyboard.getn()
