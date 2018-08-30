from collections import namedtuple

from .error import ParseError
from .instructions import *


SPACE, TAB, LF = ' ', '\t', '\n'
TOKENS = [SPACE, TAB, LF]


SourceLocation = namedtuple(
    'SourceLocation',
    'start_index start_line start_column end_index end_line end_column'
)


class Parser:
    def __call__(self, src):
        return self._parse(src)

    def _parse(self, src):
        self._instructions = []

        self._src = src
        self._src_length = len(src)

        self._current_index = -1
        self._current_line = 0
        self._current_column = -1

        self._start_index = -1
        self._start_line = 0
        self._start_column = -1

        self._substart_index = -1
        self._substart_line = 0
        self._substart_column = -1

        self._next_line = False

        return self._parse_start()

    def _parse_start(self):
        t = self._next_token()

        self._capture_start()

        if t == SPACE:
            return self._parse_stack_manipulation()
        elif t == TAB:
            t = self._next_token()
            if t == SPACE:
                return self._parse_arithmetic()
            elif t == TAB:
                return self._parse_heap_access()
            elif t == LF:
                return self._parse_io()
            else:
                raise self._parse_error('expected an IMP')
        elif t == LF:
            return self._parse_flow_control()
        else:
            return self._instructions

    def _parse_stack_manipulation(self):
        t = self._next_token()

        if t == SPACE:
            n = self._parse_number()
            return self._capture_instruction_and_continue(Push(n))
        elif t == LF:
            t = self._next_token()

            if t == SPACE:
                return self._capture_instruction_and_continue(Dup())
            elif t == TAB:
                return self._capture_instruction_and_continue(Swap())
            elif t == LF:
                return self._capture_instruction_and_continue(Discard())
            else:
                raise self._parse_error('expected a stack manipulation instruction')
        else:
            raise self._parse_error('expected a stack manipulation instruction')

    def _parse_arithmetic(self):
        t = self._next_token()

        if t == SPACE:
            t = self._next_token()

            if t == SPACE:
                return self._capture_instruction_and_continue(Add())
            elif t == TAB:
                return self._capture_instruction_and_continue(Sub())
            elif t == LF:
                return self._capture_instruction_and_continue(Mul())
            else:
                raise self._parse_error('expected an arithmetic instruction')
        elif t == TAB:
            t = self._next_token()

            if t == SPACE:
                return self._capture_instruction_and_continue(Div())
            elif t == TAB:
                return self._capture_instruction_and_continue(Mod())
            else:
                raise self._parse_error('expected an arithmetic instruction')
        else:
            raise self._parse_error('expected an arithmetic instruction')

    def _parse_heap_access(self):
        t = self._next_token()

        if t == SPACE:
            return self._capture_instruction_and_continue(Store())
        elif t == TAB:
            return self._capture_instruction_and_continue(Retrieve())
        else:
            raise self._parse_error('expected a heap access instruction')

    def _parse_flow_control(self):
        t = self._next_token()

        if t == SPACE:
            t = self._next_token()

            if t == SPACE:
                name = self._parse_label()
                return self._capture_instruction_and_continue(Label(name))
            elif t == TAB:
                name = self._parse_label()
                return self._capture_instruction_and_continue(Call(name))
            elif t == LF:
                name = self._parse_label()
                return self._capture_instruction_and_continue(Ujmp(name))
            else:
                raise self._parse_error('expected a flow control instruction')
        elif t == TAB:
            t = self._next_token()

            if t == SPACE:
                name = self._parse_label()
                return self._capture_instruction_and_continue(Zjmp(name))
            elif t == TAB:
                name = self._parse_label()
                return self._capture_instruction_and_continue(Njmp(name))
            elif t == LF:
                return self._capture_instruction_and_continue(Ret())
            else:
                raise self._parse_error('expected a flow control instruction')
        elif t == LF:
            t = self._next_token()

            if t == LF:
                return self._capture_instruction_and_continue(End())
            else:
                raise self._parse_error('expected a flow control instruction')
        else:
            raise self._parse_error('expected a flow control instruction')

    def _parse_io(self):
        t = self._next_token()

        if t == SPACE:
            t = self._next_token()

            if t == SPACE:
                return self._capture_instruction_and_continue(Putc())
            elif t == TAB:
                return self._capture_instruction_and_continue(Putn())
            else:
                raise self._parse_error('expected an I/O instruction')
        elif t == TAB:
            t = self._next_token()

            if t == SPACE:
                return self._capture_instruction_and_continue(Getc())
            elif t == TAB:
                return self._capture_instruction_and_continue(Getn())
            else:
                raise self._parse_error('expected an I/O instruction')
        else:
            raise self._parse_error('expected an I/O instruction')

    def _parse_number(self):
        return self._parse_sign() * self._parse_positive_number()

    def _parse_sign(self):
        t = self._next_token()

        self._capture_substart()

        if t == SPACE:
            return 1
        elif t == TAB:
            return -1
        else:
            raise self._parse_error('expected a sign')

    def _parse_positive_number(self):
        t = self._next_token()

        self._capture_substart()

        return self._parse_positive_number_rec(0, 0, t)

    def _parse_positive_number_rec(self, n, l, t):
        if t == SPACE:
            return self._parse_positive_number_rec(2 * n, l + 1, self._next_token())
        elif t == TAB:
            return self._parse_positive_number_rec(2 * n + 1, l + 1, self._next_token())
        elif t == LF:
            if l > 0:
                return n
            else:
                raise self._parse_error('expected a number')
        else:
            raise self._parse_error('expected the number to be LF terminated')

    def _parse_label(self):
        t = self._next_token()

        self._capture_substart()

        return self._parse_label_rec('', 0, t)

    def _parse_label_rec(self, name, l, t):
        if t == SPACE or t == TAB:
            return self._parse_label_rec(name + t, l + 1, self._next_token())
        elif t == LF:
            if l > 0:
                return name
            else:
                raise self._parse_error('expected a non-empty label')
        else:
            raise self._parse_error('expected the label to be LF terminated')

    def _next_token(self):
        if self._current_index + 1 == self._src_length:
            return None

        if self._next_line:
            self._next_line = False
            self._current_line += 1
            self._current_column = -1

        self._current_index += 1
        self._current_column += 1
        c = self._c()

        while c and c not in TOKENS:
            if self._current_index + 1 == self._src_length:
                return None

            self._current_index += 1
            self._current_column += 1
            c = self._c()

        if c == LF:
            self._next_line = True

        return c

    def _c(self):
        return self._src[self._current_index]

    def _capture_start(self):
        self._start_index = self._current_index
        self._start_line = self._current_line
        self._start_column = self._current_column

        self._capture_substart()

    def _capture_substart(self):
        self._substart_index = self._current_index
        self._substart_line = self._current_line
        self._substart_column = self._current_column

    def _capture_instruction_and_continue(self, instruction):
        instruction.source_location = SourceLocation(
            self._start_index, self._start_line, self._start_column,
            self._current_index, self._current_line, self._current_column
        )

        self._instructions.append(instruction)

        return self._parse_start()

    def _parse_error(self, message):
        line_from_info = 'see from line {}, column {}'.format(
            self._substart_line, self._substart_column
        )

        if self._current_index + 1 == self._src_length:
            line_to_info = 'to the end'
        else:
            line_to_info = 'to line {}, column {}'.format(
                self._current_line, self._current_column
            )

        return ParseError('{}, {} {}'.format(message, line_from_info, line_to_info))


parse = Parser()
