import unittest


from whitespace.error import StackEmptyError
from whitespace.stack import Stack


class EmptyStackTestCase(unittest.TestCase):
    def setUp(self):
        self.empty_stack = Stack()

    def test_push(self):
        self.empty_stack.push(5)

        self.assertEqual(self.empty_stack.top(), 5)

    def test_pop(self):
        with self.assertRaises(StackEmptyError):
            self.empty_stack.pop()

    def test_top(self):
        with self.assertRaises(StackEmptyError):
            self.empty_stack.top()

    def test_len(self):
        self.assertEqual(len(self.empty_stack), 0)


class NonEmptyStackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        for x in range(1, 4):
            self.stack.push(2 * x)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 6)
        self.assertEqual(len(self.stack), 2)

    def test_top(self):
        self.assertEqual(self.stack.top(), 6)
        self.assertEqual(len(self.stack), 3)


class NamedStackTestCase(unittest.TestCase):
    def test_name_is_included_in_error_message(self):
        stack = Stack('named stack')

        with self.assertRaisesRegex(StackEmptyError, 'named stack'):
            stack.pop()

        with self.assertRaisesRegex(StackEmptyError, 'named stack'):
            stack.top()
