import unittest


from whitespace.error import AddressMissingError
from whitespace.memory import Memory


class MemoryTestCase(unittest.TestCase):
    def test_store_value_at_address(self):
        memory = Memory()
        memory[1] = 'value'

        self.assertEqual(memory[1], 'value')

    def test_raises_error_for_missing_address(self):
        memory = Memory()

        with self.assertRaisesRegex(AddressMissingError, '1'):
            memory[1]
