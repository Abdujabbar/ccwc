import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="ccwc",
        description="ccwc is clone of wc linux command",
    )
    parser.add_argument("-c", action="store_true")
    parser.add_argument("-l", action="store_true")
    parser.add_argument("-w", action="store_true")
    parser.add_argument("files", nargs="*")

    return parser.parse_args()


def get_user_input():
    contents = []
    while 1:
        try:
            contents.append(input())
        except EOFError:
            break

    return "\n".join(contents)
