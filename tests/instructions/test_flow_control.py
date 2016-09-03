import unittest

from whitespace.error import Halt, LabelMissingError
from whitespace.instructions.flow_control import Call, End, Label, Njmp, Ret, Ujmp, Zjmp, find_label
from whitespace.instructions.instruction import Noop
from whitespace.vm import VM


class LabelTestCase(unittest.TestCase):
    def test_it_does_not_fail(self):
        Label(' ').execute()


class CallTestCase(unittest.TestCase):
    def test_it_calls_a_subroutine(self):
        vm = VM()
        vm.load([
            Noop(),
            Label(' '),
            Noop(),
            Noop(),
            Noop()
        ])
        vm.pc = 4

        call = Call(' ')
        call.vm = vm

        call.execute()

        self.assertEqual(len(vm.cstack), 1)
        self.assertEqual(vm.cstack.top(), 4)
        self.assertEqual(vm.pc, 2)


class UjmpTestCase(unittest.TestCase):
    def test_it_changes_the_program_counter_to_the_index_of_the_instruction_after_the_label(self):
        vm = VM()
        vm.load([
            Label(' '),
            Noop(),
            Noop()
        ])
        vm.pc = 2

        ujmp = Ujmp(' ')
        ujmp.vm = vm

        ujmp.execute()

        self.assertEqual(vm.pc, 1)


class ZjmpZeroTestCase(unittest.TestCase):
    def test_it_changes_the_program_counter_to_the_index_of_the_instruction_after_the_label(self):
        vm = VM()
        vm.load([
            Label(' '),
            Noop(),
            Noop()
        ])
        vm.vstack.push(0)
        vm.pc = 2

        zjmp = Zjmp(' ')
        zjmp.vm = vm

        zjmp.execute()

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.pc, 1)


class ZjmpNonZeroTestCase(unittest.TestCase):
    def test_it_does_not_change_the_program_counter(self):
        vm = VM()
        vm.load([
            Label(' '),
            Noop(),
            Noop()
        ])
        vm.vstack.push(1)
        vm.pc = 2

        zjmp = Zjmp(' ')
        zjmp.vm = vm

        zjmp.execute()

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.pc, 2)


class NjmpNegativeTestCase(unittest.TestCase):
    def test_it_changes_the_program_counter_to_the_index_of_the_instruction_after_the_label(self):
        vm = VM()
        vm.load([
            Label(' '),
            Noop(),
            Noop()
        ])
        vm.vstack.push(-1)
        vm.pc = 2

        njmp = Njmp(' ')
        njmp.vm = vm

        njmp.execute()

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.pc, 1)


class NjmpNonNegativeTestCase(unittest.TestCase):
    def test_it_does_not_change_the_program_counter(self):
        vm = VM()
        vm.load([
            Label(' '),
            Noop(),
            Noop()
        ])
        vm.vstack.push(0)
        vm.pc = 2

        njmp = Njmp(' ')
        njmp.vm = vm

        njmp.execute()

        self.assertEqual(len(vm.vstack), 0)
        self.assertEqual(vm.pc, 2)


class RetTestCase(unittest.TestCase):
    def test_it_changes_the_program_counter_to_the_value_at_the_top_of_the_call_stack(self):
        vm = VM()
        vm.cstack.push(5)

        ret = Ret()
        ret.vm = vm

        ret.execute()

        self.assertEqual(len(vm.cstack), 0)
        self.assertEqual(vm.pc, 5)


class EndTestCase(unittest.TestCase):
    def test_it_raises_halt(self):
        end = End()

        with self.assertRaises(Halt):
            end.execute()


class FindLabelTestCase(unittest.TestCase):
    def setUp(self):
        self.instructions = [
            Noop(),
            Label(' '),
            Noop(),
            Label('  '),
            Noop()
        ]

    def test_it_returns_index_when_the_label_exists(self):
        index = find_label(self.instructions, '  ')

        self.assertEqual(index, 3)

    def test_it_raises_error_when_the_label_does_not_exist(self):
        with self.assertRaisesRegex(LabelMissingError, '   '):
            find_label(self.instructions, '   ')
