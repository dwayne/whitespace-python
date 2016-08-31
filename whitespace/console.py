import sys

from .error import ConsoleError


class Console:
    def __init__(self, input=sys.stdin, output=sys.stdout):
        self.input = input
        self.output = output

    def putc(self, n):
        try:
            c = chr(n)
        except ValueError:
            raise ConsoleError('invalid Unicode code point: %s' % n)
        else:
            self.output.write(c)

    def putn(self, n):
        self.output.write(str(n))

    def getc(self):
        c = self.input.read(1)

        if c == '':
            raise ConsoleError('unexpected EOF')
        else:
            return c

    def getn(self):
        s = self.input.readline()

        if s == '':
            raise ConsoleError('unexpected EOF')
        else:
            try:
                n = int(s, 10)
            except ValueError:
                raise ConsoleError('not a number: %s' % s)
            else:
                return n
