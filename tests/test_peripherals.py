import io
import unittest

from whitespace.error import IOError
from whitespace.peripherals import TestKeyboard, TestScreen


class KeyboardTestCase(unittest.TestCase):
    def setUp(self):
        self.keyboard = TestKeyboard()

    def tearDown(self):
        self.keyboard.detach()

    def test_getc(self):
        self.keyboard.enter('97')

        c = self.keyboard.getc()

        self.assertEqual(c, '9')

    def test_getc_eof(self):
        with self.assertRaisesRegex(IOError, 'unexpected EOF'):
            self.keyboard.getc()

    def test_getn_one_line(self):
        self.keyboard.enter('97')

        n = self.keyboard.getn()

        self.assertEqual(n, 97)

    def test_getn_multiple_lines(self):
        self.keyboard.enter('9\n7')

        n = self.keyboard.getn()

        self.assertEqual(n, 9)

    def test_getn_not_a_number(self):
        self.keyboard.enter('a')

        with self.assertRaisesRegex(IOError, 'not a number: a'):
            self.keyboard.getn()

    def test_getn_eof(self):
        with self.assertRaisesRegex(IOError, 'unexpected EOF'):
            self.keyboard.getn()


class ScreenTestCase(unittest.TestCase):
    def setUp(self):
        self.screen = TestScreen()

    def tearDown(self):
        self.screen.turnOff()

    def test_putc_for_valid_input(self):
        self.screen.putc(97)

        self.assertEqual(self.screen.contents, 'a')

    def test_putc_for_invalid_input(self):
        with self.assertRaisesRegex(IOError, 'invalid Unicode code point: -97'):
            self.screen.putc(-97)

    def test_putn(self):
        self.screen.putn(97)

        self.assertEqual(self.screen.contents, '97')
