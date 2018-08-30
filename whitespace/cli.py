import argparse
import logging

from .error import ParseError, RuntimeError
from .interpreter import eval


def main(args=None):
    ns = _argument_parser().parse_args(args)

    try:
        eval(ns.src.read())
    except ParseError:
        logging.exception('Please check your code. There was a problem parsing it.')
        return 1
    except RuntimeError:
        logging.exception('Please check your code. There was a problem executing it.')
        return 1
    except:
        logging.exception('Sorry, an unexpected error occurred.')
        return 2

    return 0


def _argument_parser():
    parser = argparse.ArgumentParser(description='A Whitespace interpreter.')

    parser.add_argument('src',
        type=argparse.FileType('r', encoding='utf-8'),
        help='the whitespace source code to execute'
    )

    return parser
