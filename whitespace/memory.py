from .error import AddressMissingError


class Memory:
    def __init__(self):
        self.cells = {}

    def __getitem__(self, address):
        if address in self.cells:
            return self.cells[address]
        else:
            raise AddressMissingError(address)

    def __setitem__(self, address, value):
        self.cells[address] = value
