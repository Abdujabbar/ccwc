from ccwc.cli import parse_args
from ccwc.utils import process
from io import TextIOWrapper, BytesIO

def main():
    args = parse_args()

    result = []
    if not args.files:
        contents = []
        while 1:
            try:
                contents.append(input())
            except EOFError as ex:
                break
        raw = process(TextIOWrapper(BytesIO('\n'.join(contents).encode())), args)
        
        result.append(' '.join(map(str, raw)))
    else:
        for file in args.files:
            try:
                with open(file) as stream:
                    raw = process(stream, args)
                    result.append(' '.join(map(str, raw)))
            except Exception as ex:
                result.append(str(ex))

    print("\n".join(result))
