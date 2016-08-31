import unittest

from whitespace.error import Halt, LabelMissingError
from whitespace.instructions.flow_control import Call, End, Label, Njmp, Ret, Ujmp, Zjmp, find_label
from whitespace.vm import VM


class TestLabel(unittest.TestCase):
    def test_it_does_not_fail(self):
        Label(None, ' ').execute()


class TestCall(unittest.TestCase):
    def test_it_calls_a_subroutine(self):
        vm = VM()
        vm.load([
            'instruction 1',
            Label(vm, ' '),
            'instruction 3',
            'instruction 4',
            'instruction 5'
        ])
        vm.pc = 4

        Call(vm, ' ').execute()

        self.assertEqual(len(vm.cstack), 1)
        self.assertEqual(vm.cstack.top(), 4)
        self.assertEqual(vm.pc, 2)


class TestUjmp(unittest.TestCase):
    def test_it_changes_the_program_counter_to_the_index_of_the_instruction_after_the_label(self):
        vm = VM()
        vm.load([
            Label(vm, ' '),
            'instruction 2',
            'instruction 3'
        ])
        vm.pc = 2

        Ujmp(vm, ' ').execute()

        self.assertEqual(vm.pc, 1)


class TestZjmpZero(unittest.TestCase):
    def test_it_changes_the_program_counter_to_the_index_of_the_instruction_after_the_label(self):
        vm = VM()
        vm.load([
            Label(vm, ' '),
            'instruction 2',
            'instruction 3'
        ])
        vm.vstack.push(0)
        vm.pc = 2

        Zjmp(vm, ' ').execute()

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.pc, 1)


class TestZjmpNonZero(unittest.TestCase):
    def test_it_does_not_change_the_program_counter(self):
        vm = VM()
        vm.load([
            Label(vm, ' '),
            'instruction 2',
            'instruction 3'
        ])
        vm.vstack.push(1)
        vm.pc = 2

        Zjmp(vm, ' ').execute()

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.pc, 2)


class TestNjmpNegative(unittest.TestCase):
    def test_it_changes_the_program_counter_to_the_index_of_the_instruction_after_the_label(self):
        vm = VM()
        vm.load([
            Label(vm, ' '),
            'instruction 2',
            'instruction 3'
        ])
        vm.vstack.push(-1)
        vm.pc = 2

        Njmp(vm, ' ').execute()

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.pc, 1)


class TestNjmpNonNegative(unittest.TestCase):
    def test_it_does_not_change_the_program_counter(self):
        vm = VM()
        vm.load([
            Label(vm, ' '),
            'instruction 2',
            'instruction 3'
        ])
        vm.vstack.push(0)
        vm.pc = 2

        Njmp(vm, ' ').execute()

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.pc, 2)


class TestRet(unittest.TestCase):
    def test_it_changes_the_program_counter_to_the_value_at_the_top_of_the_call_stack(self):
        vm = VM()
        vm.cstack.push(5)

        Ret(vm).execute()

        self.assertEqual(len(vm.cstack), 0)
        self.assertEqual(vm.pc, 5)


class TestEnd(unittest.TestCase):
    def test_it_raises_halt(self):
        with self.assertRaises(Halt):
            End(None).execute()


class TestFindLabel(unittest.TestCase):
    def setUp(self):
        self.instructions = [
            'instruction 1',
            Label(None, ' '),
            'instruction 3',
            Label(None, '  '),
            'instruction 5'
        ]

    def test_it_returns_index_when_the_label_exists(self):
        index = find_label(self.instructions, '  ')

        self.assertEqual(index, 3)

    def test_it_raises_error_when_the_label_does_not_exist(self):
        with self.assertRaisesRegex(LabelMissingError, '   '):
            find_label(self.instructions, '   ')
