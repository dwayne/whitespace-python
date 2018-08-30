import operator

from ..error import ZeroDivisionError
from .instruction import Instruction


class Add(Instruction):
    def execute(self, vm):
        _compute(vm, operator.add)


class Sub(Instruction):
    def execute(self, vm):
        _compute(vm, operator.sub)


class Mul(Instruction):
    def execute(self, vm):
        _compute(vm, operator.mul)


class Div(Instruction):
    def execute(self, vm):
        _compute(vm, _div)


class Mod(Instruction):
    def execute(self, vm):
        _compute(vm, _mod)


def _div(a, b):
    if b == 0:
        raise ZeroDivisionError('integer division by zero')

    return a // b


def _mod(a, b):
    if b == 0:
        raise ZeroDivisionError('modulo by zero')

    return a % b


def _compute(vm, op):
    b = vm.vstack.pop()
    a = vm.vstack.pop()
    vm.vstack.push(op(a, b))
