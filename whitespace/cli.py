from .interpreter import eval


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='A Whitespace interpreter.'
    )

    parser.add_argument('src',
        type=argparse.FileType('r', encoding='utf-8'),
        help='source file to evaluate'
    )

    args = parser.parse_args()

    eval(args.src.read())

    return 0
