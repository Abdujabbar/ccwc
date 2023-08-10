from ccwc.cli import parse_args
from ccwc.command import run


def main():
    args = parse_args()

    print(run(args))