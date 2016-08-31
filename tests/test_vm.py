import io
import unittest

from whitespace.console import Console
from whitespace.error import OutOfBoundsError
from whitespace.instructions import *
from whitespace.vm import VM


class TestVM(unittest.TestCase):
    def test_it_executes_each_instruction_one_by_one_until_an_end_instruction_is_reached(self):
        vm = VM()
        vm.load([
            Push(vm, 3),
            Dup(vm),
            Mul(vm),
            End(vm),
            Dup(vm)
        ])

        vm.run()

        self.assertEqual(len(vm.vstack), 1)
        self.assertEqual(vm.vstack.top(), 9)

    def test_it_raises_error_when_no_end_instruction_is_reached(self):
        vm = VM()
        vm.load([
            Push(vm, 3),
            Dup(vm),
            Mul(vm)
        ])

        with self.assertRaisesRegex(OutOfBoundsError, 'program counter: 3'):
            vm.run()


class TestCountProgram(unittest.TestCase):
    def test_it_counts_from_1_to_10(self):
        console = Console(output=io.StringIO())
        vm = VM(console=console)
        vm.load([
            Push(vm, 1),        # Put a 1 on the stack
            Label(vm, ' '),     # Set a Label at this point
            Dup(vm),            # Duplicate the top stack item
            Putn(vm),           # Output the current value
            Push(vm, 10),       # Put 10 (newline) on the stack...
            Putc(vm),           # ...and output the newline
            Push(vm, 1),        # Put a 1 on the stack
            Add(vm),            # Increment our current value
            Dup(vm),            # Duplicate the value to test it
            Push(vm, 11),       # Push 11 onto the stack
            Sub(vm),            # Subtraction
            Zjmp(vm, '\t'),     # If we have a 0, jump to the end
            Ujmp(vm, ' '),      # Jump to the start
            Label(vm, '\t'),    # Set the end label
            Discard(vm),        # Discard our accumulator, to be tidy
            End(vm)             # Finish
        ])

        vm.run()

        self.assertEqual(console.output.getvalue(), '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n')

        console.output.close()
