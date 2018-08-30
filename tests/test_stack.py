import unittest

from whitespace.error import StackEmptyError
from whitespace.stack import Stack


class StackTestCase(unittest.TestCase):
    def test_it_works_like_a_stack(self):
        stack = Stack()

        with self.assertRaises(StackEmptyError):
            stack.pop()

        with self.assertRaises(StackEmptyError):
            stack.top()

        stack.push(3)
        stack.push(2)
        stack.push(1)

        self.assertEqual(stack.top(), 1)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.top(), 2)

        stack.pop()

        self.assertEqual(len(stack), 1)

        stack.pop()

        self.assertTrue(stack.empty())


class NamedStackTestCase(unittest.TestCase):
    def test_name_is_included_in_error_message(self):
        stack = Stack('a stack')

        with self.assertRaisesRegex(StackEmptyError, 'a stack'):
            stack.pop()

        with self.assertRaisesRegex(StackEmptyError, 'a stack'):
            stack.top()
