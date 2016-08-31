from .instruction import Instruction


class Putc(Instruction):
    def execute(self):
        n = self.vm.vstack.pop()
        self.vm.console.putc(n)


class Putn(Instruction):
    def execute(self):
        n = self.vm.vstack.pop()
        self.vm.console.putn(n)


class Getc(Instruction):
    def execute(self):
        c = self.vm.console.getc()
        address = self.vm.vstack.pop()
        self.vm.memory[address] = ord(c)


class Getn(Instruction):
    def execute(self):
        address = self.vm.vstack.pop()
        self.vm.memory[address] = self.vm.console.getn()
