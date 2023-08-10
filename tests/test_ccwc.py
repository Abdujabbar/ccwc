import pytest
from ccwc.utils import process
from . import get_fixture_path
from argparse import Namespace


@pytest.mark.parametrize('filename, expected', [
    ('empty.txt', [0, 0, 0, 0]),
    ('single-char.txt', [1, 1, 0, 0]),
    ('multilines.txt', [128, 3, 0, 0]),
    ('big-content.txt', [335191,7188,0,0]),
])
def test_process_files(filename, expected):
    full_path = get_fixture_path(filename)

    with open(full_path) as stream:
        assert process(stream, Namespace(count=1, lines=1, words=1, chars=1)) == expected