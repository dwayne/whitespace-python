from .parser import parse
from .peripherals import Keyboard, Screen
from .vm import VM


def eval(src, *, keyboard=Keyboard(), screen=Screen(), parse=parse):
    vm = VM()
    vm.keyboard = keyboard
    vm.screen = screen
    vm.instructions = parse(src)
    vm.run()
