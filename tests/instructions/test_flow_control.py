import unittest

from whitespace.error import Halt, LabelMissingError
from whitespace.instructions.flow_control import Call, End, Label, Njmp, Ret, Ujmp, Zjmp
from whitespace.instructions.instruction import Noop
from whitespace.vm import VM


noop = Noop()


class CallTestCase(unittest.TestCase):
    def test_it_calls_a_subroutine(self):
        vm = VM()
        vm.instructions = [
            noop,
            Label('f'),
            noop,
            noop,
            noop
        ]
        vm.pc = 4

        Call('f').execute(vm)

        self.assertEqual(len(vm.cstack), 1)
        self.assertEqual(vm.cstack.top(), 4)
        self.assertEqual(vm.pc, 2)


class UjmpTestCase(unittest.TestCase):
    def test_it_does_an_unconditional_jump(self):
        vm = VM()
        vm.instructions = [
            Label('loop'),
            noop,
            noop
        ]
        vm.pc = 2

        Ujmp('loop').execute(vm)

        self.assertEqual(vm.pc, 1)


class ZjmpTestCase(unittest.TestCase):
    def test_it_jumps_if_zero(self):
        vm = VM()
        vm.instructions = [
            Label('loop'),
            noop,
            noop
        ]
        vm.vstack.push(0)
        vm.pc = 2

        Zjmp('loop').execute(vm)

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.pc, 1)

    def test_it_does_not_jump_if_non_zero(self):
        vm = VM()
        vm.instructions = [
            Label('loop'),
            noop,
            noop
        ]
        vm.vstack.push(1)
        vm.pc = 2

        Zjmp('loop').execute(vm)

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.pc, 2)


class NjmpNegativeTestCase(unittest.TestCase):
    def test_it_jumps_if_negative(self):
        vm = VM()
        vm.instructions = [
            Label('loop'),
            noop,
            noop
        ]
        vm.vstack.push(-1)
        vm.pc = 2

        Njmp('loop').execute(vm)

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.pc, 1)

    def test_it_does_not_jump_if_non_negative(self):
        vm = VM()
        vm.instructions = [
            Label('loop'),
            noop,
            noop
        ]
        vm.vstack.push(0)
        vm.pc = 2

        Njmp('loop').execute(vm)

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.pc, 2)


class RetTestCase(unittest.TestCase):
    def test_it_returns(self):
        vm = VM()
        vm.cstack.push(5)

        self.assertEqual(vm.pc, 0)

        Ret().execute(vm)

        self.assertEqual(len(vm.cstack), 0)
        self.assertEqual(vm.pc, 5)


class EndTestCase(unittest.TestCase):
    def test_it_raises_halt(self):
        vm = VM()

        with self.assertRaises(Halt):
            End().execute(vm)
