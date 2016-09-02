import unittest

from whitespace.error import ParseError
from whitespace.instructions import *
from whitespace.parser import Parser, SourceLocation


parser = Parser()


class TestParser(unittest.TestCase):
    def test_it_parses_push(self):
        instructions = parser.parse('  \t\t \t\n')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Push)
        self.assertEqual(instruction.n, -5)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 6, 0, 6))

    def test_it_parses_dup(self):
        instructions = parser.parse(' \n ')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Dup)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 2, 1, 0))

    def test_it_parses_swap(self):
        instructions = parser.parse(' \n\t')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Swap)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 2, 1, 0))

    def test_it_parses_discard(self):
        instructions = parser.parse(' \n\n')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Discard)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 2, 1, 0))

    def test_it_parses_add(self):
        instructions = parser.parse('\t   ')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Add)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 3, 0, 3))

    def test_it_parses_sub(self):
        instructions = parser.parse('\t  \t')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Sub)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 3, 0, 3))

    def test_it_parses_mul(self):
        instructions = parser.parse('\t  \n')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Mul)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 3, 0, 3))

    def test_it_parses_div(self):
        instructions = parser.parse('\t \t ')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Div)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 3, 0, 3))

    def test_it_parses_mod(self):
        instructions = parser.parse('\t \t\t')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Mod)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 3, 0, 3))

    def test_it_parses_store(self):
        instructions = parser.parse('\t\t ')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Store)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 2, 0, 2))

    def test_it_parses_retrieve(self):
        instructions = parser.parse('\t\t\t')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Retrieve)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 2, 0, 2))

    def test_it_parses_label(self):
        instructions = parser.parse('\n   \n')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Label)
        self.assertEqual(instruction.name, ' ')
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 4, 1, 3))

    def test_it_parses_call(self):
        instructions = parser.parse('\n \t \n')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Call)
        self.assertEqual(instruction.name, ' ')
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 4, 1, 3))

    def test_it_parses_ujmp(self):
        instructions = parser.parse('\n \n \n')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Ujmp)
        self.assertEqual(instruction.name, ' ')
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 4, 2, 1))

    def test_it_parses_zjmp(self):
        instructions = parser.parse('\n\t  \n')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Zjmp)
        self.assertEqual(instruction.name, ' ')
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 4, 1, 3))

    def test_it_parses_njmp(self):
        instructions = parser.parse('\n\t\t \n')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Njmp)
        self.assertEqual(instruction.name, ' ')
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 4, 1, 3))

    def test_it_parses_ret(self):
        instructions = parser.parse('\n\t\n')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Ret)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 2, 1, 1))

    def test_it_parses_end(self):
        instructions = parser.parse('\n\n\n')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, End)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 2, 2, 0))

    def test_it_parses_putc(self):
        instructions = parser.parse('\t\n  ')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Putc)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 3, 1, 1))

    def test_it_parses_putn(self):
        instructions = parser.parse('\t\n \t')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Putn)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 3, 1, 1))

    def test_it_parses_getc(self):
        instructions = parser.parse('\t\n\t ')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Getc)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 3, 1, 1))

    def test_it_parses_getn(self):
        instructions = parser.parse('\t\n\t\t')
        instruction = instructions[0]

        self.assertEqual(len(instructions), 1)
        self.assertIsInstance(instruction, Getn)
        self.assertEqual(instruction.source_location, SourceLocation(0, 0, 0, 3, 1, 1))


