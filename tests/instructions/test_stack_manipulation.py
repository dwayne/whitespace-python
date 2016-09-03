import unittest

from whitespace.instructions.stack_manipulation import Discard, Dup, Push, Swap
from whitespace.vm import VM


class PushTestCase(unittest.TestCase):
    def test_it_pushes_a_number_onto_the_value_stack(self):
        vm = VM()

        push = Push(1)
        push.vm = vm

        push.execute()

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 1)


class DupTestCase(unittest.TestCase):
    def test_it_duplicates_the_top_item_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(1)

        dup = Dup()
        dup.vm = vm

        dup.execute()

        self.assertEqual(len(vm.vstack), 2)
        self.assertEqual(vm.vstack.pop(), 1)
        self.assertEqual(vm.vstack.pop(), 1)


class SwapTestCase(unittest.TestCase):
    def test_it_swaps_the_two_top_items_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(1)
        vm.vstack.push(2)

        swap = Swap()
        swap.vm = vm

        swap.execute()

        self.assertEqual(len(vm.vstack), 2)
        self.assertEqual(vm.vstack.pop(), 1)
        self.assertEqual(vm.vstack.pop(), 2)


class DiscardTestCase(unittest.TestCase):
    def test_it_discards_the_top_item_on_the_value_stack(self):
        vm = VM()
        vm.vstack.push(1)

        discard = Discard()
        discard.vm = vm

        discard.execute()

        self.assertEqual(len(vm.vstack), 0)
