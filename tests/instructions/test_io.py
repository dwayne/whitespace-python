import io
import unittest

from whitespace.instructions.io import Getc, Getn, Putc, Putn
from whitespace.peripherals import TestKeyboard, TestScreen
from whitespace.vm import VM


class PutcTestCase(unittest.TestCase):
    def test_it_outputs_the_character_at_the_top_of_the_value_stack(self):
        screen = TestScreen()

        vm = VM()
        vm.screen = screen
        vm.vstack.push(97)

        Putc().execute(vm)

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(screen.contents, 'a')

        screen.turnOff()


class PutnTestCase(unittest.TestCase):
    def test_it_outputs_the_number_at_the_top_of_the_value_stack(self):
        screen = TestScreen()

        vm = VM()
        vm.screen = screen
        vm.vstack.push(97)

        Putn().execute(vm)

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(screen.contents, '97')

        screen.turnOff()


class GetcTestCase(unittest.TestCase):
    def test_it_reads_a_character_and_places_it_at_the_address_on_the_top_of_the_value_stack(self):
        keyboard = TestKeyboard('ab')

        vm = VM()
        vm.keyboard = keyboard
        vm.vstack.push(100)

        Getc().execute(vm)

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.memory[100], 97)

        keyboard.detach()


class GetnTestCase(unittest.TestCase):
    def test_it_reads_a_number_and_places_it_at_the_address_on_the_top_of_the_value_stack(self):
        keyboard = TestKeyboard('1234')

        vm = VM()
        vm.keyboard = keyboard
        vm.vstack.push(100)

        Getn().execute(vm)

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.memory[100], 1234)

        keyboard.detach()
