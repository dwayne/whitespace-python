import io
import sys

from .error import IOError


class Keyboard:
    def __init__(self, *, input=sys.stdin):
        self._input = input

    def getc(self):
        c = self._input.read(1)

        if not c:
            raise IOError('unexpected EOF')

        return c

    def getn(self):
        s = self._input.readline()

        if not s:
            raise IOError('unexpected EOF')

        try:
            n = int(s, 10)
        except ValueError:
            raise IOError('not a number: %s' % s)
        else:
            return n


class TestKeyboard(Keyboard):
    def __init__(self, typed=''):
        super().__init__(input=io.StringIO(typed))

    def enter(self, typed):
        self._input.write(typed)
        self._input.seek(0)

    def detach(self):
        self._input.close()


class Screen:
    def __init__(self, *, output=sys.stdout):
        self._output = output

    def putc(self, n):
        try:
            c = chr(n)
        except ValueError:
            raise IOError('invalid Unicode code point: %d' % n)
        else:
            self._write(c)

    def putn(self, n):
        self._write(str(n))

    def _write(self, s):
        self._output.write(s)
        self._output.flush()


class TestScreen(Screen):
    def __init__(self):
        super().__init__(output=io.StringIO())

    @property
    def contents(self):
        return self._output.getvalue()

    def turnOff(self):
        self._output.close()
