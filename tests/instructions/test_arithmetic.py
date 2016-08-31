import unittest

from whitespace.error import ZeroDivisionError
from whitespace.instructions.arithmetic import Add, Div, Mod, Mul, Sub
from whitespace.vm import VM


class TestAdd(unittest.TestCase):
    def test_it_adds_the_top_two_items_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(3)
        vm.vstack.push(2)

        Add(vm).execute()

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 5)


class TestSub(unittest.TestCase):
    def test_it_subtracts_the_top_two_items_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(3)
        vm.vstack.push(2)

        Sub(vm).execute()

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 1)


class TestMul(unittest.TestCase):
    def test_it_multiplies_the_top_two_items_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(3)
        vm.vstack.push(2)

        Mul(vm).execute()

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 6)


class TestDiv(unittest.TestCase):
    def test_it_divides_the_top_two_items_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(7)
        vm.vstack.push(2)

        Div(vm).execute()

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 3)

    def test_when_divisor_is_zero(self):
        vm = VM()
        vm.vstack.push(1)
        vm.vstack.push(0)

        with self.assertRaisesRegex(ZeroDivisionError, 'integer division by zero'):
            Div(vm).execute()


class TestMod(unittest.TestCase):
    def test_it_computes_the_remainder_of_the_top_two_items_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(7)
        vm.vstack.push(2)

        Mod(vm).execute()

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 1)

    def test_when_divisor_is_zero(self):
        vm = VM()
        vm.vstack.push(1)
        vm.vstack.push(0)

        with self.assertRaisesRegex(ZeroDivisionError, 'modulo by zero'):
            Mod(vm).execute()
