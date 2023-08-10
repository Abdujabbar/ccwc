from io import TextIOWrapper, BytesIO
from ccwc.utils import process


def run(args):
    result = []
    if not args.files:
        raw = process(
            TextIOWrapper(BytesIO(get_content_from_terminal().encode())), args
        )
        result.append(" ".join(apply_padding(raw)))
    else:
        for file in args.files:
            try:
                with open(file) as stream:
                    raw = process(stream, args)
                    raw.append(f"{file:10}")

                    result.append(" ".join(raw))
            except Exception as ex:
                result.append(str(ex))

    return "\n".join(result)


def get_content_from_terminal():
    contents = []
    while 1:
        try:
            contents.append(input())
        except EOFError:
            break

    return "\n".join(contents)


def apply_padding(arr):
    for x in range(len(arr)):
        arr[x] = f"{arr[x]:6}"
