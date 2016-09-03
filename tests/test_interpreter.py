import io
import os
import unittest

from whitespace.console import Console
from whitespace.interpreter import eval


def src(name):
    path = os.path.join(os.path.dirname(__file__), 'fixtures/{}.ws'.format(name))

    with open(path, encoding='utf-8') as f:
        return f.read()


class EvalTestCase(unittest.TestCase):
    def setUp(self):
        self.console = Console(input=None, output=io.StringIO())

    def tearDown(self):
        if self.console.input:
            self.console.input.close()
        self.console.output.close()

    def test_it_evaluates_count_ws(self):
        eval(src('count'), console=self.console)

        self.assertEqual(
            self.console.output.getvalue(),
            '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'
        )

    def test_it_evaluates_fact_ws(self):
        self.console.input = io.StringIO('40')

        eval(src('fact'), console=self.console)

        self.assertEqual(
            self.console.output.getvalue(),
            'Enter a number: '
            '40! = 20397882081197443358640281739902897356800000000\r\n'
        )

    def test_it_evaluates_hello_ws(self):
        eval(src('hello'), console=self.console)

        self.assertEqual(
            self.console.output.getvalue(),
            'Hello, world of spaces!\r\n'
        )

    def test_it_evaluates_name_ws(self):
        self.console.input = io.StringIO('Dwayne\n')

        eval(src('name'), console=self.console)

        self.assertEqual(
            self.console.output.getvalue(),
            'Please enter your name: '
            'Hello Dwayne\n\r\n'
        )
