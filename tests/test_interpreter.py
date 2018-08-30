import io
import os
import unittest

from whitespace.peripherals import TestKeyboard, TestScreen
from whitespace.interpreter import eval


def src(name):
    path = os.path.join(os.path.dirname(__file__), 'fixtures/{}.ws'.format(name))

    with open(path, encoding='utf-8') as f:
        return f.read()


class EvalTestCase(unittest.TestCase):
    def setUp(self):
        self.keyboard = TestKeyboard()
        self.screen = TestScreen()

    def tearDown(self):
        self.keyboard.detach()
        self.screen.turnOff()

    def test_it_evaluates_count_ws(self):
        eval(src('count'), screen=self.screen)

        self.assertEqual(self.screen.contents, '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n')

    def test_it_evaluates_fact_ws(self):
        self.keyboard.enter('40')

        eval(src('fact'), keyboard=self.keyboard, screen=self.screen)

        self.assertEqual(
            self.screen.contents,
            'Enter a number: '
            '40! = 815915283247897734345611269596115894272000000000\r\n'
        )

    def test_it_evaluates_hello_ws(self):
        eval(src('hello'), screen=self.screen)

        self.assertEqual(self.screen.contents, 'Hello, world of spaces!\r\n')

    def test_it_evaluates_name_ws(self):
        self.keyboard.enter('Dwayne\n')

        eval(src('name'), keyboard=self.keyboard, screen=self.screen)

        self.assertEqual(
            self.screen.contents,
            'Please enter your name: '
            'Hello Dwayne\n\r\n'
        )
