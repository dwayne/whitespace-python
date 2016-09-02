from .console import Console
from .parser import Parser
from .vm import VM


def eval(src, console=Console()):
    parser = Parser()
    vm = VM(console=console)
    vm.load(parser.parse(src))
    vm.run()
