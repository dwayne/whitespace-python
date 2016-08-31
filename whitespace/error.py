"""Exception classes raised by whitespace.

The base exception class is WhitespaceError, which inherits from Exception. It
doesn't define any behavior of its own, but is the base class for all exceptions
defined in this package.
"""

import builtins


class WhitespaceError(Exception):
    pass


class AddressMissingError(WhitespaceError, KeyError):
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return str(self.address)


class StackEmptyError(WhitespaceError, IndexError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        if self.name:
            return self.name
        else:
            return ''


class ZeroDivisionError(WhitespaceError, builtins.ZeroDivisionError):
    pass
