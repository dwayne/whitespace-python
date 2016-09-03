import unittest

from whitespace.error import ZeroDivisionError
from whitespace.instructions.arithmetic import Add, Div, Mod, Mul, Sub
from whitespace.vm import VM


class AddTestCase(unittest.TestCase):
    def test_it_adds_the_top_two_items_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(3)
        vm.vstack.push(2)

        add = Add()
        add.vm = vm

        add.execute()

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 5)


class SubTestCase(unittest.TestCase):
    def test_it_subtracts_the_top_two_items_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(3)
        vm.vstack.push(2)

        sub = Sub()
        sub.vm = vm

        sub.execute()

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 1)


class MulTestCase(unittest.TestCase):
    def test_it_multiplies_the_top_two_items_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(3)
        vm.vstack.push(2)

        mul = Mul()
        mul.vm = vm

        mul.execute()

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 6)


class DivTestCase(unittest.TestCase):
    def test_it_divides_the_top_two_items_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(7)
        vm.vstack.push(2)

        div = Div()
        div.vm = vm

        div.execute()

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 3)

    def test_when_divisor_is_zero(self):
        vm = VM()
        vm.vstack.push(1)
        vm.vstack.push(0)

        div = Div()
        div.vm = vm

        with self.assertRaisesRegex(ZeroDivisionError, 'integer division by zero'):
            div.execute()


class ModTestCase(unittest.TestCase):
    def test_it_computes_the_remainder_of_the_top_two_items_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(7)
        vm.vstack.push(2)

        mod = Mod()
        mod.vm = vm

        mod.execute()

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 1)

    def test_when_divisor_is_zero(self):
        vm = VM()
        vm.vstack.push(1)
        vm.vstack.push(0)

        mod = Mod()
        mod.vm = vm

        with self.assertRaisesRegex(ZeroDivisionError, 'modulo by zero'):
            mod.execute()
