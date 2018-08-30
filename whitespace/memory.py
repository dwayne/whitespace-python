from .error import AddressMissingError


class Memory:
    def __init__(self):
        self._cells = {}

    def __getitem__(self, address):
        if address in self._cells:
            return self._cells[address]
        else:
            raise AddressMissingError(address)

    def __setitem__(self, address, value):
        self._cells[address] = value
