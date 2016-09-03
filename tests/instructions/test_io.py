import io
import unittest

from whitespace.console import Console
from whitespace.instructions.io import Getc, Getn, Putc, Putn
from whitespace.vm import VM


class PutcTestCase(unittest.TestCase):
    def test_it_outputs_the_character_at_the_top_of_the_value_stack(self):
        console = Console(output=io.StringIO())
        vm = VM(console=console)
        vm.vstack.push(97)

        putc = Putc()
        putc.vm = vm

        putc.execute()

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(console.output.getvalue(), 'a')

        console.output.close()


class PutnTestCase(unittest.TestCase):
    def test_it_outputs_the_number_at_the_top_of_the_value_stack(self):
        console = Console(output=io.StringIO())
        vm = VM(console=console)
        vm.vstack.push(97)

        putn = Putn()
        putn.vm = vm

        putn.execute()

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(console.output.getvalue(), '97')

        console.output.close()


class GetcTestCase(unittest.TestCase):
    def test_it_reads_a_character_and_places_it_in_the_location_given_by_the_top_of_the_value_stack(self):
        console = Console(input=io.StringIO('ab'))
        vm = VM(console=console)
        vm.vstack.push(100)

        getc = Getc()
        getc.vm = vm

        getc.execute()

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.memory[100], 97)

        console.input.close()


class GetnTestCase(unittest.TestCase):
    def test_it_reads_a_number_and_places_it_in_the_location_given_by_the_top_of_the_value_stack(self):
        console = Console(input=io.StringIO('1234'))
        vm = VM(console=console)
        vm.vstack.push(100)

        getn = Getn()
        getn.vm = vm

        getn.execute()

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.memory[100], 1234)

        console.input.close()
