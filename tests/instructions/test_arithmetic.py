import unittest

from whitespace.error import ZeroDivisionError
from whitespace.instructions.arithmetic import Add, Div, Mod, Mul, Sub
from whitespace.vm import VM


class AddTestCase(unittest.TestCase):
    def test_it_adds(self):
        vm = VM()
        vm.vstack.push(3)
        vm.vstack.push(2)

        Add().execute(vm)

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 5)


class SubTestCase(unittest.TestCase):
    def test_it_subtracts(self):
        vm = VM()
        vm.vstack.push(3)
        vm.vstack.push(2)

        Sub().execute(vm)

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 1)


class MulTestCase(unittest.TestCase):
    def test_it_multiplies(self):
        vm = VM()
        vm.vstack.push(3)
        vm.vstack.push(2)

        Mul().execute(vm)

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 6)


class DivTestCase(unittest.TestCase):
    def test_it_divides(self):
        vm = VM()
        vm.vstack.push(7)
        vm.vstack.push(2)

        Div().execute(vm)

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 3)

    def test_when_divisor_is_zero(self):
        vm = VM()
        vm.vstack.push(1)
        vm.vstack.push(0)

        with self.assertRaisesRegex(ZeroDivisionError, 'integer division by zero'):
            Div().execute(vm)


class ModTestCase(unittest.TestCase):
    def test_it_mods(self):
        vm = VM()
        vm.vstack.push(7)
        vm.vstack.push(2)

        Mod().execute(vm)

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 1)

    def test_when_divisor_is_zero(self):
        vm = VM()
        vm.vstack.push(1)
        vm.vstack.push(0)

        with self.assertRaisesRegex(ZeroDivisionError, 'modulo by zero'):
            Mod().execute(vm)
