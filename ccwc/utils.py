from io import SEEK_END


def process(stream, args):
    result = []
    count_bytes = args.c
    count_lines = args.l
    count_words = args.w
    count_chars = args.m

    if not any([count_bytes, count_lines, count_words]):
        result.append(get_lines_count(stream))
        result.append(get_words_count(stream))
        result.append(get_bytes(stream))

    if count_lines:
        result.append(get_lines_count(stream))

    if count_words:
        result.append(get_words_count(stream))

    if count_bytes:
        result.append(get_bytes(stream))

    if count_chars:
        result.append(get_chars_count(stream))

    return result


def get_bytes(stream):
    stream.seek(0, SEEK_END)
    total_bytes = stream.tell()
    return total_bytes


def get_lines_count(stream):
    return sum([1 for _ in stream])


def get_words_count(stream):
    stream.seek(0)
    return sum([len(words.split()) for words in stream.readlines()])


def get_chars_count(stream):
    return get_bytes(stream)
