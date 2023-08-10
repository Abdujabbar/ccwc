from io import TextIOWrapper, BytesIO
from ccwc.utils import process

def run(args):
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
                    for x in range(len(raw)):
                        raw[x] = f"{raw[x]:6}"
                    raw.append(f"{file:10}")

                    result.append(' '.join(raw))
            except Exception as ex:
                result.append(str(ex))
    
    return "\n".join(result)
