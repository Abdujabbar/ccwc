from io import TextIOWrapper, BytesIO
from ccwc.utils import process
from ccwc.cli import get_user_input


def run(args):
    lines = []
    if not args.files:
        raw = process(TextIOWrapper(BytesIO(get_user_input().encode())), args)
        lines.append(to_str(raw))
    else:
        for file in args.files:
            try:
                with open(file) as stream:
                    raw = process(stream, args)
                    raw.append(f"{file}")

                    lines.append(to_str(raw))
            except Exception as ex:
                lines.append(str(ex))

    return "\n".join(lines)


def to_str(arr):
    for x in range(len(arr)):
        arr[x] = f"{arr[x]:7} "

    return " ".join(arr)
