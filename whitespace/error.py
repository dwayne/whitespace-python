"""Exception classes raised by whitespace.

The base exception class is WhitespaceError, which inherits from Exception. It
doesn't define any behavior of its own, but is the base class for all exceptions
defined in this package.
"""

import builtins


class WhitespaceError(Exception):
    pass


class ParseError(WhitespaceError):
    pass


class RuntimeError(WhitespaceError):
    pass


class AddressMissingError(RuntimeError, KeyError):
    pass


class LabelMissingError(RuntimeError, IndexError):
    pass


class StackEmptyError(RuntimeError, IndexError):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def __str__(self):
        return str(self._name)


class OutOfBoundsError(RuntimeError, IndexError):
    pass


class ZeroDivisionError(RuntimeError, builtins.ZeroDivisionError):
    pass


class IOError(RuntimeError):
    pass


class Halt(RuntimeError):
    pass
