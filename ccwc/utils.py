from io import SEEK_END


def process(stream, args):
    res = []
    count_bytes = args.count
    count_lines = args.lines
    count_words = args.words
    count_chars = args.chars

    if count_bytes:
        res.append(get_bytes(stream))

    if count_lines:
        res.append(get_lines_count(stream))

    if count_words:
        res.append(get_words_count(stream))

    if count_chars:
        res.append(get_chars_count(stream))

    return res


def get_bytes(stream):
    stream.seek(0, SEEK_END)
    total_bytes = stream.tell()
    stream.seek(0)
    return total_bytes


def get_lines_count(stream):
    return sum([1 for _ in stream])


def get_words_count(stream):
    return sum([len(words.split()) for words in stream.readlines()])


def get_chars_count(stream):
    return 0