class TestInstructionParseErrors(unittest.TestCase):
    def test_imp_errors(self):
        with self.assertRaisesRegex(ParseError, 'expected an IMP'):
            parser.parse('\t')

    def test_stack_manipulation_instruction_errors(self):
        for src in [' ', ' \t', ' \n']:
            with self.assertRaisesRegex(ParseError, 'expected a stack manipulation instruction'):
                parser.parse(src)

    def test_arithmetic_instruction_errors(self):
        for src in ['\t ', '\t \n', '\t  ', '\t \t', '\t \t\n']:
            with self.assertRaisesRegex(ParseError, 'expected an arithmetic instruction'):
                parser.parse(src)

    def test_heap_access_instruction_errors(self):
        for src in ['\t\t', '\t\t\n']:
            with self.assertRaisesRegex(ParseError, 'expected a heap access instruction'):
                parser.parse(src)

    def test_flow_control_instruction_errors(self):
        for src in ['\n', '\n ', '\n\t', '\n\n', '\n\n ', '\n\n\t']:
            with self.assertRaisesRegex(ParseError, 'expected a flow control instruction'):
                parser.parse(src)

    def test_io_instruction_errors(self):
        for src in ['\t\n', '\t\n ', '\t\n\t', '\t\n\n', '\t\n \n', '\t\n\t\n']:
            with self.assertRaisesRegex(ParseError, 'expected an I/O instruction'):
                parser.parse(src)


class TestNumberParsing(unittest.TestCase):
    def test_it_parses_1(self):
        instruction = parser.parse('   \t\n')[0]

        self.assertEqual(instruction.n, 1)

    def test_it_parses_2(self):
        instruction = parser.parse('   \t \n')[0]

        self.assertEqual(instruction.n, 2)

    def test_it_parses_5(self):
        instruction = parser.parse('   \t \t\n')[0]

        self.assertEqual(instruction.n, 5)

    def test_it_parses_0(self):
        # There is an infinite number of representations of 0
        for src in ['    \n', '  \t \n', '     \n', '  \t  \n']:
            instruction = parser.parse(src)[0]

            self.assertEqual(instruction.n, 0)

    def test_it_parses_negative_1(self):
        instruction = parser.parse('  \t\t\n')[0]

        self.assertEqual(instruction.n, -1)

    def test_it_parses_negative_2(self):
        instruction = parser.parse('  \t\t \n')[0]

        self.assertEqual(instruction.n, -2)

    def test_it_parses_negative_5(self):
        instruction = parser.parse('  \t\t \t\n')[0]

        self.assertEqual(instruction.n, -5)

    def test_it_must_have_a_sign_part(self):
        for src in ['  ', '  \n']:
            with self.assertRaisesRegex(ParseError, 'expected a sign'):
                parser.parse(src)

    def test_it_must_have_a_positive_number_part(self):
        for src in ['   \n', '  \t\n']:
            with self.assertRaisesRegex(ParseError, 'expected a number'):
                parser.parse(src)

    def test_it_must_be_lf_terminated(self):
        for src in ['   \t', '  \t\t']:
            with self.assertRaisesRegex(ParseError, 'expected the number to be LF terminated'):
                parser.parse(src)

    def test_it_pinpoints_the_error(self):
        with self.assertRaisesRegex(ParseError, 'line 0, column 1 to the end'):
            parser.parse('  ')

        with self.assertRaisesRegex(ParseError, 'line 0, column 3 to the end'):
            parser.parse('   \n')

        with self.assertRaisesRegex(ParseError, 'line 0, column 3 to the end'):
            parser.parse('   \t')


class TestLabelParsing(unittest.TestCase):
    def test_it_parses_lf_terminated_spaces_tabs(self):
        for src, name in [('\n   \n', ' '), ('\n  \t\n', '\t'), ('\n  \t \t  \n', '\t \t  ')]:
            instruction = parser.parse(src)[0]

            self.assertEqual(instruction.name, name)

    def test_it_must_be_non_empty(self):
        with self.assertRaisesRegex(ParseError, 'expected a non-empty label'):
            parser.parse('\n  \n')

    def test_it_must_be_lf_terminated(self):
        with self.assertRaisesRegex(ParseError, 'expected the label to be LF terminated'):
            parser.parse('\n   ')

    def test_it_pinpoints_the_error(self):
        with self.assertRaisesRegex(ParseError, 'line 1, column 2 to the end'):
            parser.parse('\n  \n')

        with self.assertRaisesRegex(ParseError, 'line 1, column 2 to the end'):
            parser.parse('\n   ')
