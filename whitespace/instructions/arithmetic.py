from ..error import ZeroDivisionError
from .instruction import Instruction


class Add(Instruction):
    def execute(self):
        _compute(self.vm, '+')


class Sub(Instruction):
    def execute(self):
        _compute(self.vm, '-')


class Mul(Instruction):
    def execute(self):
        _compute(self.vm, '*')


class Div(Instruction):
    def execute(self):
        _compute(self.vm, '/')


class Mod(Instruction):
    def execute(self):
        _compute(self.vm, '%')


def _div(x, y):
    if y == 0:
        raise ZeroDivisionError('integer division by zero')
    else:
        return x // y


def _mod(x, y):
    if y == 0:
        raise ZeroDivisionError('modulo by zero')
    else:
        return x % y


_binops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': _div,
    '%': _mod
}


def _compute(vm, op):
    right = vm.vstack.pop()
    left = vm.vstack.pop()
    vm.vstack.push(_binops[op](left, right))
