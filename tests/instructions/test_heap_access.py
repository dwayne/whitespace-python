import unittest

from whitespace.instructions.heap_access import Retrieve, Store
from whitespace.vm import VM


class TestStore(unittest.TestCase):
    def test_it_stores_the_value_at_the_given_address(self):
        vm = VM()
        vm.vstack.push(1000)
        vm.vstack.push(1)

        Store(vm).execute()

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.memory[1000], 1)


class TestRetrieve(unittest.TestCase):
    def test_it_retrieves_the_value_from_the_given_address(self):
        vm = VM()
        vm.memory[1000] = 5
        vm.vstack.push(1000)

        Retrieve(vm).execute()

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 5)
