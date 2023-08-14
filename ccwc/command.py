from io import TextIOWrapper, BytesIO
from ccwc.utils import process
from ccwc.cli import get_user_input


def run(args):
    lines = []
    if not args.files:
        with BytesIO(get_user_input().encode()) as stream:
            raw = process(TextIOWrapper(stream), args)
            lines.append(to_str(raw))
    else:
        for file in args.files:
            try:
                with open(file) as stream:
                    raw = process(stream, args)
                    raw.append(f"{file}")
                    lines.append(to_str(raw))
            except PermissionError:
                lines.append(f"Not enough permission for read: {file}")
            except FileNotFoundError:
                lines.append(f"File {file} doesn't exists")

    return "\n".join(lines)


def to_str(arr):
    return " ".join([f"{arr[x]:7}" for x in range(len(arr))])
