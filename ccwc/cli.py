import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog='ccwc',
        description='ccwc is clone of wc linux command',
    )
    parser.add_argument('-c', '--count', action='store_true', default=True)
    parser.add_argument('-l', '--lines', action='store_true', default=True)
    parser.add_argument('-w', '--words', action='store_true')
    parser.add_argument('-m', '--chars', action='store_true')

    parser.add_argument('files', nargs='*')

    return parser.parse_args()
