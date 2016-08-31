import io
import unittest

from whitespace.error import ConsoleError
from whitespace.console import Console


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = Console(input=None, output=io.StringIO())

    def tearDown(self):
        if self.console.input:
            self.console.input.close()
        self.console.output.close()

    def test_putc_when_code_point_is_valid(self):
        self.console.putc(97)

        self.assertEqual(self.console.output.getvalue(), 'a')

    def test_putc_when_code_point_is_invalid(self):
        with self.assertRaisesRegex(ConsoleError, 'invalid Unicode code point: -97'):
            self.console.putc(-97)

    def test_putn(self):
        self.console.putn(97)

        self.assertEqual(self.console.output.getvalue(), '97')

    def test_getc(self):
        self.console.input = io.StringIO('97')

        c = self.console.getc()

        self.assertEqual(c, '9')

    def test_getc_eof(self):
        self.console.input = io.StringIO()

        with self.assertRaisesRegex(ConsoleError, 'unexpected EOF'):
            self.console.getc()

    def test_getn_one_line(self):
        self.console.input = io.StringIO('97')

        n = self.console.getn()

        self.assertEqual(n, 97)

    def test_getn_multiple_lines(self):
        self.console.input = io.StringIO('9\n7')

        n = self.console.getn()

        self.assertEqual(n, 9)

    def test_getn_not_a_number(self):
        self.console.input = io.StringIO('a')

        with self.assertRaisesRegex(ConsoleError, 'not a number: a'):
            self.console.getn()

    def test_getn_eof(self):
        self.console.input = io.StringIO()

        with self.assertRaisesRegex(ConsoleError, 'unexpected EOF'):
            self.console.getn()
