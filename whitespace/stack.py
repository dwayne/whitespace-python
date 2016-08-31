from .error import StackEmptyError


class Stack:
    def __init__(self, name=None):
        self.name = name
        self.elements = []

    def push(self, x):
        self.elements.append(x)

    def pop(self):
        if self.elements:
            return self.elements.pop()
        else:
            raise StackEmptyError(self.name)

    def top(self):
        if self.elements:
            return self.elements[-1]
        else:
            raise StackEmptyError(self.name)

    def __len__(self):
        return len(self.elements)
